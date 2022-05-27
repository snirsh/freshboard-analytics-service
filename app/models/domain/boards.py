from typing import List

from app.models.domain.company_ref import CompanyRefModel
from app.models.domain.rwmodel import RWModel


class Board(RWModel):
    name: str = ""
    domain: str = ""
    companies: List[CompanyRefModel] = []
