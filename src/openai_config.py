from openai import OpenAI, AsyncOpenAI

from config import OPENAPI_KEY

client = OpenAI(api_key=OPENAPI_KEY)
async_client = AsyncOpenAI(api_key=OPENAPI_KEY)
