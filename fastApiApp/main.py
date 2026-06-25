from fastapi import FastAPI
from database.timelines import *
from database.stories import *

from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    
    timelines_rows = fetch_all_timelines()

    json_timelines = []

    for i in range(len(timelines_rows)):

        row = timelines_rows[i]

        json_timelines.append({
            "number" : i+1,
            "title" : row[1],
            "id" : row[0]
        })

    return json_timelines

    
@app.get("/timelines")
def get_all_timelines():

    timelines_rows = fetch_all_timelines()

    json_timelines = []

    for i in range(len(timelines_rows)):

        row = timelines_rows[i]

        json_timelines.append({
            "number" : i+1,
            "title" : row[1],
            "id" : row[0]
        })

    return json_timelines

@app.get("/timelines/{timeline_id}")
def get_timeline(timeline_id: str):

    json_stories = []

    print(timeline_id)

    stories = fetch_timeline_stories(timeline_id)


    for i in range(len(stories)):

        row = stories[i]

        json_stories.append({
            "num": i+1,
            "id": row[0],
            "content": row[2]
        })

    return json_stories


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}