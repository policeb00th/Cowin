import requests
import json
import time
from datetime import date
from datetime import timedelta
import filterCenters
import getListofCenters
import getFormattedDate


today = date.today()
num_weeks = 5        # number of weeks to search through for
district_id = 188    # district id of gurgaon-188, south delhi-149,SE Del-144. SW-Del-150
select_age_flag = 1             # 0 for age based search,1 to search and retu for both ages.
age= 18              # 18 returns centers with available vaccines for 18-44 year olds, 45 returns centers with available vaccines for 45+ year olds
if select_age_flag == 1:

    print(
        f"----------------------Paid-> Age {age}------------------------------------")
    for i in range(num_weeks):  # searching for 3 weeks
        getDateFormatted = getFormattedDate.getDate(today)
        response = getListofCenters.getListOfCenters(
            district_id, getDateFormatted)
        if response.status_code == 200:
            availableDates = filterCenters.getAgeBasedCentersPaid(response, age)
            print(availableDates)
        else:
            print(
                f"Error accessing data from Cowin for date{getDateFormatted}, try again")
        today = today+timedelta(weeks=1)

else:
    print(f"----------------------Paid-> All ages------------------------------------")
    for i in range(num_weeks):  # searching for 3 weeks
        getDateFormatted = getFormattedDate.getDate(today)
        response = getListofCenters.getListOfCenters(
            district_id, getDateFormatted)
        if response.status_code == 200:
            availableDates = filterCenters.getAllCentersPaid(response, age)
            print(availableDates)
        else:
            print(
                f"Error accessing data from Cowin for date{getDateFormatted}, try again")
        today = today+timedelta(weeks=1)
