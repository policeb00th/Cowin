import time
from datetime import timedelta
import filterCenters
import getListofCenters
import outputPrettifier
import getFormattedDate


def getAgeGroup(age):
    if age>=45:
        return 45
    else:
        return 18

def getPaid(select_age_flag,num_weeks,today,district_id,age):
    if select_age_flag == 1:
        print(
            f"\n\n\n----------------------Paid centers for minimum Age {age}------------------------------\n")
        for i in range(num_weeks):  # searching for 3 weeks
            getDateFormatted = getFormattedDate.getDate(today)
            response = getListofCenters.getListOfCenters(
                district_id, getDateFormatted)
            if response.status_code == 200:
                availableDates = filterCenters.getAgeBasedCentersPaid(response, age)
                if availableDates=={}:
                    print(f"\tNone showing from {getDateFormatted} till  {getFormattedDate.getDate(today+timedelta(weeks=1))}\n")            
                else:
                    outputPrettifier.prettyprint(availableDates)
            else:
                print(f"\tError accessing data from Cowin for dates from date {getDateFormatted} till  {getFormattedDate.getDate(today+timedelta(weeks=1))}, try again\n")
            today = today+timedelta(weeks=1)

    else:
        print(f"----------------------Paid-> All ages------------------------------------")
        for i in range(num_weeks):  # searching for 3 weeks
            getDateFormatted = getFormattedDate.getDate(today)
            response = getListofCenters.getListOfCenters(
                district_id, getDateFormatted)
            if response.status_code == 200:
                availableDates = filterCenters.getAllCentersPaid(response, age)
                if availableDates=={}:
                    print(f"\tNone showing from {getDateFormatted} till  {getFormattedDate.getDate(today+timedelta(weeks=1))}\n")            
                else:
                    outputPrettifier.prettyprint(availableDates)
            else:
                print(f"\tError accessing data from Cowin for date{getDateFormatted}, try again\n")
            today = today+timedelta(weeks=1)



def getUnpaid(select_age_flag,num_weeks,today,district_id,age):
    if select_age_flag == 1:
        print(
            f"\n\n\n----------------------Unpaid centers for minimum Age {age}------------------------------\n")
        for i in range(num_weeks):  # searching for 3 weeks
            getDateFormatted = getFormattedDate.getDate(today)
            response = getListofCenters.getListOfCenters(
                district_id, getDateFormatted)
            if response.status_code == 200:
                availableDates = filterCenters.getAgeBasedCentersUnpaid(response, age)
                if availableDates=={}:
                    print(f"\tNone showing from {getDateFormatted} till  {getFormattedDate.getDate(today+timedelta(weeks=1))}\n")            
                else:
                    outputPrettifier.prettyprint(availableDates)
            else:
                print(f"\tError accessing data from Cowin for dates from date {getDateFormatted} till  {getFormattedDate.getDate(today+timedelta(weeks=1))}, try again\n")
            today = today+timedelta(weeks=1)

    else:
        print(f"----------------------Unpaid-> All ages------------------------------------")
        for i in range(num_weeks):  # searching for 3 weeks
            getDateFormatted = getFormattedDate.getDate(today)
            response = getListofCenters.getListOfCenters(
                district_id, getDateFormatted)
            if response.status_code == 200:
                availableDates = filterCenters.getAllCentersUnpaid(response, age)
                if availableDates=={}:
                    print(f"\tNone showing from {getDateFormatted} till  {getFormattedDate.getDate(today+timedelta(weeks=1))}\n")            
                else:
                    outputPrettifier.prettyprint(availableDates)
            else:
                print(f"\tError accessing data from Cowin for date{getDateFormatted}, try again\n")
            today = today+timedelta(weeks=1)
