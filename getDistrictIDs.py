import requests
import json

'''
Edit State ID
'''
StateID=21




url = f"https://cdn-api.co-vin.in/api/v2/admin/location/districts/{StateID}"
payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
if response.status_code==200:
    for i in response.json()["districts"]:
        print(i["district_name"],"\t\t\t",i["district_id"])
else:
    print("Cowin is presenting cloudflare error, please run the file again or try again after some time")
