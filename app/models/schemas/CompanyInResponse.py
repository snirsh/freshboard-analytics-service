from typing import List

from pydantic import BaseModel

from app.models.domain.companies import Company


class CompanyInResponse(BaseModel):
    companies: List[Company]
