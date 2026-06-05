from dotenv import load_dotenv
import os
import anthropic
from news_objects import *

load_dotenv()

claude_key = os.getenv("ANTHROPIC_API_KEY")

client = anthropic.Anthropic()


# Summarizes a set of articles on the same event
def summarize_articles(articles):

    prompt = """

    Your job is to summarize a set of news articles in up to 4 sentences. In this summary, you should use AT MOST one quote from the articles,
    and you should not directly copy so as to avoid plagiarism. Just return the summary text, nothing else.

    These are the articles:

    """

    article_context = []

    article_context.append({
        "type" : "text",
        "text": prompt
    })

    for i in range(len(articles)):

        article_context.append(

            
            {
                "type": "document",
                "source": {"type": "text", "media_type": "text/plain", "data": articles[i]},
                "title": f'Article {i+1}'
            }
        )

    
    
    message = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": article_context
            }
        ],
    )


    return message.content[0].text

# Generates a title for the timeline given the first story
def generate_title(story):

    prompt = """
    You are an experienced Journalist and headline writer who is trying to prepare a news timeline that could
    possibly brew from a story. The given story will be the first in the timeline of events, and your job it to generate a short
    headline for the timeline based off of the given story. The headline should not be too long, no more than 8 words.

    You should only output the headline as text output. 
    """

    message = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=1000,
        system = prompt,
        messages=[
            {
                "role": "user",
                "content": story.text
            }
        ],
    )

    return message.content[0].text


