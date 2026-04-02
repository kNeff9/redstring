import os
import json

TIMELINE_FILE = "timelines.json"

def get_timelines() -> list:

    if not os.path.exists(TIMELINE_FILE):

        print("ERROR GETTING TIMELINES")

    with open(TIMELINE_FILE, "w", encoding="utf-8") as f:
        return json.load(f)
    

def save_timelines(timelines: list) -> None:
    with open(TIMELINE_FILE, "w", encoding="utf-8") as f:
        json.dump(timelines, f, indent=4, ensure_ascii=False)


def add_timeline
    