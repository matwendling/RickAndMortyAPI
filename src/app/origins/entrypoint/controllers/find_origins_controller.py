from dataclasses import asdict

from app.origins.domain.dtos.find_origin import FindOriginDTO
from app.origins.domain.usecases.find_origins_usecase import FindOriginsUsecase
from app.origins.entrypoint.requests.find_origin_request import FindOriginsRequest
from framework.dependency_injector import DependencyInjector


class FindOriginsController:
    def run(self, where: FindOriginsRequest) -> list[dict]:
        dependency_injector = DependencyInjector()
        usecase = FindOriginsUsecase(
            dependency_injector.get_origin_repository_adapter()
        )
        res = usecase.execute(
            FindOriginDTO(
                name=where.name
            )
        )
        return [asdict(c) for c in res]