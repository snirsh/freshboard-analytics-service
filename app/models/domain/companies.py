from typing import List

from app.models.domain.ref_item_model import RefItemModel
from app.models.domain.rwmodel import RWModel


class Company(RWModel):
    id: str
    name: str
    manualCompany: bool
    tagline: str
    description: str
    industries: List[RefItemModel]
    website: str
    juniorFriendly: bool
    remote: bool
