import aiohttp
from fastapi import Depends

from app.core.config import get_app_settings
from app.core.settings.app import AppSettings
from app.db.errors import EntityDoesNotExist
from app.db.repositories.base_repository import BaseRepository
from app.models.domain.boards import Board


class BoardRepository(BaseRepository):
    def __init__(self, settings: AppSettings = Depends(get_app_settings)):
        super(BoardRepository, self).__init__(settings)

    async def get_board_by_domain_name(self, board_name: str) -> Board:
        async with aiohttp.ClientSession(headers=self.headers) as session:
            try:
                response = await session.get(f"{self.MASTER_URL}/collection/boards/items/",
                                             params=f'query=domain:{board_name}')
                name = (await response.json())[0].get('name')
                domain = (await response.json())[0].get('domain')
                companies = (await response.json())[0].get('companies')
                return Board(name=name, domain=domain, companies=companies)
            except IndexError:
                raise EntityDoesNotExist
