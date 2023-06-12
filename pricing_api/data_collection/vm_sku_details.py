import os
import requests
import logging
import datetime
from pricing_api.data_collection.locations import location_display_names

logger = logging.getLogger(__name__)
def get_access_token():
    creds = {
        "grant_type": "client_credentials",
        'client_id': os.environ.get('CLIENT_ID'),
        'client_secret': os.environ.get('CLIENT_SECRET'),
        'scope' : 'https://management.azure.com/.default',
    }
    tenant = os.environ.get('TENANT')
    request_token_url: str = (
            f"https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token"
    )
    access_token = requests.post(request_token_url, data=creds).json()['access_token']
    logger.info(" access token generation "+access_token)
    return access_token
access_token = get_access_token()



def get_vm_sku_data():
    header={'Authorization': 'Bearer ' + access_token}
    subscription = os.environ.get('SUBSCRIPTION_ID')
    url = f"https://management.azure.com/subscriptions/{subscription}/providers/Microsoft.Compute/skus?api-version=2021-07-01"
    response = requests.get(url, headers=header)
    logger.info("the resposnse code of url %s",str(response.status_code))
    return response
response = get_vm_sku_data()
vm_sku_json = response.json()

vm_sku_list=[]


invalidLocationInSkuData = []
def process_collected_data(location_display_names):  
        logger.info("processing collected data started"+str(datetime.datetime.now())+' hours!')
        for row in vm_sku_json['value']:
            if row["resourceType"] == "virtualMachines":
                for vmskulocation in row["locations"]:
                    if vmskulocation.lower() in location_display_names:
                        processed_json_data = {
                            "vm_sku_name": row["name"],
                            "vm_sku_detail":  dict(row),
                            "family" : row["family"],
                            "location" : vmskulocation
                            }
                        for capabilities in row["capabilities"]:
                            if capabilities["name"]== "vCPUs":
                                processed_json_data["vCPUs"] = capabilities["value"]
                            if capabilities["name"]== "MemoryGB":
                                processed_json_data["MemoryGB"] = capabilities["value"]
                        vm_sku_list.append(processed_json_data)
                    else:
                            invalidLocationInSkuData.append(vmskulocation)
        res = [*set(invalidLocationInSkuData)]
        logger.info("processing collected data finished"+str(datetime.datetime.now())+' hours!')
        return vm_sku_list , res
vm_sku_list , invalidLocationInSkuData = process_collected_data(location_display_names)