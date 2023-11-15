from fastapi import APIRouter, status
from app.data.inmemory_repo import InMemoryRepo

router = APIRouter(
    prefix="/posts",
    tags=["Post"],
    responses={404: {"description": "Not found"}},
)

# repo = InMemoryRepo.get_instance()
repo = InMemoryRepo()


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: int):
    repo.delete(id)
