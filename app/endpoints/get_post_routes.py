from typing import List

from fastapi import status, HTTPException
from app.endpoints.base_route import BaseRoute, RouteInfo


class GetPostRoutes(BaseRoute):
    def _get_api_routes(self) -> List[RouteInfo]:
        return [
            RouteInfo(path="", endpoint=self.get_all, method=["GET"], status_code=status.HTTP_200_OK),
            RouteInfo(path="/{id}", endpoint=self.get, method=["GET"], status_code=status.HTTP_200_OK)
        ]

    async def get_all(self):
        return self._repo.get_all()

    async def get(self, id: int):
        post = self._repo.get(id)
        if not post:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"Response": f"Post not found for id: {id}."}
            )
        return post
