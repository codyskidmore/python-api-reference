from fastapi import APIRouter, status, HTTPException
from app.data import inmemory_repo

router = APIRouter(
    prefix="/posts",
    tags=["Post"],
    responses={404: {"description": "Not found"}},
)

repo = inmemory_repo.repo


@router.get("/")
async def get_all():
    return repo.get_all()


# TODO: Investigate why "/posts/{id:int}" doesn't actually work.
@router.get("/{id}")
async def get(id: int):
    post = repo.get(id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"Response": f"Post not found for id: {id}."}
        )
    return post
