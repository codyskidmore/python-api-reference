# from pydantic import BaseModel
from src.data.post import Post


class InMemoryRepo():
    __posts = {}

    def __init__(self):
        self.__posts[1] = Post(id=1, title="My Title 1", content="My Content 1")
        self.__posts[2] = Post(id=2, title="My Title 2", content="My Content 2")

    def get_all(self):
        return self.__posts

    def get(self, id):
        return self.__posts[id]

    def create(self, post):
        self.__posts[post.id] = post
        return post
