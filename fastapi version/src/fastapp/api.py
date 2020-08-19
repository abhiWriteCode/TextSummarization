from fastapi import APIRouter
from pydantic import BaseModel
import asyncio

from .model import get_summary


class Data(BaseModel):
    text: str
    max_length: int


router = APIRouter()

@router.get('/')
async def index():
    json_data = {'message': 'Welcome to Text Summarization service'}
    return json_data

@router.post('/summary')
async def index(data: Data):
    summary_text = await get_summary(long_text=data.text, max_length=data.max_length)
    json_data = {"summary_text": summary_text}
    return json_data