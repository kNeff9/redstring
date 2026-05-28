from pipeline_functions.article_embedding import *
from pipeline_functions.cluster_summary import *
from news_objects.Story import *
from news_objects.Timeline import *
import os
from database.insert import *

"""

In this file I will be creating the pipeline for getting articles, summarizing them, and adding
them to timelines.

"""
# Array of Story() objects after clusters are summarized. They inherit the ai summary and cluster centroid
stories = []

world_news_feeds = [
    # 1. Associated Press - World News
    'https://apnews.com/apf-topnews',
    
    # 2. BBC World News
    'https://feeds.bbci.co.uk/news/world/rss.xml',
    
    # 3. Reuters World
    'https://www.reutersagency.com/feed/?taxonomy=best-topics&post_type=best',
    
    # 4. Al Jazeera
    'https://www.aljazeera.com/xml/rss/all.xml',
    
    # 5. The Guardian - World News
    'https://www.theguardian.com/world/rss',
    
    # 6. NPR World News
    'https://feeds.npr.org/1004/rss.xml',
    
    # 7. CNN World
    'http://rss.cnn.com/rss/cnn_world.rss',
    
    # 8. Deutsche Welle (German international broadcaster)
    'https://rss.dw.com/xml/rss-en-all',
    
    # 9. France 24 English
    'https://www.france24.com/en/rss',
    
    # 10. ABC News International
    'https://abcnews.go.com/abcnews/internationalheadlines',
]


# temp = fetch_articles(world_news_feeds)[1]

# for item in temp:

#     print(item[:100])
#     print("=========================")
#     print()


# An array of Cluster() objects
article_clusters = get_article_clusters()

popular_stories = []


for cluster in article_clusters:

    if len(cluster.articles) < 2:
        continue

    curr_summary = summarize_articles(cluster.articles)

    newStory = Story(cluster.centroid, curr_summary)

    stories.append(newStory)









