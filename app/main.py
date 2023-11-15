# main.py

import uvicorn
from fastapi import FastAPI

from app.endpoints import create_post, update_post, get_post, delete_post

app = FastAPI(title="Python API", description="Python API Reference")


@app.get("/")
async def root():
    return {"message": "Nothing to see here"}


app.include_router(create_post.router)
app.include_router(update_post.router)
app.include_router(get_post.router)
app.include_router(delete_post.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
