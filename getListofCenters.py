import requests
def getListOfCenters(district_id,today):
    url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={district_id}&date={today}"
    payload={}
    headers = {
      'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
      'Accept': 'application/json, text/plain, */*',
      'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
      'If-None-Match': 'W/"dee4-NC3UJeJ92GNh/n8HD9Ag9/h/oOA"',
      'Origin': 'https://www.cowin.gov.in',
      'Referer': 'https://www.cowin.gov.in',
      'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'cross-site'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response
