from typing import List

from app.models.domain.rwmodel import RWModel
from app.models.domain.tags_model import TagsModel


class TagsInResponse(RWModel):
    tags: List[TagsModel]