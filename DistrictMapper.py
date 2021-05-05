import pickle

def getMapper():
    a=open("/home/diptanshu/Desktop/Cowin/map.pkl","rb")
    mapper=pickle.load(a)
    a.close()
    return mapper
