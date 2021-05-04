
def getAgeBasedCentersPaid(response,age):
    response=response.json()
    listofCenters=[]
    centers=response["centers"]
    dateCenterdict={}
    for center in centers:
        if center["fee_type"]=="Paid":
            for session in center["sessions"]:
                if session["min_age_limit"]==age and session["available_capacity"]!=0:
                    if session["date"] in dateCenterdict:
                        dateCenterdict[session["date"]].append([center["name"],session["vaccine"],session["available_capacity"]])
                    else:
                        dateCenterdict[session["date"]]=[[center["name"],session["vaccine"],session["available_capacity"]]]
    return(dateCenterdict)

def getAllCentersPaid(response,age):
    response=response.json()
    listofCenters=[]
    centers=response["centers"]
    dateCenterdict={}
    for center in centers:
        if center["fee_type"]=="Paid":
            for session in center["sessions"]:
                if session["available_capacity"]!=0:
                    if session["date"] in dateCenterdict:
                        dateCenterdict[session["date"]].append([center["name"],session["vaccine"],session["available_capacity"]])
                    else:
                        dateCenterdict[session["date"]]=[[center["name"],session["vaccine"],session["available_capacity"]]]
    return(dateCenterdict)

def getAllCentersUnpaid(response,age):
    response=response.json()
    listofCenters=[]
    centers=response["centers"]
    dateCenterdict={}
    for center in centers:
        if center["fee_type"]=="Free":
            for session in center["sessions"]:
                if session["available_capacity"]!=0:
                    if session["date"] in dateCenterdict:
                        dateCenterdict[session["date"]].append([center["name"],session["vaccine"],session["available_capacity"]])
                    else:
                        dateCenterdict[session["date"]]=[[center["name"],session["vaccine"],session["available_capacity"]]]
    return(dateCenterdict)

def getAgeBasedCentersUnpaid(response,age):
    response=response.json()
    listofCenters=[]
    centers=response["centers"]
    dateCenterdict={}
    for center in centers:
        if center["fee_type"]=="Free":
            for session in center["sessions"]:
                if session["min_age_limit"]==age and session["available_capacity"]!=0:
                    if session["date"] in dateCenterdict:
                        dateCenterdict[session["date"]].append([center["name"],session["vaccine"],session["available_capacity"]])
                    else:
                        dateCenterdict[session["date"]]=[[center["name"],session["vaccine"],session["available_capacity"]]]
    return(dateCenterdict)