from dotenv import load_dotenv
import os
import anthropic
from news_objects import *

load_dotenv()

claude_key = os.getenv("ANTHROPIC_API_KEY")

client = anthropic.Anthropic()