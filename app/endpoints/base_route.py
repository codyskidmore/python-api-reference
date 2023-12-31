from abc import ABC, abstractmethod
from collections import namedtuple
from typing import List

from fastapi import APIRouter, status

from app.data.base_repository import BaseRepository

RouteInfo = namedtuple('RouteInfo', 'path endpoint method status_code')


class BaseRoute(ABC):
    _router: APIRouter
    _repo: BaseRepository

    def __init__(self, api_router: APIRouter, repo: BaseRepository):
        self._router = api_router
        self._repo = repo
        self._add_routes()

    def _add_routes(self):
        route_infos = self._get_api_routes()
        for route_info in route_infos:
            self._router.add_api_route(route_info.path, route_info.endpoint, methods=route_info.method,
                                       status_code=route_info.status_code)

    @abstractmethod
    def _get_api_routes(self) -> List[RouteInfo]:
        pass

    def get_api_routes(self) -> APIRouter:
        return self._router
