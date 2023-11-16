from abc import ABC, abstractmethod
from typing import List

from app.data.post import Post
from app.data.update_post import UpdatePost


class BaseRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Post]:
        pass

    @abstractmethod
    def get(self, id) -> Post:
        pass

    @abstractmethod
    def create(self, post: Post) -> Post:
        pass

    @abstractmethod
    def delete(self, id) -> None:
        pass

    @abstractmethod
    def update(self, id: int, update_post: UpdatePost) -> Post:
        pass
