import ollama


test_articles = [
    # Article 1: Tech-focused perspective
    """
    TechRadar Express — Silicon Valley giant NexaCore announced its newest hardware milestone today with the unveiling of the 'Aegis-9' AI accelerator chip. Built on a cutting-edge 3nm architecture, NexaCore claims the Aegis-9 delivers a staggering 45% increase in processing efficiency for Large Language Models compared to last year's model. Engineering VP Sarah Jenkins noted during the keynote that the chip features a specialized onboard power-management unit designed specifically to reduce server cooling costs. Pre-orders open next month, with shipping expected to begin in Q4.
    """,
    
    # Article 2: Financial and market perspective
    """
    The Daily Market Report — NexaCore shares surged 6.2% following the official reveal of its highly anticipated Aegis-9 processor. The hardware giant is positioning the new chip as a direct challenge to current market leaders in the enterprise AI space. According to industry analysts, the 3nm chip's promise of a 45% jump in LLM processing efficiency could significantly lower operational overhead for data centers. NexaCore confirmed that major cloud providers have already secured early-access allocation contracts ahead of the Q4 rollout, sparking strong investor confidence.
    """,
    
    # Article 3: General mainstream news perspective
    """
    Global News Network — Technology firm NexaCore has taken the wraps off a powerful new computer chip aimed at accelerating the ongoing artificial intelligence boom. Dubbed the Aegis-9, the processor is engineered to handle massive AI workloads much faster while consuming less energy—a critical factor as tech companies face scrutiny over data center power consumption. NexaCore executives stated during a press event that the hardware boasts a 45% efficiency boost for training and running AI models. The chips are slated to begin shipping to enterprise clients by the end of this year.
    """
]



def summarize_articles(articles):


    prompt = """

    Your job is to summarize a set of news articles in up to 4 sentences. In this summary, you should use AT MOST one quote from the articles,
    and you should not directly copy so as to avoid plagiarism. Just return the summary text, nothing else.

    These are the articles:

    """

    full_content = f"{prompt}\n\n"


    for i, article_text in enumerate(articles):
        full_content += f"--- Article {i+1} ---\n"
        full_content += f"{article_text.strip()}\n\n"
    
    try:

        response = ollama.chat(
            model= 'qwen3:8b',
            messages=[
                {'role': 'user', 'content': full_content}
            ],
            
            options={
                'temperature': 0.2,
            }
        )

        print("Summary of articles:")
        print(response['message']['content'])
        print("-----------------------")

    except Exception as e:
        print(f"An error occured: {e}")


if __name__ == "__main__":

    summarize_articles(test_articles)