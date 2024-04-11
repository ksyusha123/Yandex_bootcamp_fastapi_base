import logging
import os
from abc import ABC
from typing import Any
import io
import os

import boto3
import pandas as pd


from fastapi_service.settings.settings import settings, Settings


logger = logging.getLogger(__name__)

s3 = boto3.client(service_name="s3", 
    aws_access_key_id=os.environ["S3_ACCESS_KEY_ID"],
    aws_secret_access_key=os.environ["S3_SECRET_ACCESS_KEY"],
    region_name=os.environ["S3_DEFAULT_REGION"],
    endpoint_url="https://storage.yandexcloud.net")


class AbstractLoader(ABC):

    def get(self, conf: Settings) -> Any:
        """Get entity if possible
        """

        raise NotImplemented


class S3Loader(AbstractLoader):
    def get(self, conf: Settings) -> bytes:
        response = s3.get_object(Bucket=conf.s3.bucket, Key=conf.s3.last_data_with_prediction_name)
        model_bytes = response['Body'].read()
        return model_bytes


def get_last_data_with_prediction() -> pd.DataFrame:
    csv = S3Loader().get(settings).decode('utf-8')
    return pd.read_csv(io.StringIO(csv))
