from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import AgglomerativeClustering
import newspaper
import feedparser
import spacy
import numpy as np
import time


# sources = [
#     'https://feedx.net/rss/ap.xml',
#     'http://rss.cnn.com/rss/cnn_topstories.rss',
#     'https://feeds.bbci.co.uk/news/rss.xml',
#     'http://rss.cnn.com/rss/cnn_topstories.rss',
#     'https://www.wpbf.com/topstories-rss'
# ]

# sources = [
#     'https://www.wuft.org/news-feed.rss'
# ]

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

articles = []

for source in world_news_feeds:

    print(source)

    d = feedparser.parse(source)

    # model = SentenceTransformer('all-MiniLM-L6-v2')
    for i in range(5):

        if i >= len(d.entries):
            continue

        entry = d.entries[i]

        if 'title' in entry:

            headlines.append(entry.title)

            if 'link' in entry:

                article = newspaper.article(entry.link)
                articles.append(article.text)
        
        # time.sleep(1)
    


model = SentenceTransformer('all-mpnet-base-v2')

embeddings = model.encode(articles)

clustering = AgglomerativeClustering(
    n_clusters=None,
    distance_threshold=0.4,  # tune this
    metric='cosine',
    linkage='average'
)

labels = clustering.fit_predict(embeddings)

print(labels)

# org_clusters = {}

# for label, headline in zip(labels, headlines):

#     if label in org_clusters:

#         org_clusters[label].append(headline)
    
#     else:

#         org_clusters[label] = [headline]


# for item in org_clusters:

#     for headline in org_clusters[item]:

#         print(headline)

#     print("-----------------------------")


# # embeddings = model.encode(articles)

# # similarity = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
# # print(f"Articles 1&2 similarity: {similarity:.3f}")  # will be high
