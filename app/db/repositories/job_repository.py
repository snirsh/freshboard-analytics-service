from typing import List

import aiohttp
from fastapi import Depends

from app.core.config import get_app_settings
from app.core.settings.app import AppSettings
from app.db.errors import EntityDoesNotExist
from app.db.repositories.base_repository import BaseRepository
from app.db.repositories.board_repository import BoardRepository
from app.db.repositories.company_repository import CompanyRepository
from app.models.domain.company_ref import CompanyRefModel
from app.models.domain.jobs import Job
from app.models.transformers.job_transformers import job_response_to_dto


class JobRepository(BaseRepository):
    def __init__(self, settings: AppSettings = Depends(get_app_settings)):
        super(JobRepository, self).__init__(settings)

    async def get_company_jobs(self, company_name: str) -> List[Job]:
        async with aiohttp.ClientSession(headers=self.headers) as session:
            try:
                company_id = (await CompanyRepository(settings=self.settings).get_company_by_name(company_name)).id
                response = await session.get(f"{self.MASTER_URL}/collection/jobs/items/",
                                             params=f'query=company.itemRefID:{company_id}')
                return list(map(lambda job: job_response_to_dto(job), await response.json()))
            except IndexError:
                raise EntityDoesNotExist

    async def get_active_board_jobs(self, board_domain_name: str) -> List[Job]:
        try:
            board_companies: List[CompanyRefModel] = (await BoardRepository(settings=self.settings)
                                                      .get_board_by_domain_name(board_domain_name)) \
                .companies
            params = []
            for company in board_companies:
                branches_ids: List[str] = list(map(lambda b: b.itemRefID, company.branchesNestedCollection))
                params += [{"query": f"active:true+company.branchesNestedCollection.itemRefID:{b_id}"} for b_id in branches_ids]
            branch_jobs_response = await self.parallel_fetching_by_params(
                url=f"{self.MASTER_URL}/collection/jobs/items/",
                params=params
            )
            return list(map(lambda job: job_response_to_dto(job), [job for branch in branch_jobs_response for job in branch]))
        except IndexError:
            raise EntityDoesNotExist

    async def get_non_active_board_jobs(self, board_domain_name: str) -> List[Job]:
        try:
            board_companies: List[CompanyRefModel] = (await BoardRepository(settings=self.settings)
                                                      .get_board_by_domain_name(board_domain_name)) \
                .companies
            params = []
            for company in board_companies:
                branches_ids: List[str] = list(map(lambda b: b.itemRefID, company.branchesNestedCollection))
                params += [{"query": f"active:false+company.branchesNestedCollection.itemRefID:{b_id}"} for b_id in branches_ids]
            branch_jobs_response = await self.parallel_fetching_by_params(
                url=f"{self.MASTER_URL}/collection/jobs/items/",
                params=params
            )
            return list(map(lambda job: job_response_to_dto(job), [job for branch in branch_jobs_response for job in branch]))
        except IndexError:
            raise EntityDoesNotExist
