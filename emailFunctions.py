import yagmail
import time
from ElasticEmailClient import ApiClient, Account, Email
from CONSTANTS import CONSTANTS
email,password=CONSTANTS.email.value,CONSTANTS.password.value
yag=yagmail.SMTP(email,password)

def sendMail(adresses,data):
    contents = [data]
    s=time.time()
    yag.send(to=[a for a in adresses],subject='Open Cowin slots!', contents= contents)
    print(time.time()-s)


def sendMailEE(address,data):
    print(Email.Send(subject="Trial",EEfrom="diptanshu@c4projects.tech",sender="diptanshu@c4projects.tech",to=address,bodyText="Trial",bodyHtml=data))