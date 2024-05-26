import openai
from fastapi import APIRouter

from src.embedding.constants import model_embedding_dimension_mapping
from src.embedding.llmmodel import gte_model, mini_l6_model
from src.embedding.schemas import EmbeddingRequest, EmbeddingModel, EmbeddingResponse
from src.logger import logger
from src.openai_config import async_client

router = APIRouter()


@router.post("/embedding")
async def get_embedding(_data: EmbeddingRequest) -> EmbeddingResponse:
    """
    Generates embedding based on the model selected
    :param _data: Request body containing list of texts to embed and model name to embed them
    :return: EmbeddingResponse
    """
    try:
        logger.info("Request received" + str(_data.__repr__()))

        model = None
        encodings = []
        model_dimensions = 0

        if _data.modelname == EmbeddingModel.GTELarge:
            model = gte_model
            encodings = model.encode(_data.texts)
            model_dimensions = model.get_sentence_embedding_dimension()
        elif _data.modelname == EmbeddingModel.MiniLML6V2:
            model = mini_l6_model
            encodings = model.encode(_data.texts)
            model_dimensions = model.get_sentence_embedding_dimension()
        else:
            embed_resp = await async_client.embeddings.create(input=_data.texts, model=_data.modelname)
            if embed_resp and embed_resp.data:
                encodings = [x.embedding for x in embed_resp.data]
                model_dimensions = model_embedding_dimension_mapping[_data.modelname]

        response = EmbeddingResponse(embeddings=encodings, modelname=_data.modelname,
                                     dimensions=model_dimensions, success=encodings.any())
        logger.info("Response sent" + str(response.__repr__()))
        return response
    except openai.PermissionDeniedError as ope:
        logger.error(f"Error embedding text: {ope}", exc_info=True)
        return EmbeddingResponse(embeddings=[], modelname=_data.modelname, dimensions=0, success=False)
    except Exception as ex:
        logger.error(f"Error embedding text: {ex}", exc_info=True)
        return EmbeddingResponse(embeddings=[], modelname=_data.modelname, dimensions=0, success=False)
