
import time
import requests
from pricing_data.pricing_api.reg_price_models import Pricing
import threading

start = time.time()

vm_pricing_list = []

def fetch_vm_prices(lower_bound, upper_bound=None):
    url = f"https://prices.azure.com/api/retail/prices?$filter=serviceName eq 'Virtual Machines'&$skip={lower_bound}"
    session = requests.Session()
    flag = True

    while(url and flag):
        print(url)
        json_data = session.get(url).json()

        for row in json_data['Items']:
            if row["serviceName"] == "Virtual Machines":  
                data = Pricing(currencyCode=row["currencyCode"], tierMinimumUnits=row["tierMinimumUnits"],
                                retailPrice=row["retailPrice"], unitPrice=row["unitPrice"],
                                armRegionName=row["armRegionName"], location=row["location"],
                                effectiveStartDate=row["effectiveStartDate"], meterId=row["meterId"],
                                meterName=row["meterName"], productId=row["productId"],
                                skuId=row["skuId"],
                                productName=row["productName"], skuName=row["skuName"],
                                serviceName=row["serviceName"], serviceId=row["serviceId"],
                                serviceFamily=row["serviceFamily"], unitOfMeasure=row["unitOfMeasure"],
                                type=row["type"], isPrimaryMeterRegion=row["isPrimaryMeterRegion"],
                                armSkuName=row["armSkuName"]
                            )
                vm_pricing_list.append(data)

        url = json_data['NextPageLink']
        lower_bound += 100

        if upper_bound:
            if lower_bound > upper_bound:
                flag = False
        else: 
            flag = True

def execute_thread():
    incremental_value = 29700
    lower_bound = 0
    upper_bound = incremental_value

    thread_count = 10
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

def save_vm_prices():
    Pricing.objects.bulk_create(vm_pricing_list)

execute_thread()
save_vm_prices()

end = time.time()

elapsed_time=(end-start)
print('Execution time:', elapsed_time, 'seconds')