from datetime import date
from typing import List, Optional

from app.models.domain.MultipleSelectItem import MultipleSelectItem
from app.models.domain.company_ref import CompanyRefModel
from app.models.domain.ref_item_model import RefItemModel
from app.models.domain.rwmodel import RWModel


class Job(RWModel):
    lastUpdatedDate: date
    id: str
    position: str
    active: bool
    company: List[CompanyRefModel]
    jobDescription: str
    tags: Optional[List[RefItemModel]]
    remote: bool
    rawLocation: Optional[str]
    experienceLevel: Optional[MultipleSelectItem]
