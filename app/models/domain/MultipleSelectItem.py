from pydantic import BaseModel


class MultipleSelectItem(BaseModel):
    _id: str
    value: str