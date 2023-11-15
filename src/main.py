# main.py

import uvicorn
from fastapi import FastAPI, status, HTTPException
from src.data.post import Post
from src.data.update_post import UpdatePost
from src.data.inmemory_repo import InMemoryRepo

app = FastAPI(title="Python API", description="Python API Reference")

repo = InMemoryRepo()


# Note to reader:
#   These endpoints will live in separate files.

@app.get("/")
async def root():
    return {"message": "Nothing to see here"}


@app.get("/posts")
async def get_all():
    return repo.get_all()


# TODO: Investigate why "/posts/{id:int}" doesn't actually work.
@app.get("/posts/{id}")
async def get(id: int):
    post = repo.get(id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"Response": f"Post not found for id: {id}."}
        )
    return post


@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create(new_post: Post):
    post = repo.create(new_post)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={"Response": f"Post already exists for id: {new_post.id}."}
        )
    return {"new_post": new_post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: int):
    repo.delete(id)


@app.put("/posts")
async def put(update_post: UpdatePost):
    updated_post = repo.update(update_post)
    if not updated_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"Response": f"Post not found for id: {update_post.id}."}
        )
    return updated_post


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
