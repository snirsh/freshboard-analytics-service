import aiohttp
from fastapi import Depends

from app.core.config import get_app_settings
from app.core.settings.app import AppSettings
from app.db.errors import EntityDoesNotExist
from app.db.repositories.base_repository import BaseRepository
from app.models.domain.companies import Company
from app.models.transformers.company_transformers import company_response_to_dto


class CompanyRepository(BaseRepository):
    def __init__(self, settings: AppSettings = Depends(get_app_settings)):
        super(CompanyRepository, self).__init__(settings)

    async def get_company_by_name(self, company_name: str) -> Company:
        async with aiohttp.ClientSession(headers=self.headers) as session:
            try:
                response = await session.get(f"{self.MASTER_URL}/collection/companies/items/",
                                             params=f'query=name:{company_name}')
                return company_response_to_dto((await response.json())[0])
            except IndexError:
                raise EntityDoesNotExist

