from fastapi import HTTPException, Depends, Path
from starlette.status import HTTP_404_NOT_FOUND

from app.core.config import get_app_settings
from app.core.settings.app import AppSettings
from app.db.errors import EntityDoesNotExist
from app.db.repositories.company_repository import CompanyRepository
from app.models.domain.companies import Company
from app.resources import strings


async def get_company_by_name_from_query(settings: AppSettings = Depends(get_app_settings), name: str = Path(..., min_length=1)) -> \
        Company:
    try:
        return await CompanyRepository(settings).get_company_by_name(name)
    except EntityDoesNotExist:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=strings.BOARD_NOT_FOUND
        )