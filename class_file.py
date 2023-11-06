from datetime import datetime
from time import strftime

class Message():
    def __init__(self,autor,message):
        self.autor = autor
        self.message= message
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

mess = Message("MAelle","test")
print(mess.autor)
