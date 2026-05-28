from dotenv import load_dotenv
import os
import anthropic
from news_objects import *

load_dotenv()

claude_key = os.getenv("ANTHROPIC_API_KEY")

client = anthropic.Anthropic()


# Uses ai to 
def summarize_articles(articles):

    prompt = """

    Your job is to summarize a set of news articles in up to 4 sentences. In this summary, you should use AT MOST one quote from the articles,
    and you should not directly copy so as to avoid plagiarism. Just return the summary text, nothing else.

    These are the articles:

    """

    article_context = []

    for i in range(len(articles)):

        article_context.append(

            
            {
                "type": "document",
                "source": {"type": "text", "media_type": "text/plain", "data": articles[i]},
                "title": f'Article {i+1}'
            }
        )

    article_context.append({
        "type" : "text",
        "text": prompt
    })
    


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


# articles = [
#     """Scientists at MIT have announced a major breakthrough in solar panel efficiency, achieving a record 47% energy conversion rate in laboratory conditions. The new technology uses a multi-layered perovskite cell design that captures a broader spectrum of sunlight than traditional silicon panels. Researchers say the panels could be commercially available within five years. The team received $50 million in federal funding to accelerate development. If scaled, the technology could cut solar energy costs by up to 60%.""",

#     """A research team from Stanford University has developed a next-generation solar cell that converts nearly half of incoming sunlight into electricity, shattering previous efficiency records. The cells use an experimental perovskite-silicon tandem structure and were tested under controlled lab conditions. Industry analysts say the breakthrough could reshape the renewable energy market. However, some experts caution that translating lab results to mass production remains a significant hurdle. The Department of Energy called it the most important solar advancement in a decade.""",

#     """The renewable energy sector is buzzing after two separate American universities announced competing solar efficiency milestones this week. Both MIT and Stanford claim to have achieved efficiency rates above 45% using perovskite-based solar cells, far exceeding the current commercial standard of around 22%. Critics have questioned whether the results can be replicated outside laboratory settings. Environmental groups praised the developments, saying cheaper solar could accelerate the global transition away from fossil fuels. Stock prices for several solar manufacturers rose sharply following the announcements.""",
# ]
