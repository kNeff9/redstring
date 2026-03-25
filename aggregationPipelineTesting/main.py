import feedparser
import spacy

# nlp = spacy.load("en_core_web_sm")


sources = [
    'https://rss.nytimes.com/services/xml/rss/nyt/World.xml',
    'https://feedx.net/rss/ap.xml',
    'https://feeds.nbcnews.com/nbcnews/public/news'
]

for s in sources:

    d = feedparser.parse(s)

    for entry in d.entries:

        if 'link' in entry:

            print(entry.link)
        
        if 'title' in entry:

            print(entry.title)
        
        
        print("-------------------------")


