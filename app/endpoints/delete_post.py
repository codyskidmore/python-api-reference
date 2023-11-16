from fastapi import APIRouter, status
from app.endpoints.base_route import BaseRoute, RouteInfo


class DeletePostRoute(BaseRoute):
    def _get_api_route(self) -> RouteInfo:
        return RouteInfo(path="/{id}", endpoint=self.delete, method=["DELETE"], status_code=status.HTTP_204_NO_CONTENT)

    async def delete(self, id: int):
        self._repo.delete(id)

# @router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete(id: int):
#     repo.delete(id)
