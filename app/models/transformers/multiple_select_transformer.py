from typing import Optional, Mapping

from app.models.domain.MultipleSelectItem import MultipleSelectItem


def multi_reference_response_to_dto(multi_reference: Optional[Mapping[str, str]]) -> MultipleSelectItem | None:
    if not multi_reference:
        return None
    return MultipleSelectItem(
        _id=multi_reference.get('_id'),
        value=multi_reference.get('value')
    )