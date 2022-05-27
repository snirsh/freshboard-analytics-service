import datetime
from typing import List

from fastapi import HTTPException, Depends
from fastapi.params import Path
from starlette.status import HTTP_404_NOT_FOUND

from app.core.config import get_app_settings
from app.core.settings.app import AppSettings
from app.db.errors import EntityDoesNotExist
from app.db.repositories.job_repository import JobRepository
from app.models.domain.jobs import Job
from app.models.domain.tags_model import TagsModel
from app.resources import strings


async def get_company_jobs_by_name_in_query(settings: AppSettings = Depends(get_app_settings),
                                            company_name: str = Path(..., min_length=1)) -> \
        List[Job]:
    try:
        return await JobRepository(settings).get_company_jobs(company_name)
    except EntityDoesNotExist:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=strings.BOARD_NOT_FOUND
        )


async def get_active_board_jobs_by_domain(settings: AppSettings = Depends(get_app_settings),
                                          domain: str = Path(..., min_length=1)) -> \
        List[Job]:
    try:
        return await JobRepository(settings).get_active_board_jobs(domain)
    except EntityDoesNotExist:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=strings.BOARD_NOT_FOUND
        )


async def get_active_this_month_by_board_jobs_by_domain(settings: AppSettings = Depends(get_app_settings),
                                                        domain: str = Path(..., min_length=1)) -> \
        List[Job]:
    try:

        active = await JobRepository(settings).get_active_board_jobs(domain)
        active_this_month = list(filter(lambda j: j.lastUpdatedDate.month == datetime.datetime.now().month, active))
        return active_this_month
    except EntityDoesNotExist:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=strings.BOARD_NOT_FOUND
        )


async def get_non_active_this_month_by_board_jobs_by_domain(settings: AppSettings = Depends(get_app_settings),
                                                            domain: str = Path(..., min_length=1)) -> \
        List[Job]:
    try:

        active = await JobRepository(settings).get_non_active_board_jobs(domain)
        active_this_month = list(filter(lambda j: j.lastUpdatedDate.month == datetime.datetime.now().month, active))
        return active_this_month
    except EntityDoesNotExist:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=strings.BOARD_NOT_FOUND
        )


async def get_active_tags_this_month_by_board_jobs_by_domain(settings: AppSettings = Depends(get_app_settings),
                                                             domain: str = Path(..., min_length=1)) -> \
        List[TagsModel]:
    try:
        this_month = await get_active_this_month_by_board_jobs_by_domain(settings, domain)
        tags = set()
        for j in this_month:
            for t in j.tags:
                tags.add(t.value)
        tags_count = {t: 0 for t in tags}
        for j in this_month:
            for tag in j.tags:
                tags_count[tag.value] += 1
        tags_model = [TagsModel(tag=t, count=i) for t, i in tags_count.items()]
        return tags_model
    except EntityDoesNotExist:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=strings.BOARD_NOT_FOUND
        )
