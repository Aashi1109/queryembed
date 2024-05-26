from enum import Enum

from pydantic import BaseModel


class EmbeddingModel(str, Enum):
    GTELarge = "GTE-Large"
    MiniLML6V2 = "MiniLML6V2"
    TextEmbedding3Large = "text-embedding-3-large"
    TextEmbedding3Small = "text-embedding-3-small"
    TextEmbedding3Ada002 = "text-embedding-ada-002"


class EmbeddingRequest(BaseModel):
    texts: list[str]
    modelname: EmbeddingModel


class EmbeddingResponse(BaseModel):
    embeddings: list[list[float]]
    modelname: EmbeddingModel
    dimensions: int
    success: bool
