import os
from dotenv import load_dotenv
load_dotenv()
# Any remote API (OpenAI, Cohere etc.)
OPENAI_TIMEOUT = float(os.getenv("REMOTE_API_TIMEOUT_SEC", 30))
OPENAI_BACKOFF = float(os.getenv("REMOTE_API_BACKOFF_SEC", 10))
OPENAI_MAX_RETRIES = int(os.getenv("REMOTE_API_MAX_RETRIES", 5))
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Cloud data store (Redis, Pinecone etc.)
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = str(os.getenv("REDIS_PORT"))
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")


REMOTE_API_TIMEOUT_SEC=30
REMOTE_API_BACKOFF_SEC=10
REMOTE_API_MAX_RETRIES=5
OPENAI_API_KEY='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'

# Cloud data store (Redis, Pinecone etc.)
REDIS_HOST='redis-19780.c17.us-east-1-4.ec2.cloud.redislabs.com'
REDIS_PORT=19780
REDIS_PASSWORD='OPGGvjAIygYGqK9e8IqxvQQYZQoe1hXl'
