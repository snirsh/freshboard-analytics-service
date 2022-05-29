from BagelDBWrapper import BagelDBWrapper
from fastapi import Depends

from app.core.config import get_app_settings
from app.core.settings.app import AppSettings


async def check_health(settings: AppSettings = Depends(get_app_settings)) -> bool:
    return len(
        BagelDBWrapper(api_token=settings.api_token.get_secret_value(), enable_tqdm=True).get_collection('tags')) != 0
