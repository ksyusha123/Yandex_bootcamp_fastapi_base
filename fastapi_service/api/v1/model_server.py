import logging

from fastapi import APIRouter

from fastapi_service.services.model_loader import get_last_data_with_prediction, get_latest_news

logger = logging.getLogger()
router = APIRouter()


@router.get("/predict")
async def predict_item(index_name: str = "imoex"):
    df = get_last_data_with_prediction(index_name)
    return df.to_dict()

@router.get("/news")
async def get_news(day : str):
    df = get_latest_news(day)
    return df.to_dict()
