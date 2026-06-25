from database.stories import *
from database.timelines import *
from database.similarity_screen import *
from database.urls import *
from news_objects.Story import *
from news_objects.Timeline import *
import os
import numpy as np
import uuid

# Right now I am removing the db constratint that requires each story's timeline_id to be in timelines

# To add it back, this is the SQL code:

# ALTER TABLE stories ADD CONSTRAINT stories_timeline_id_fkey 
# FOREIGN KEY (timeline_id) REFERENCES timelines(id);

timeline_id = '16e50ec7-ed43-47e9-ba0f-e7cde627ad33'

res = latest_timeline_stories(timeline_id)

for item in res:

    print(item[2])
    print()