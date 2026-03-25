import newspaper
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-mpnet-base-v2')

article = newspaper.article('https://www.alligator.org/article/2026/03/gators-prairie-view-first-round')

print(article.authors)
# ['Hannah Brewitt']

print(article.publish_date)
# 2023-10-29 00:00:00

print(article.text)

articles = [article.text]

embeddings = model.encode(articles)

