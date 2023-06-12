import os
import requests
from typing import Dict

def get_availability_zones(subscription_id : str, access_token : str) -> Dict[str, set]:
    """
    Get list of availablity zones
    :parm subscription_id: azure subscription id
    :return: Dict of available zones
    """
    print("Started fetching zone data")
    url : str = f"https://management.azure.com/subscriptions/{subscription_id}/providers/Microsoft.Compute/skus?api-version=2021-07-01"
    data_set = requests.get(url, headers={ 'Authorization': 'Bearer ' + access_token }).json()['value']
    availability_zones : Dict[str, set] = dict()

    for data in data_set:
        if data['resourceType'] == 'virtualMachines':
            if data['locationInfo']:
                location_name = data['locationInfo'][0]['location']
                if location_name in availability_zones:
                    availability_zones[location_name.lower().replace(' ', '')] = sorted(set(availability_zones[location_name]).union(set(data['locationInfo'][0]['zones'])))
                else:
                    availability_zones[location_name.lower().replace(' ', '')] = sorted(data['locationInfo'][0]['zones'])
    return availability_zones


def get_location_display_names(subscription_id : str, access_token : str) -> Dict[str, str]:
    """
    Get list of display names
    :parm subscription_id: azure subscription id
    :return: Dict of display names
    """
    url2 : str = f"https://management.azure.com/subscriptions/{subscription_id}/providers/Microsoft.Web/geoRegions?api-version=2022-03-01"
    location_display_names : Dict[str, str] = dict()

    data_set = requests.get(url2, headers={ 'Authorization': 'Bearer ' + access_token }).json()['value']

    for data in data_set:
        location_display_names[data['properties']['name'].replace(' ', '').lower()] = data['properties']['displayName']
    return location_display_names


def get_access_token():
    """
    Get the Bearer Access token
    :return: String of Access token
    """
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


subscription_id = os.environ.get('SUBSCRIPTION_ID')
access_token = get_access_token() 
availability_zones = get_availability_zones(subscription_id, access_token)
location_display_names = get_location_display_names(subscription_id, access_token)