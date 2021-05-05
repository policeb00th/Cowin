import pickle
import json
a=open("map.pkl",'ab')
mapper = {
    149:{
        'sinha.diptanshu10@gmail.com':{
            'age_based':1,
            'age':18,
            'paid_necessary':0
            
        },
        'sinha.diptanshu@hotmail.com':{
            'age_based':1,
            'age':45,
            'paid_necessary':0
            
        },
        'sinha.diptanshu.vit@gmail.com':{
            'age_based':0,
            'paid_necessary':0,
            'age':21
            
        }
    }
}
pickle.dump(mapper,a)
a.close()
a=open("/home/diptanshu/Desktop/Cowin/map.pkl",'rb')
print(pickle.load(a))
a.close()
a=open("/home/diptanshu/Desktop/Cowin/MapperLog.txt","a")
a.write(f"Initizalized mapper \n\n Current mapper: \n {json.dumps(mapper,indent=1)}")