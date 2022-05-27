from pydantic import BaseModel

from app.models.domain.boards import Board


class BoardInResponse(BaseModel):
    board: Board
