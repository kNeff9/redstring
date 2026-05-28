from pipeline_functions.article_embedding import *
from pipeline_functions.cluster_summary import *
from news_objects.Story import *
from news_objects.Timeline import *
import os
from jsonTesting.timeline_sorting import *
import newspaper


chrono_urls = get_chrono_urls()


article_clusters = {}

articles = []
titles = []

for date in chrono_urls:

    res = fetch_articles(chrono_urls[date])
    print(res)
    articles = res[1]
    titles = res[0]


article_clusters = get_test_clusters(articles, titles)

for cluster in article_clusters:

    print("Titles of stories in this cluster:")
    print(cluster.titles)
    print("----------------")