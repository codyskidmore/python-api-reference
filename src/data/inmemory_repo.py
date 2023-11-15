# from pydantic import BaseModel
from src.data.post import Post
from src.data.update_post import UpdatePost


class InMemoryRepo():
    __posts = {}

    def __init__(self):
        self.__posts[1] = Post(id=1, title="My Title 1", content="My Content 1")
        self.__posts[2] = Post(id=2, title="My Title 2", content="My Content 2")

    def get_all(self):
        return self.__posts

    def get(self, id):
        if id not in self.__posts:
            return
        return self.__posts[id]

    def create(self, post: Post):
        if post.id in self.__posts:
            return
        self.__posts[post.id] = post
        return post

    def delete(self, id):
        if id in self.__posts:
            del self.__posts[id]
        return

    def update(self, id: int, update_post: UpdatePost):
        if id not in self.__posts:
            return
        existing_post = self.__posts[id]
        update_dict = update_post.model_dump(exclude_unset=True)
        for key in update_dict:
            existing_post.__dict__[key] = update_dict[key]
        self.__posts[existing_post.id] = existing_post
        return existing_post
