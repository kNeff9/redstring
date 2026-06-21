from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import AgglomerativeClustering
from database.urls import *
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


# world_news_feeds = [
#     # 1. Associated Press - World News
#     'https://apnews.com/apf-topnews',
    
#     # 2. BBC World News
#     'https://feeds.bbci.co.uk/news/world/rss.xml',
    
#     # 3. Reuters World
#     'https://www.reutersagency.com/feed/?taxonomy=best-topics&post_type=best',
    
#     # 4. Al Jazeera
#     'https://www.aljazeera.com/xml/rss/all.xml',
    
#     # 5. The Guardian - World News
#     'https://www.theguardian.com/world/rss',
    
#     # 6. NPR World News
#     'https://feeds.npr.org/1004/rss.xml',
    
#     # 7. CNN World
#     'http://rss.cnn.com/rss/cnn_world.rss',
    
#     # 8. Deutsche Welle (German international broadcaster)
#     'https://rss.dw.com/xml/rss-en-all',
    
#     # 9. France 24 English
#     'https://www.france24.com/en/rss',
    
#     # 10. ABC News International
#     'https://abcnews.go.com/abcnews/internationalheadlines',
# ]


world_news_feeds = [
    # ── EXISTING (kept as-is) ──────────────────────────────────────────────

    # 1. Associated Press - World News
    'https://apnews.com/apf-topnews',

    # 2. BBC World News
    'https://feeds.bbci.co.uk/news/world/rss.xml',

    # 3. Reuters (via Google News proxy — direct RSS was dropped in 2020)
    'https://news.google.com/rss/search?q=when:24h+allinurl:reuters.com&ceid=US:en&hl=en-US&gl=US',

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


    # ── NEW ADDITIONS ──────────────────────────────────────────────────────

    # 11. New York Times - World
    'https://rss.nytimes.com/services/xml/rss/nyt/World.xml',

    # 12. Washington Post - World
    'https://feeds.washingtonpost.com/rss/world',

    # 13. Sky News - World
    'https://feeds.skynews.com/feeds/rss/world.xml',

    # 14. UPI - World News (wire service, very clean feed)
    'https://rss.upi.com/news/tn_int.rss',

    # 15. RFI (Radio France Internationale) - English
    'https://rfi.fr/en/international/rss',

    # 16. CNBC - World News
    'https://www.cnbc.com/id/100003114/device/rss/rss.html',

    # 17. CBS News - Main Feed
    'https://cbsnews.com/feeds/rss/main.rss',

    # 18. NBC News - Top Stories
    'https://feeds.nbcnews.com/feeds/topstories',

    # 19. Yahoo News - World
    'https://news.yahoo.com/rss/world',

    # 20. Times of India - World News
    'https://timesofindia.indiatimes.com/rssfeeds/296589292.cms',

    # 21. Politico - Top Stories
    'https://www.politico.com/rss/politicopicks.xml',

    # 22. CNN World (alternate stable endpoint)
    'http://rss.cnn.com/rss/edition_world.rss',

    # 23. NPR News (top stories, broader than feed #6)
    'https://feeds.npr.org/1001/rss.xml',

    # 24. USA Today - Top Stories
    'https://rssfeeds.usatoday.com/usatoday-newstopstories',

    # 25. UPI - Top News (broader companion to feed #14)
    'https://rss.upi.com/news/top_news.rss',
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

                    seen_url = already_seen(entry.link) # Checking if link is in db seen_urls table already

                    if seen_url:
                        print("Already Seen Url. Moving on.")
                        continue

                    try: 
                        article = newspaper.article(entry.link)
                        titles.append(article.title)
                        articles.append(article.text)
                        insert_url(entry.link) # Adding new url to db seen_urls table
                    except:
                        continue
    
    return (titles, articles)


def get_article_clusters(articles):

    model = SentenceTransformer('all-mpnet-base-v2')

    embeddings = model.encode(articles)

    clustering = AgglomerativeClustering(
        n_clusters=None,
        distance_threshold=0.3,  # tune this
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

    
    

