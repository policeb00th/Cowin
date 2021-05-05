import yagmail
from getPassword import getpwd
import time
email,password=getpwd()
yag=yagmail.SMTP(email,password)

def sendMail(adresses,data):
    contents = [data]
    s=time.time()
    yag.send(to=[a for a in adresses],subject='Open Cowin slots!', contents= contents)
    print(time.time()-s)