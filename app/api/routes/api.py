from fastapi import APIRouter

from app.api.routes import boards, companies, jobs, health

router = APIRouter()
router.include_router(boards.router, tags=["boards"], prefix="/boards")
router.include_router(companies.router, tags=["companies"], prefix="/companies")
router.include_router(jobs.router, tags=["jobs"], prefix="/jobs")
# router.include_router(users.router, tags=["users"], prefix="/user")
# router.include_router(profiles.router, tags=["profiles"], prefix="/profiles")
# router.include_router(articles.router, tags=["articles"])
# router.include_router(
#     comments.router,
#     tags=["comments"],
#     prefix="/articles/{slug}/comments",
# )
# router.include_router(tags.router, tags=["tags"], prefix="/tags")
