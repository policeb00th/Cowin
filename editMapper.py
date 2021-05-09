import pickle
import re
import json
import pandas as pd
from datetime import datetime 
from CONSTANTS import CONSTANTS
from ageFiltered import getAgeGroup
regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$' 

def loadData():
    df = pd.read_csv(CONSTANTS.path.value+'/data.csv')
    return df


# Change New
def getValues(df, i):
    district = int(df['district_id'][i])
    email = df['email_id'][i]
    age = int(df['age_type'][i])
    return district, email, age

def addEntryFromCSV(district_id, email_id, age_based):
    if re.search(regex, email_id):
        if age_based == 0:
            age = 0
        else:
            age = getAgeGroup(age_based)
            age_based = 1
        a = open(CONSTANTS.path.value + "/map.pkl", "rb")
        mapper = pickle.load(a)
        a.close()
        if district_id not in mapper:
            mapper[district_id] = {email_id: {"age_based": age_based, "age": age, "paid_necessary": 0}}
        else:
            mapper[district_id][email_id] = {"age_based": age_based, "age": age, "paid_necessary": 0}

        a = open(CONSTANTS.path.value + "/map.pkl", "wb")
        pickle.dump(mapper, a)
        a.close()
        a = open(CONSTANTS.path.value + "/MapperLog.txt", "a")
        a.write(f"\n\nAdded district {district_id}, Email {email_id} with age {age} and aged_based {age_based} at time {datetime.now()}\n\n Current mapper: \n {json.dumps(mapper, indent=1)}")

def addEntryManually():
    district_id=int(input("Enter district ID: "))
    email=input("enter email address: ")
    if (re.search(regex,email)):
        age_based=int(input("enter 0 if you don't want to filter by age, else enter age to filter by: "))
        if(age_based==0):
            age=0
        else:
            age=getAgeGroup(age_based)
            age_based=1
        a=open(CONSTANTS.path.value+"/map.pkl","rb")
        mapper=pickle.load(a)
        a.close()
        if district_id not in mapper:
            mapper[district_id]={email:{"age_based":age_based,"age":age,"paid_necessary":0}} 
        else:
            mapper[district_id][email]={"age_based":age_based,"age":age,"paid_necessary":0}
        
        a=open(CONSTANTS.path.value+"/map.pkl","wb")
        pickle.dump(mapper,a)
        a.close()
        a=open(CONSTANTS.path.value+"/MapperLog.txt","a")
        a.write(f"\n\nAdded district {district_id}, Email {email} with age {age} and aged_based {age_based}\n\n Current mapper: \n {json.dumps(mapper,indent=1)}")


def RenameDistrict():
    district_id=int(input("Enter old district id: "))
    a=open(CONSTANTS.path.value+"/map.pkl","rb")
    mapper=pickle.load(a)
    a.close()
    if district_id not in mapper:
        print("Enter ID not present")
    else:
        new_id=int(input("Enter new id: "))
        temp=mapper[district_id]
        mapper[new_id]=temp
        del mapper[district_id]
        a=open(CONSTANTS.path.value+"/map.pkl","wb")
        pickle.dump(mapper,a)
        a.close()
        a=open(CONSTANTS.path.value+"/MapperLog.txt","a")
        a.write(f"\n\nChanged district ID from {district_id} to {new_id}\n\n Current mapper: \n {json.dumps(mapper,indent=1)}")
        

def DeleteDistrict():
    district_id=int(input("Enter district ID to delete: "))
    a=open(CONSTANTS.path.value+"/map.pkl","rb")
    mapper=pickle.load(a)
    a.close()
    if district_id not in mapper:
        print("Enter ID not present")
    else:
        del mapper[district_id]
        a=open(CONSTANTS.path.value+"/map.pkl","wb")
        pickle.dump(mapper,a)
        a.close()
        a=open(CONSTANTS.path.value+"/MapperLog.txt","a")
        a.write(f"\n\nDeleted district ID: {district_id}\n\n Current mapper: \n {json.dumps(mapper,indent=1)}")

def DeleteEmailByDistrict():
    district_id=int(input("Enter district ID : "))
    a=open(CONSTANTS.path.value+"/map.pkl","rb")
    mapper=pickle.load(a)
    a.close()
    if district_id not in mapper:
        print("Enter ID not present")
    else:
        email=input("Enter email to delete by: ")
        if email in mapper[district_id]:
            del mapper[district_id][email]
            a=open(CONSTANTS.path.value+"/map.pkl","wb")
            pickle.dump(mapper,a)
            a.close()
            a=open(CONSTANTS.path.value+"/MapperLog.txt","a")
            a.write(f"\n\ndeleted email {email} from district id {district_id}\n\n Current mapper: \n {json.dumps(mapper,indent=1)}")
        else:
            print("email not present")

def loopThrough(df):
    for i in range(0, len(df)):
        district, email, age = getValues(df, i)
        # print(district, email, age)
        district = int(district)
        age = int(age)
        addEntryFromCSV(district, email, age)

def AddFromCSV():
    data = loadData()
    loopThrough(data)

def deleteAllEmailOccurences():
    a=open(CONSTANTS.path.value+"/map.pkl","rb")
    mapper=pickle.load(a)
    a.close()
    found=0
    email=input("enter email: ")
    for district in mapper:
        if email in mapper[district]:
            del mapper[district][email]
            a=open(CONSTANTS.path.value+"/map.pkl","wb")
            pickle.dump(mapper,a)
            a.close()
            a=open(CONSTANTS.path.value+"/MapperLog.txt","a")
            a.write(f"\n\ndeleted email {email} from district id {district}\n\n Current mapper: \n {json.dumps(mapper,indent=1)}")
            found=1
        break
    if found==0:
        print("No email found")
    else:
        print("email deleted")
    
# for i in range(0,33):
#     print(f"entry number {i+1}")
#     addEntry()
#  RenameDistrict()
#  DeleteDistrict()
#  DeleteEmailByDistrict()
# addEntry()
AddFromCSV()
# deleteAllEmailOccurences()