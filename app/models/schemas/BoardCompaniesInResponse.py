from typing import List

from pydantic import BaseModel


class BoardCompaniesInResponse(BaseModel):
    total: int
    company_names: List[str]
