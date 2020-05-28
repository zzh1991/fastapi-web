from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel

import uuid

app = FastAPI()
client = MongoClient('localhost', 27017)
db = client.feedback
feeds = db.feeds

class Item(BaseModel):
    name: str
    description: str = None

@app.post("/feeds")
def post_feed(item : Item):
    feed = item.dict()
    feed['_id'] = str(uuid.uuid4())
    id = feeds.insert_one(feed).inserted_id
    return id

@app.get("/feeds")
def get_feeds():
    list = []
    for feed in feeds.find():
        list.append(feed)
    return list