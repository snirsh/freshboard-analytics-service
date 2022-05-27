from typing import Mapping, Optional

from app.models.domain.ref_item_model import RefItemModel


def item_reference_response_to_dto(item_ref: Optional[Mapping[str, str]]) -> RefItemModel | None:
    if not item_ref:
        return None
    return RefItemModel(
        itemRefID=item_ref.get("itemRefID"),
        value=item_ref.get("value")
    )