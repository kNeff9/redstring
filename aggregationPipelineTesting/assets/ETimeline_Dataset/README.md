# ETimeline
This dataset provides complete data including 600 timelines and a news pool containing over 120,000 candidates.

## Format
The dataset is provided in `json` format.


### timeline example
```json
    {
        "topic_index": "165",                                                      # timeline's index
        "language": "en",                                                          # timeline's language
        "topic": "Kobayashi Pharmaceutical health product fatal incident",         # timeline's topic
        "length": 40,                                                              # timeline's length
        "domain": "Society",                                                       # timeline's news domain
        "node_list": [                                                             # timeline's node list
            {
                "node_index": "165-1",                                             # node index
                "title": "Osaka drugmaker recalls dietary supplements linked to kidney disorders",    # node title
                "date": "2024-03-24",                                                                 # node date
                "url": "https://www.japantimes.co.jp/news/2024/03/24/japan/science-health/kobayashi-pharmaceutical-recalls-supplements/"
            },
            {
                "node_index": "165-2",
                "title": "26 hospitalized after taking Japan drugmaker's health supplements",
                "date": "2024-03-25",
                "url": "https://english.kyodonews.net/news/2024/03/858c8ddf5f8d-26-hospitalized-after-taking-japan-drugmakers-health-supplements.html"
            },
            ...
            {
                "node_index": "165-40",
                "title": "The death toll has increased to 4! Kobayashi Pharmaceutical crisis ...",
                "date": "2024-04-13",
                "url": "https://inf.news/en/news/0326e6798d91676a597f041e323d62b3.html"
            }
        ]
    },
 
```


### news pool example
```json
    {
        "title": "Putin Quietly Signals He Is Open to a Cease-Fire in Ukraine",
        "date": "2023-12-23",
        "url": "https://www.nytimes.com/2023/12/23/world/europe/putin-russia-ukraine-war-cease-fire.html",
        "language": "en"
    },
 
```