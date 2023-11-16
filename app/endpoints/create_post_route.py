from app.data.post import Post
from fastapi import status, HTTPException
from app.endpoints.base_route import BaseRoute, RouteInfo


class CreatePostRoute(BaseRoute):
    def _get_api_route(self) -> RouteInfo:
        return RouteInfo(path="/", endpoint=self.create, method=["POST"], status_code=status.HTTP_201_CREATED)

    async def create(self, new_post: Post):
        post = self._repo.create(new_post)
        if not post:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail={"Response": f"Post already exists for id: {new_post.id}."}
            )
        return {"new_post": new_post}
