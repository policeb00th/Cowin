import yagmail
from getPassword import getpwd
import time
yag=yagmail.SMTP('sinha.diptanshu10@gmail.com',getpwd())

def sendMail(adresses,data):
    contents = [data]
    s=time.time()
    yag.send(to=[a for a in adresses],subject='Open Cowin slots!', contents= contents)
    print(time.time()-s)