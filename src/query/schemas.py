from enum import Enum
from typing import Optional, List, Union, Literal

from pydantic import BaseModel


class InferenceModel(str, Enum):
    GPT3Turbo = "gpt-3.5-turbo"


class InferenceTextInput(BaseModel):
    role: Union[Literal["system"], Literal["user"], Literal["assistant"]]
    content: str


class InferenceRequest(BaseModel):
    modelname: InferenceModel
    input_text: List[InferenceTextInput]
    api_key: Optional[str] = None
    streaming_response: Optional[bool] = False


class InferenceResponse(BaseModel):
    modelname: str
    response: str
    success: bool
