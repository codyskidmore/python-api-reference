from app.data.post import Post
from fastapi import APIRouter, status, HTTPException
from app.data.inmemory_repo import InMemoryRepo

router = APIRouter(
    prefix="/posts",
    tags=["Post"],
    responses={404: {"description": "Not found"}},
)

repo = InMemoryRepo()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(new_post: Post):
    post = repo.create(new_post)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={"Response": f"Post already exists for id: {new_post.id}."}
        )
    return {"new_post": new_post}
