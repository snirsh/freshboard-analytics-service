from typing import List

from fastapi import APIRouter, Depends

from app.api.dependencies.jobs import get_company_jobs_by_name_in_query, get_active_board_jobs_by_domain, \
    get_active_this_month_by_board_jobs_by_domain, get_non_active_this_month_by_board_jobs_by_domain, \
    get_active_tags_this_month_by_board_jobs_by_domain
from app.models.domain.jobs import Job
from app.models.domain.tags_model import TagsModel
from app.models.schemas.JobInResponse import JobsInResponse
from app.models.schemas.TagsInResponse import TagsInResponse

router = APIRouter()


@router.get('/{company-name}/',
            response_model=JobsInResponse,
            name="jobs:get-company-jobs",
            )
async def retrieve_company_jobs_by_name(
        jobs: List[Job] = Depends(get_company_jobs_by_name_in_query),
) -> JobsInResponse:
    return JobsInResponse(jobs=jobs, total=len(jobs))


@router.get('/{domain}/active',
            response_model=JobsInResponse,
            name="jobs:get-board-jobs",
            )
async def retrieve_active_board_jobs_by_domain(
        jobs: List[Job] = Depends(get_active_board_jobs_by_domain),
) -> JobsInResponse:
    return JobsInResponse(jobs=[], total=len(jobs))


@router.get('/{domain}/active-this-month',
            response_model=JobsInResponse,
            name="jobs:get-board-active-this-month"
            )
async def retrieve_active_this_month_by_board_domain(
        jobs: List[Job] = Depends(get_active_this_month_by_board_jobs_by_domain)
) -> JobsInResponse:
    return JobsInResponse(jobs=[], total=len(jobs))


@router.get('/{domain}/non-active-this-month',
            response_model=JobsInResponse,
            name="jobs:get-board-non-active-this-month"
            )
async def retrieve_non_active_this_month_by_board_domain(
        jobs: List[Job] = Depends(get_non_active_this_month_by_board_jobs_by_domain)
) -> JobsInResponse:
    return JobsInResponse(jobs=[], total=len(jobs))


@router.get('/{domain}/active-tags-this-month',
            response_model=TagsInResponse,
            name="jobs:get-board-active-tags-this-month"
            )
async def retrieve_non_active_this_month_by_board_domain(
        tags: List[TagsModel] = Depends(get_active_tags_this_month_by_board_jobs_by_domain)
) -> TagsInResponse:
    return TagsInResponse(tags=tags)
