from dataclasses import asdict

from app.characters.domain.dtos.find_character import FindCharacterDTO
from app.characters.domain.usecases.find_characters_usecase import FindCharactersUsecase
from app.characters.entrypoint.requests.find_character_request import FindCharacterRequest
from framework.dependency_injector import DependencyInjector

class FindCharactersController:
    def run(self, where: FindCharacterRequest) -> list[dict]:
        dependency_injector = DependencyInjector()
        usecase = FindCharactersUsecase(
            dependency_injector.get_character_repository_adapter()
        )
        res = usecase.execute(
            FindCharacterDTO(
                name=where.name,
                status=where.status,
                specie_id=where.specie_id,
                type_id=where.type_id,
                gender=where.gender,
                origin_id=where.origin_id,
                location_id=where.location_id
            )
        )
        return [asdict(c) for c in res]