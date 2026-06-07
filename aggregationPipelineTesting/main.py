from pipeline_functions.article_embedding import *
from pipeline_functions.cluster_summary import *
from news_objects.Story import *
from news_objects.Timeline import *
from database.similarity_screen import *
from database.timelines import *
from database.stories import *
import os

"""

In this file I will be creating the pipeline for getting articles, summarizing them, and adding
them to timelines.

"""
# Array of Story() objects after clusters are summarized. They inherit the ai summary and cluster centroid
stories = []

# An array of Cluster() objects
article_clusters = get_article_clusters(fetch_articles()[1])

popular_stories = []


for cluster in article_clusters:

    if len(cluster.articles) < 2:
        continue

    curr_summary = summarize_articles(cluster.articles)

    print(len(cluster.articles))
    print(curr_summary)
    print("======================================")

    newStory = Story(cluster.centroid, curr_summary)

    stories.append(newStory)


for s in stories:

    timeline_candidates = get_timeline_candidates(s)

    if len(timeline_candidates) < 1:

        # If the story has no timelines it fits into, a new one is created

        timeline_title = generate_title(s)

        print("New timeline created: ", timeline_title)
        print("")

        new_timeline = Timeline(s.timeline_id, s.centroid, timeline_title)

        insert_timeline(new_timeline)

        insert_story(s)

        continue

    for row in timeline_candidates:

        candidate_id = row[0]

        s.timeline_id = candidate_id

        insert_story(s)

        break

    











