"""Configuration for the LLM Council."""

import os
from dotenv import load_dotenv

load_dotenv()

# OpenRouter API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# OpenRouter API endpoint
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# OpenRouter API key
NEBIUS_API_KEY = os.getenv("NEBIUS_API_KEY")

# OpenRouter API endpoint
NEBIUS_API_URL = "https://api.tokenfactory.nebius.com/v1/chat/completions"



# Council members - list of OpenRouter model identifiers
# COUNCIL_MODELS = [
#     "openai/gpt-5.1",
#     "google/gemini-3-pro-preview",
#     "anthropic/claude-sonnet-4.5",
#     "x-ai/grok-4",
# ]

COUNCIL_MODELS = [
    {
        "id": "openai-gpt-5.1",
        "provider": "openrouter",
        "model":"openai/gpt-5.1"
    },
    {
        "id": "google-gemini-3-pro-preview",
        "provider": "openrouter",
        "model":"google/gemini-3-pro-preview"
    },
    {
        "id": "anthropic-claude-sonnet-4.5",
        "provider": "openrouter",
        "model":"anthropic/claude-sonnet-4.5"
    },
    {
        "id": "x-ai-grok-4",
        "provider": "openrouter",
        "model":"x-ai/grok-4"
    },
    {
        "id": "gpt-oss:20b",
        "provider": "nebius",
        "model": "openai/openai/gpt-oss:20b",
    }
]

# Chairman model - synthesizes final response
# CHAIRMAN_MODEL = "google/gemini-3-pro-preview"

CHAIRMAN_MODEL = {
        "id": "gpt-oss:20b",
        "provider": "nebius",
        "model":"google/gemini-3-pro-preview"
    }

# Data directory for conversation storage
DATA_DIR = "data/conversations"
