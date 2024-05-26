from fastapi import APIRouter

from src.logger import logger
from src.tokens.helpers import split_text_into_tokens, num_tokens_from_string
from src.tokens.schemas import TokenSplitRequest, TokenCountRequest, TokenSplitResponse, TokenCountResponse

router = APIRouter()


@router.post("/token_split")
async def token_split(_data: TokenSplitRequest):
    logger.info("Request received" + str(_data.__repr__()))
    texts = split_text_into_tokens(_data.text, _data.max_tokens, _data.encoding_model)
    response = TokenSplitResponse(texts=texts, success=True)
    logger.info("Response sent" + str(response.__repr__()))
    return response


@router.post("/token_count")
async def token_count(_data: TokenCountRequest):
    logger.info("Request received" + str(_data.__repr__()))

    tokens_count = num_tokens_from_string(_data.text, _data.encoding_name)
    response = TokenCountResponse(tokens_count=tokens_count, success=True)
    logger.info("Response sent" + str(response.__repr__()))
    return response
