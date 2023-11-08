from typing import Union
from class_file import *
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}



#  CORRECTION ______________________________________________________________________

@app.post("/chat/{room_id}", tags=["message"])
def post_a_message (room_id: str, message: Message):
    return #TO DO

@app.get("/chat/{room_id}", tags=["message"])
def get_a_message (room_id: str)->ChatRoom:
    return None#TO DO

@app.delete("/chatroom/{room_id}", tags=["chatroom"])
def del_chatroom (room_id: str):
    pass#TO DO

@app.delete("/chat/{message_id}", tags=["message"])
def del_message (message_id: str):
    pass #TO DO

@app.post("/chatroom/{room_id}", tags=["chatroom"])
def add_chatroom (chatroom : ChatRoom):
    return #TO DO