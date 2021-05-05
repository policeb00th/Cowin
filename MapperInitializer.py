import pickle
import json
from CONSTANTS import CONSTANTS
a=open(CONSTANTS.path.value+"/map.pkl",'ab')
mapper = {
    149:{
        'sinha.diptanshu10@gmail.com':{
            'age_based':0,
            'age':18,
            'paid_necessary':0
            
        },
        'sinha.diptanshu@hotmail.com':{
            'age_based':1,
            'age':45,
            'paid_necessary':0
            
        },
        'sinha.diptanshu.vit@gmail.com':{
            'age_based':1,
            'paid_necessary':0,
            'age':21
            
        }
    }
}
pickle.dump(mapper,a)
a.close()
a=open(CONSTANTS.path.value+"/map.pkl",'rb')
print(pickle.load(a))
a.close()
a=open(CONSTANTS.path.value+"/MapperLog.txt","a")
a.write(f"Initizalized mapper \n\n Current mapper: \n {json.dumps(mapper,indent=1)}")