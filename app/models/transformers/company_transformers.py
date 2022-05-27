from typing import Mapping

from app.models.domain.companies import Company
from app.models.domain.company_ref import CompanyRefModel
from app.models.transformers.item_reference_transformer import item_reference_response_to_dto
from app.models.transformers.nested_collection_item_transformer import nested_item_response_to_dto


def company_response_to_dto(company_response: Mapping[str, str]) -> Company:
    return Company(
        id=company_response.get("_id"),
        name=company_response.get("name"),
        manualCompany=bool(company_response.get("manualCompany")),
        tagline=company_response.get("tagline"),
        description=company_response.get("description"),
        industries=list(map(lambda i: item_reference_response_to_dto(i), company_response.get("industries"))),
        website=company_response.get("website"),
        juniorFriendly=bool(company_response.get("juniorFriendly")),
        remote=bool(company_response.get("remote")),
    )


def company_ref_to_dto(company_ref: Mapping[str, str]) -> CompanyRefModel:
    return CompanyRefModel(itemRefID=company_ref.get('itemRefID'), value=company_ref.get('value'),
                            branchesNestedCollection=list(map(lambda branch: nested_item_response_to_dto(branch),
                                                              company_ref.get('branchesNestedCollection'))))
