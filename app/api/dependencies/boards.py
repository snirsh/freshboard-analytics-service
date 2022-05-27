from fastapi import HTTPException, Path, Depends
from starlette.status import HTTP_404_NOT_FOUND

from app.core.config import get_app_settings
from app.core.settings.app import AppSettings
from app.db.errors import EntityDoesNotExist
from app.db.repositories.board_repository import BoardRepository
from app.models.domain.boards import Board
from app.resources import strings


async def get_board_by_domain_from_path(settings: AppSettings = Depends(get_app_settings), domain: str = Path(..., min_length=1)) -> \
        Board:
    try:
        return await BoardRepository(settings).get_board_by_domain_name(domain)
    except EntityDoesNotExist:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=strings.BOARD_NOT_FOUND
        )