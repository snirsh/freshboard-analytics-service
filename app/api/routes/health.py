from fastapi import APIRouter, Depends

from app.api.dependencies.health_check import check_health

router = APIRouter()


@router.get('/health/',
            response_model=bool,
            name="health:health-check",
            )
async def check_health(
        health_check: bool = Depends(check_health),
) -> bool:
    return health_check

