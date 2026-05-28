import os
import json
import newspaper
import feedparser
from pipeline_functions.article_embedding import fetch_articles, Cluster
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import AgglomerativeClustering
from sentence_transformers import SentenceTransformer
import newspaper
import feedparser
import spacy
import numpy as np
import time
from pathlib import Path

class JsonCluster:

    def __init__(self):
        
        # Array of real article texts
        self.articles = []

        self.titles = []

        # The embedding score, computed from list of embeddings via compute_centroid()
        self.centroid = None

        # Stores embedding val of each article to later get the average
        self.embedding_vectors = []

        self.title = None
    
    def add_article(self, article):

        self.articles.append(article)

    def add_embedding(self, val):

        self.embedding_vectors.append(val)

    def compute_centroid(self):

        self.centroid = np.mean(self.embedding_vectors, axis=0)


def get_test_clusters(articles, titles):

    # This will create Cluster objects for the training articles so I don't have to use ai summary

    model = SentenceTransformer('all-mpnet-base-v2')

    embeddings = model.encode(articles)

    clustering = AgglomerativeClustering(
        n_clusters=None,
        distance_threshold=0.4,  # tune this
        metric='cosine',
        linkage='average'
    )

    labels = clustering.fit_predict(embeddings)

    article_clusters = {} # This is a dictionary for clustering articles based on their label (same label means similar articles)

    for label, article, embedding, title in zip(labels, articles, embeddings, titles):

        if label not in article_clusters:

            article_clusters[label] = JsonCluster()

        article_clusters[label].titles.append(title)
        article_clusters[label].add_article(article)
        article_clusters[label].add_embedding(embedding)
    
    return article_clusters


# Creating dict that contains date as a key and a list of article urls from that date as the contained value

def get_chrono_urls() -> dict:

    base_dir = Path(__file__).resolve().parent

    STORIES_FILE = base_dir / "test_stories.json"
    TIMELINE_FILE = "timelines.json"


    with open(STORIES_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    chrono_urls = {}

    for i in range(1):

        story_js = data[i]

        if story_js["date"] not in chrono_urls:

            chrono_urls[story_js["date"]] = []

        chrono_urls[story_js["date"]].append(story_js["url"])

    return chrono_urls

