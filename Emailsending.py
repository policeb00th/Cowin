import DistrictMapper
from getListofCenters import getListOfCenters
from getFormattedDate import getDate
from datetime import date
from emailFunctions import sendMail
import requests
from datetime import datetime
from outputPrettifier import prettyreturnAllAge,prettyreturnByAge
from Emailresponsefilter import getAgeBasedCenters,getAllCenters
mapper=DistrictMapper.getMapper()
today = date.today()
num_weeks=5

for district in mapper:
    below45List={email for (email,details) in mapper[district].items() if details['age']==18 and details['age_based']==1}
    above45List={email for (email,details) in mapper[district].items() if details['age']==45 and details['age_based']==1}
    bothList={email for (email,details) in mapper[district].items() if details['age_based']==0}
    below45data={"data":""}
    above45data={"data":""}
    bothdata={"data":""}
    for i in range(num_weeks):
        response=getListOfCenters(district,getDate(today))
        if response.status_code==200:
            bothAgeCenters=getAllCenters(response)
            if bothAgeCenters!={}:
                data=prettyreturnAllAge(bothAgeCenters)
                bothdata['data']+=data
                below45AgeCenters=getAgeBasedCenters(response,18)
                above45AgeCenters=getAgeBasedCenters(response,45)
                if below45AgeCenters!={}:
                    data=prettyreturnByAge(below45AgeCenters)
                    below45data['data']+=data
                if above45AgeCenters!={}:
                    data=prettyreturnByAge(above45AgeCenters)
                    above45data['data']+=data
        else:
            print(f"Error getting data from Cowin {district} at time {datetime.now()}\n")
    if bothdata['data']!="":
        sendMail(bothList,bothdata['data'])
        print(f"mail sent for bothList at time {datetime.now()} containing {len(bothList)} recipients for district {district}\n")   
    if below45data['data']!="":
        sendMail(below45List,below45data['data'])
        print(f"mail sent for below45 at time {datetime.now()} containing {len(below45List)} recipients for district {district}\n")       
    if above45data['data']!="":
        sendMail(above45List,above45data["data"])
        print(f"mail sent for above45 at time {datetime.now()} containing {len(above45List)} recipients for district {district}\n")               
