from fastapi import status, HTTPException
from app.data.update_post import UpdatePost
from app.endpoints.base_route import BaseRoute, RouteInfo


class UpdatePostRoute(BaseRoute):
    def _get_api_route(self) -> RouteInfo:
        return RouteInfo(path="/{id}", endpoint=self.put, method=["PUT"], status_code=status.HTTP_200_OK)

    async def put(self, update_post: UpdatePost, id: int):
        updated_post = self._repo.update(id, update_post)
        if not updated_post:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"Response": f"Post not found for id: {update_post.id}."}
            )
        return updated_post
