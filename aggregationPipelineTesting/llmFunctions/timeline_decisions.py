from dotenv import load_dotenv
import os
import anthropic
from news_objects import *

load_dotenv()

claude_key = os.getenv("ANTHROPIC_API_KEY")

client = anthropic.Anthropic()


def determine_timeline_fit(recent_stories: list[str], new_story: str):
    prompt = """You are a news timeline classifier. Your job is to determine whether a new story belongs in an existing timeline of related news stories.

A story belongs in a timeline if it:
- Involves the same core event, situation, or developing story
- Features the same key people, organizations, or locations as the central subject
- Represents a continuation, update, or direct consequence of the existing stories

A story does NOT belong if it:
- Merely shares a topic or theme but is a separate, unrelated event
- Involves similar subjects in a completely different context or incident
- Is only tangentially related through background context

Respond with ONLY a single word: YES or NO."""

    timeline_context = "\n\n".join(
        [f"[Story {i+1}]: {story}" for i, story in enumerate(recent_stories)]
    )

    user_content = f"""EXISTING TIMELINE STORIES:
{timeline_context}

NEW STORY TO EVALUATE:
{new_story}

Does the new story belong in this timeline?"""

    message = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=10,
        system=prompt,
        messages=[
            {
                "role": "user",
                "content": user_content
            }
        ],
    )

    return message.content[0].text.strip().upper() == "YES"