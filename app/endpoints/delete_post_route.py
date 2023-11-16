from typing import List
from fastapi import status
from app.endpoints.base_route import BaseRoute, RouteInfo


class DeletePostRoute(BaseRoute):
    def _get_api_routes(self) -> List[RouteInfo]:
        return [
            RouteInfo(path="/{id}", endpoint=self.delete, method=["DELETE"], status_code=status.HTTP_204_NO_CONTENT)]

    async def delete(self, id: int):
        self._repo.delete(id)
