import openai
from fastapi import APIRouter, HTTPException
from starlette.responses import StreamingResponse

from src.openai_config import async_client
from src.query.helpers import stream_generator
from src.query.schemas import InferenceRequest, InferenceResponse

router = APIRouter()


@router.post(f"/query", status_code=200)
async def openai_streaming(request: InferenceRequest):
    try:
        do_stream_response = request.streaming_response

        subscription = await async_client.chat.completions.create(
            model=request.modelname,
            messages=request.input_text,
            stream=do_stream_response,
        )

        if do_stream_response:
            return StreamingResponse(stream_generator(subscription),
                                     media_type='text/event-stream')
        else:
            return InferenceResponse(response=subscription.choices[0].message.content, model_name=request.modelname,
                                     success=True)
    except openai.OpenAIError:
        raise HTTPException(status_code=500, detail='OpenAI call failed')
