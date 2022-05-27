from fastapi import APIRouter, Depends

from app.api.dependencies.boards import get_board_by_domain_from_path
from app.models.domain.boards import Board
from app.models.schemas.BoardCompaniesInResponse import BoardCompaniesInResponse
from app.models.schemas.BoardInResponse import BoardInResponse

router = APIRouter()


@router.get('/{domain}',
            response_model=BoardInResponse,
            name="boards:get-board",
            )
async def retrieve_board_by_domain_name(
        board: Board = Depends(get_board_by_domain_from_path),
) -> BoardInResponse:
    return BoardInResponse(board=board)


@router.get('/{domain}/companies',
            response_model=BoardCompaniesInResponse,
            name="boards:get-companies"
            )
async def retrieve_board_companies_by_domain_name(
        board: Board = Depends(get_board_by_domain_from_path)
) -> BoardCompaniesInResponse:
    return BoardCompaniesInResponse(
        total=len(board.companies),
        company_names=list(map(lambda c: c.value, board.companies))
    )
