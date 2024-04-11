import logging

from fastapi import APIRouter

from fastapi_service.services.model_loader import get_last_data_with_prediction

logger = logging.getLogger()
router = APIRouter()


@router.post("/predict")
async def predict_item():
    df = get_last_data_with_prediction()
    return df.to_dict()
