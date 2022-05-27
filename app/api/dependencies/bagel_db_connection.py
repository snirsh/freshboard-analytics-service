from BagelDBWrapper import BagelDBWrapper
from fastapi import Depends

from app.core.config import get_app_settings
from app.core.settings.app import AppSettings


def get_bagel_wrapper_connection(settings: AppSettings = Depends(get_app_settings)) -> BagelDBWrapper:
    return BagelDBWrapper(api_token=settings.api_token.get_secret_value(), enable_tqdm=True)
