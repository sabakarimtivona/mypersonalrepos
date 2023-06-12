import json
from sku_api.models import vm_sizes
import requests
import json
import os

def run():
    """def get_access_token():
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
    return access_token

access_token = get_access_token()    

"""




    access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyIsImtpZCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldC8iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC83NWYyYTk5Yi0wMWZkLTQ4ZjItYWM2MC1kNGE3YTQ0ZmQwY2MvIiwiaWF0IjoxNjgwMDYzNTcwLCJuYmYiOjE2ODAwNjM1NzAsImV4cCI6MTY4MDA2ODIyOSwiYWNyIjoiMSIsImFpbyI6IkFWUUFxLzhUQUFBQWRsdnQ5cmdFTVF2YmE5Vm5xeFdnMm8rUnFTbm9ndG0vdXlDUnVzZms3R0kzTU1SdVF5elZFbzNsRHArcTF0K2hQTGFrN2lybHlDM29rTkdHdVlPTjhBbnQzQ3JwRW55bkdHM2syOHFHTHBJPSIsImFtciI6WyJwd2QiLCJtZmEiXSwiYXBwaWQiOiIwNGIwNzc5NS04ZGRiLTQ2MWEtYmJlZS0wMmY5ZTFiZjdiNDYiLCJhcHBpZGFjciI6IjAiLCJmYW1pbHlfbmFtZSI6IkoiLCJnaXZlbl9uYW1lIjoiSW5pZ28iLCJncm91cHMiOlsiZjU2ZjNlY2MtNThmMy00NmE2LThmZGQtMTFmNmJkZjk0YWI2Il0sImlwYWRkciI6IjQ5LjM3LjIxMC4yNTEiLCJuYW1lIjoiSW5pZ28gSiIsIm9pZCI6ImRiNWFlNTdiLWM3MDAtNGZiZC04ZTc2LTRmMDUxYjI4YjE1NyIsInB1aWQiOiIxMDAzMjAwMjRENDFFNjU3IiwicHdkX2V4cCI6IjAiLCJwd2RfdXJsIjoiaHR0cHM6Ly9wb3J0YWwubWljcm9zb2Z0b25saW5lLmNvbS9DaGFuZ2VQYXNzd29yZC5hc3B4IiwicmgiOiIwLkFVa0FtNm55ZGYwQjhraXNZTlNucEVfUXpFWklmM2tBdXRkUHVrUGF3ZmoyTUJOSkFHUS4iLCJzY3AiOiJ1c2VyX2ltcGVyc29uYXRpb24iLCJzdWIiOiJMSndJUERQbFQwT3V2dDdXaEpJX0J5Nzk3eWRjQjhmMEk5MnRMSEM1MmNrIiwidGlkIjoiNzVmMmE5OWItMDFmZC00OGYyLWFjNjAtZDRhN2E0NGZkMGNjIiwidW5pcXVlX25hbWUiOiJpbmlnby5qQHhlbmNpYS5jb20iLCJ1cG4iOiJpbmlnby5qQHhlbmNpYS5jb20iLCJ1dGkiOiJzS29fQTJXeF9rbVJoVjkwbEkyZ0FBIiwidmVyIjoiMS4wIiwid2lkcyI6WyJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXSwieG1zX2NjIjpbIkNQMSJdLCJ4bXNfdGNkdCI6MTMxNzU3MjQwMn0.CloFXvKU_B-NayypefwCPwF5FmetxH4UIxzvJRDi_tT2CU-HWbUmFZYZT4EKoBDE4CQCFJYhJTp1n5REoe9EyBKM-_6y89FMlvlHQ-q0kb_Xl-aniuetyyKeWw4cSNGiRNLgKNJOp-2UWfaXKrUSRqU9w_AgWqXKhOD2noBKxdx2gGmA1yV-CDVLKPUR7xgHFKpsHAprONaEVH2plrModTwduS3c2piFTgXIMHVpPL8JkULFuucCQUPZCu6rTj9msOeX_ck0sbJOLHuK-mDvAzK5D82KWOh4o-ANkOr55prFXYJFDgtwvxASe2MbCn1EpEVQWAwmS3lOVL-ZOd0Caw'



    def vm_sku_api_data_collection():
        header={'Authorization': 'Bearer ' + access_token}
        url = "https://management.azure.com/subscriptions/a8d00da7-ec1e-4764-9ebf-b825b6d5424f/providers/Microsoft.Compute/skus?api-version=2021-07-01"
        response = requests.get(url, headers=header)
        print(response.status_code)
        return response

    response = vm_sku_api_data_collection()
    print(response)
    vm_sku_json = response.json()
    print(response.status_code)

    vm_sku_list=[]
    for row in vm_sku_json['value']:
        if row["resourceType"] == "virtualMachines":
                            for location in row["locations"]:

                                processed_json_data = {
                                    "vm_sku_name": row["name"],
                                    "vm_sku_detail": { k: v for k, v in row.items() if  k != "locations"},
                                    "family" : row["family"],
                                    "location" : location
                                    }
                                for capabilities in row["capabilities"]:
                                    if(capabilities["name"]== "vCPUs"):
                                        processed_json_data["vCPUs"] = capabilities["value"]
                                    if(capabilities["name"]== "MemoryGB"):
                                          processed_json_data["MemoryGB"] = capabilities["value"]


                                vm_sku_list.append(processed_json_data)


    for data in vm_sku_list:
        model_object = vm_sizes()
        model_object.vm_sku_name = data['vm_sku_name']
        model_object.vm_sku_details = data['vm_sku_detail']
        model_object.family = data['family']
        model_object.vCPUs = data['vCPUs']
        model_object.MemoryGB = data['MemoryGB']
        model_object.location = data['location']
        model_object.save() 
