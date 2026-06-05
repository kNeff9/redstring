from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import AgglomerativeClustering
import newspaper
import feedparser
import spacy
import numpy as np
import time

class Cluster:

    def __init__(self):
        
        # Array of real article texts
        self.articles = []

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

headlines = []


def fetch_articles():

    article_links = world_news_feeds

    titles = []
    articles = []

    for source in article_links:

        d = feedparser.parse(source)

        # model = SentenceTransformer('all-MiniLM-L6-v2')
        for i in range(5):

            if i >= len(d.entries):
                continue

            entry = d.entries[i]

            if 'title' in entry:

                if 'link' in entry:

                    try: 
                        article = newspaper.article(entry.link)
                        titles.append(article.title)
                        articles.append(article.text)
                    except:
                        continue
    
    return (titles, articles)


def get_article_clusters(articles):

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

    for label, article, embedding in zip(labels, articles, embeddings):

        if label not in article_clusters:

            article_clusters[label] = Cluster()

        article_clusters[label].add_article(article)
        article_clusters[label].add_embedding(embedding)

    
    final_cluster_array = [] # This is a list of Cluster objects that will be returned (for clarity)

    for label in article_clusters:

        article_clusters[label].compute_centroid()
        final_cluster_array.append(article_clusters[label])
    
    return final_cluster_array

    
    

