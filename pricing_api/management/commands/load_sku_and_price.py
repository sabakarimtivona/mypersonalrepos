import time
import requests
import threading
from pricing_api.models.vm_sku_models import VmSizes , Pricing
from pricing_api.data_collection.vm_sku_details import vm_sku_list
from django.core.management.base import BaseCommand
import pandas
import datetime , logging

logger = logging.getLogger('django')

class Command(BaseCommand):
    help = "extracts the vmsku data from api , process it and loads it in the databse"
    
    
    def handle(self, *args, **options):
        self.load_data_to_db()
    
    
    def load_data_to_db(self):
        
        def load_vm_size_data(vm_sku_list):
            logger.info("object instance creation for vmsku started at "+str(datetime.datetime.now())+' hours!')

            for vm_sku in vm_sku_list:
                VmSizes.objects.update_or_create(
                            vm_sku_name=vm_sku["vm_sku_name"],
                            vm_sku_details=vm_sku["vm_sku_detail"],
                            family =         vm_sku["family"],
                            vCPUs =          vm_sku["vCPUs"],
                            MemoryGB =       vm_sku["MemoryGB"],
                            location =       vm_sku["location"],
                )

            logger.info("finished loading sku objects with the values at "+str(datetime.datetime.now())+' hours!')

                
        def load_vm_price():
            """
            Load the vm price data into the Postgres
            """
            start = time.time()
            obj_create = []
            def get_orm_action(row):

                unit_price_obj = Pricing.objects.filter(skuId=row["skuId"],location=row["location"],
                                                     effectiveStartDate=row["effectiveStartDate"],type=row["type"],currencyCode=row["currencyCode"]).values('unitPrice')
                
                if unit_price_obj:
                    return "ignore" if unit_price_obj[0]['unitPrice'] == row["unitPrice"] else "update"
                else:
                    return "create"

            def fetch_vm_prices(lower_bound, upper_bound=None):
                url = f"https://prices.azure.com/api/retail/prices?$filter=serviceName eq 'Virtual Machines'&$skip={lower_bound}"
                session = requests.Session()
                flag = True
                all_data=[]
                time_string = time.strftime("%Y %m %d - %H %M ")
                file_name = f"mismatched_dataset_details_{time_string}.csv"

                while(url and flag):
                    print(url)
                    try:
                        json_data = session.get(url).json()
                    except Exception as e:
                        print(f"Error occurs when fetching URL: {e}")

                    for row in json_data['Items']:
                        if row["serviceName"] == "Virtual Machines":  
                            try:
                            
                                action = get_orm_action(row)

                                if action == "create":
                                
                                    obj_create.append(Pricing(currencyCode=row["currencyCode"],tierMinimumUnits=row["tierMinimumUnits"],retailPrice=row["retailPrice"],unitPrice=row["unitPrice"],armRegionName=row["armRegionName"],location=row["location"],effectiveStartDate=row["effectiveStartDate"],meterId=row["meterId"],meterName=row["meterName"],productId=row["productId"],skuId=row["skuId"],productName=row["productName"],skuName=row["skuName"],serviceName=row["serviceName"], serviceId=row["serviceId"],serviceFamily=row["serviceFamily"],unitOfMeasure=row["unitOfMeasure"],type=row["type"],isPrimaryMeterRegion=row["isPrimaryMeterRegion"],armSkuName=row["armSkuName"],vmsize=VmSizes.objects.get(location__iexact=row["armRegionName"], vm_sku_name__iexact=row["armSkuName"])))

                                elif action == "update":
                                
                                    Pricing.objects.update(currencyCode=row["currencyCode"], location=row["location"],skuId=row["skuId"],type=row["type"],effectiveStartDate=row['effectiveStartDate'], defaults={
                                        'productName':row["productName"],'skuName':row["skuName"],'serviceName':row["serviceName"], 'serviceId':row["serviceId"],'serviceFamily':row["serviceFamily"],'unitOfMeasure':row["unitOfMeasure"],'isPrimaryMeterRegion':row["isPrimaryMeterRegion"],'armSkuName':row["armSkuName"],'meterId':row["meterId"],'meterName':row["meterName"],'productId':["productId"],
                                        'armRegionName':row["armRegionName"],'tierMinimumUnits':row["tierMinimumUnits"],'retailPrice':row['retailPrice'],'unitPrice':row['unitPrice']})
                            except:
                                reason = "mismatched_sku_detail"
                                all_data.append({"armSkuName" : row["armSkuName"], "armRegionName" : row["armRegionName"], "currencyCode": row["currencyCode"],"tierMinimumUnits":row["tierMinimumUnits"],"retailPrice":row["retailPrice"],"unitPrice": row["unitPrice"],"location": row["location"],"effectiveStartDate":row["effectiveStartDate"],"meterId":row["meterId"],"meterName":row["meterName"],"productId": row["productId"],"skuId":row["skuId"],"productName":row["productName"],"skuName":row["skuName"],"serviceName":row["serviceName"],"serviceId":row["serviceId"],"serviceFamily":row["serviceFamily"],"unitOfMeasure":row["unitOfMeasure"],"type":row["type"],"isPrimaryMeterRegion":row["isPrimaryMeterRegion"],"mismatched_reason": reason})    

                    url = json_data['NextPageLink']
                    lower_bound += 100

                    if upper_bound:
                        if lower_bound > upper_bound:
                            flag = False
                    else: 
                        flag = True
                df=pandas.DataFrame(all_data)
                df.to_csv(path_or_buf=file_name,mode="w")
            
            
            def execute_thread():
                incremental_value = 15000
                lower_bound = 0
                upper_bound = incremental_value

                thread_count = 20
                thread_objects = []
                for count in range(thread_count):
                    if count == thread_count-1:
                        a = threading.Thread(target=fetch_vm_prices, args=(lower_bound,))
                    else:    
                        a = threading.Thread(target=fetch_vm_prices, args=(lower_bound, upper_bound,))
                    lower_bound, upper_bound = upper_bound+100, upper_bound+incremental_value
                    a.start()
                    thread_objects.append(a)

                for thread in thread_objects:
                    thread.join()

                if obj_create:
                    Pricing.objects.bulk_create(obj_create)

            
            execute_thread()
            end = time.time()
            elapsed_time=(end-start)
            print('Execution time : ',elapsed_time,'seconds')
            print("Data migration completed")
        load_vm_size_data(vm_sku_list)
        load_vm_price()
        
        