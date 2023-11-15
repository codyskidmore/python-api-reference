from fastapi import APIRouter, status
from app.data import inmemory_repo

router = APIRouter(
    prefix="/posts",
    tags=["Post"],
    responses={404: {"description": "Not found"}},
)

repo = inmemory_repo.repo


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: int):
    repo.delete(id)
