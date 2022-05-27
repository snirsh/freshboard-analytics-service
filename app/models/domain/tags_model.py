from app.models.domain.rwmodel import RWModel


class TagsModel(RWModel):
    tag: str
    count: int
