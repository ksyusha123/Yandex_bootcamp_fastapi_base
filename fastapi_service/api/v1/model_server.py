import logging

from fastapi import APIRouter

from fastapi_service.services.model_loader import get_last_data_with_prediction

logger = logging.getLogger()
router = APIRouter()


@router.get("/predict")
async def predict_item(index_name: str = "imoex"):
    df = get_last_data_with_prediction(index_name)
    return df.to_dict()

@router.get("/news")
async def predict_item(day : str):
    df = get_last_data_with_prediction(day)
    return df.to_dict()
