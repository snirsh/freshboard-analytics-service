from typing import List

from app.models.domain.ref_item_model import RefItemModel
from app.models.domain.rwmodel import RWModel


class CompanyRefModel(RWModel):
    itemRefID: str
    value: str
    branchesNestedCollection: List[RefItemModel]
