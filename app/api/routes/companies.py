from fastapi import APIRouter, Depends

from app.api.dependencies.companies import get_company_by_name_from_query
from app.models.domain.companies import Company
from app.models.schemas.CompanyInResponse import CompanyInResponse

router = APIRouter()


@router.get('/{company-name}',
            response_model=CompanyInResponse,
            name="companies:get-company",
            )
async def retrieve_company_by_name(
        company: Company = Depends(get_company_by_name_from_query),
) -> CompanyInResponse:
    return CompanyInResponse(companies=[company])
