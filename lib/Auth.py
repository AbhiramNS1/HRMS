from genericpath import exists
import json,threading
from urllib import parse,request

WEBSITE_LINK='https://cakehouse.co.in/hr-management/apis/main.php'

# from cryptography.fernet import Fernet

# def encrypt(message: bytes, key: bytes):
#     return Fernet(key).encrypt(message)

# def decrypt(token: bytes, key: bytes):
#     return Fernet(key).decrypt(token)

def fetch(link):
    with request.urlopen(link) as url:
        if url:=url.read().decode():
            return json.loads(url)

def post(link,data:dict)->dict:
    return fetch(request.Request(link,data=parse.urlencode(data).encode()))


def setNewToken(token):
    with open('.techtok4u','w') as file:
        file.write(token)
def getToken()->str:
    if(exists('.techtok4u')):
        with open('.techtok4u','r') as file:
            return file.read()

def AuthenticateUser(username,password,callback=None):
    def get():
        try:
            data=post(WEBSITE_LINK,{'username':username,'password':password})
            sucess='status' in data.keys() and data['status']
            if(sucess):
                setNewToken(data['token'])
                if(callback):callback(sucess)
        except:
            print('--implement the new thread access to tlc widndow')
    threading.Thread(target=get).start()
def MarkAttendence(token):
    return post(WEBSITE_LINK,{'mark_attendence':1,'token':token})
   