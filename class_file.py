from datetime import datetime
from time import strftime
from pydantic import BaseModel

class Message(BaseModel):
    def __init__(self,autor,message):
        self.autor = autor
        self.message= message
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

'''mess = Message("MAelle","test")
print(mess.autor)'''

class ChatRoom(BaseModel):
    def __init__(self):
        self.historique = []
    def send(self,message):
        self.historique.append(message)

class serveur (BaseModel):
    def __init__(self):
        self.discutions = {}

    def add(self,name):
        id = len(self.discutions)
        self.discutions[id]=name