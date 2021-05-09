import DistrictMapper
from getListofCenters import getListOfCenters
from getFormattedDate import getDate
from datetime import date
import time
from emailFunctions import sendMail,sendMailEE
import requests
from datetime import datetime
from outputPrettifier import prettyreturnAllAge,prettyreturnByAge
from datetime import timedelta
from Emailresponsefilter import getAgeBasedCenters,getAllCenters
mapper=DistrictMapper.getMapper()
num_weeks=5

print(f"program started at time {datetime.now()}\n--------------------------------------")
for district in mapper:
    today = date.today()
    below45List={email for (email,details) in mapper[district].items() if details['age']==18 and details['age_based']==1}
    above45List={email for (email,details) in mapper[district].items() if details['age']==45 and details['age_based']==1}
    bothList={email for (email,details) in mapper[district].items() if details['age_based']==0}
    below45data={"data":""}
    above45data={"data":""}
    bothdata={"data":""}
    c=0
    for i in range(num_weeks):
        response=getListOfCenters(district,getDate(today))
        if response.status_code==200:
            bothAgeCenters=getAllCenters(response)
            if bothAgeCenters!={}:
                if bothList != set():
                    c+=1
                    data=prettyreturnAllAge(bothAgeCenters)
                    bothdata['data']+=data
                below45AgeCenters=getAgeBasedCenters(response,18)
                above45AgeCenters=getAgeBasedCenters(response,45)
                if below45AgeCenters!={} and below45List!= set():
                    c+=1
                    data=prettyreturnByAge(below45AgeCenters)
                    below45data['data']+=data
                if above45AgeCenters!={} and above45List!= set():
                    c+=1
                    data=prettyreturnByAge(above45AgeCenters)
                    above45data['data']+=data
        else:
            print(f"Error getting data from Cowin {district} at time {datetime.now()}\n")
        today = today+timedelta(weeks=1)
    if(c!=0):
        if bothdata['data']!="":
            sendMailEE(bothList,bothdata['data'])
            print(f"mail sent for bothList at time {datetime.now()} containing {len(bothList)} recipients for district {district}\n")   
        if below45data['data']!="":
            sendMailEE(below45List,below45data['data'])
            print(f"mail sent for below45 at time {datetime.now()} containing {len(below45List)} recipients for district {district}\n")       
        if above45data['data']!="":
            sendMailEE(above45List,above45data["data"])
            print(f"mail sent for above45 at time {datetime.now()} containing {len(above45List)} recipients for district {district}\n")
    else:
        print(f"No data against district ID {district} for next 5 weeks")            

print(f"program ended at time {datetime.now()}")