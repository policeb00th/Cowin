import pickle
from CONSTANTS import CONSTANTS

def getMapper():
    a=open(CONSTANTS.path.value+"/map.pkl","rb")
    mapper=pickle.load(a)
    a.close()
    return mapper
