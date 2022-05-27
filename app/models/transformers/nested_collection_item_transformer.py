from typing import Mapping

from app.models.domain.ref_item_model import RefItemModel


def nested_item_response_to_dto(nested_item: Mapping[str, str]) -> RefItemModel:
    return RefItemModel(itemRefID=nested_item.get('itemRefID'), value=nested_item.get('value'))
