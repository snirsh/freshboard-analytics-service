from typing import Mapping

from dateutil.parser import isoparse

from app.models.domain.jobs import Job
from app.models.transformers.company_transformers import company_ref_to_dto
from app.models.transformers.item_reference_transformer import item_reference_response_to_dto
from app.models.transformers.multiple_select_transformer import multi_reference_response_to_dto


def job_response_to_dto(job_response: Mapping[str, str]) -> Job:
    return Job(
        lastUpdatedDate=isoparse(job_response.get('_lastUpdatedDate')),
        id=job_response.get('_id'),
        position=job_response.get('position'),
        active=bool(job_response.get('active')),
        company=list(map(lambda c: company_ref_to_dto(c), job_response.get('company'))),
        jobDescription=job_response.get('jobDescription'),
        tags=list(map(lambda tag: item_reference_response_to_dto(tag), job_response.get('tags'))),
        remote=bool(job_response.get('remote')),
        rawLocation=job_response.get('rawLocation'),
        experienceLevel=multi_reference_response_to_dto(job_response.get('experienceLevel'))
    )
