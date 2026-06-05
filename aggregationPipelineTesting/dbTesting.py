from database.stories import *
from database.timelines import *
from database.similarity_screen import *
from news_objects.Story import *
from news_objects.Timeline import *
import os
import numpy as np
import uuid

# Right now I am removing the db constratint that requires each story's timeline_id to be in timelines

# To add it back, this is the SQL code:

# ALTER TABLE stories ADD CONSTRAINT stories_timeline_id_fkey 
# FOREIGN KEY (timeline_id) REFERENCES timelines(id);

test_centroid = np.random.rand(768)

test_id = uuid.uuid4()

test_timeline = Timeline(test_id, test_centroid, "")

insert_timeline(test_timeline)