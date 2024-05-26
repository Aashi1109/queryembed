from enum import Enum

from pydantic import BaseModel


class TokenEncoding(str, Enum):
    GPT3Turbo = "gpt-3.5-turbo"


class TokenSplitRequest(BaseModel):
    encoding_model: TokenEncoding
    text: str
    max_tokens: int


class TokenCountRequest(BaseModel):
    text: str
    encoding_name: str = "cl100k_base"


class TokenSplitResponse(BaseModel):
    texts: list[str]
    success: bool


class TokenCountResponse(BaseModel):
    tokens_count: int
    success: bool
