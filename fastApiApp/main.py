from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):

    id: int
    name: str



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/timelines")
def get_all_timelines():
    timelines = []

    return {"timeline": 2}

@app.get("/timeline/{timeline_id}")
def get_timeline(timeline_id: int):

    return {"timeline_id": timeline_id}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}