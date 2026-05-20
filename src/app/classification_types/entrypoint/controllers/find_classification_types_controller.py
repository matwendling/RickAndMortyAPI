from dataclasses import asdict

from app.classification_types.domain.dtos.find_classification_type import FindClassificationTypeDTO
from app.classification_types.domain.usecases.find_classification_types_usecase import FindClassificationTypesUsecase
from app.classification_types.entrypoint.requests.find_classification_types_request import FindClassificationTypesRequest
from framework.dependency_injector import DependencyInjector


class FindClassificationTypesController:
    def run(self, where: FindClassificationTypesRequest) -> list[dict]:
        dependency_injector = DependencyInjector()
        usecase = FindClassificationTypesUsecase(
            dependency_injector.get_type_repository_adapter()
        )
        res = usecase.execute(
            FindClassificationTypeDTO(
                name=where.name,
            )
        )
        return [asdict(r) for r in res]