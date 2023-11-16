# main.py

import uvicorn
from fastapi import FastAPI, APIRouter

from app.data.inmemory_repository import InMemoryRepository
from app.endpoints import update_post_route, get_post, delete_post
from app.endpoints.create_post_route import CreatePostRoute
from app.endpoints.delete_post import DeletePostRoute
from app.endpoints.update_post_route import UpdatePostRoute

app = FastAPI(title="Python API", description="Python API Reference")


@app.get("/")
async def root():
    return {"message": "Nothing to see here"}


def get_api_router() -> APIRouter:
    return APIRouter(
        prefix="/posts",
        tags=["Post"],
        responses={404: {"description": "Not found"}},
    )


repo = InMemoryRepository()
api_router = get_api_router()

app.include_router(CreatePostRoute(api_router, repo).get_api_routes())
app.include_router(UpdatePostRoute(api_router, repo).get_api_routes())
app.include_router(get_post.router)
app.include_router(DeletePostRoute(api_router, repo).get_api_routes())

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
