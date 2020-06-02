from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import uuid

app = FastAPI()
client = MongoClient('localhost', 27017)
db = client.feedback
feeds = db.feeds

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    version: str
    type: str
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