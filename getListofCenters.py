import requests
def getListOfCenters(district_id,today):
    url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id={district_id}&date={today}"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response
