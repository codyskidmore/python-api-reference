from fastapi import APIRouter, status, HTTPException
from app.data.update_post import UpdatePost
from app.data.inmemory_repo import InMemoryRepo

router = APIRouter(
    prefix="/posts",
    tags=["Post"],
    responses={404: {"description": "Not found"}},
)

repo = InMemoryRepo()


@router.put("/{id}")
async def put(update_post: UpdatePost, id: int):
    updated_post = repo.update(id, update_post)
    if not updated_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"Response": f"Post not found for id: {update_post.id}."}
        )
    return updated_post
