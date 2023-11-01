# main.py

import uvicorn
from fastapi import FastAPI
from src.data.post import Post
from src.data.inmemory_repo import InMemoryRepo

app = FastAPI(title="Python API", description="Python API Reference")

repo = InMemoryRepo()


# Note to reader:
#   These endpoints will live in separate files.

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/posts")
async def get_all_posts():
    return repo.get_all()


# TODO: Investigate why "/posts/{id:int}" doesn't actually work.
@app.get("/posts/{id}")
async def get_post(id: int):
    return repo.get(id)


@app.post("/posts")
def create_post(new_post: Post):
    repo.create(new_post)
    print(new_post)
    return {"new_post": new_post}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
