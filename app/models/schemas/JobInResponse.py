from typing import List

from pydantic import BaseModel

from app.models.domain.jobs import Job


class JobsInResponse(BaseModel):
    jobs: List[Job]
    total: int
