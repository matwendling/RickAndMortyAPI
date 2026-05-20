from app.characters.domain.clients.i_character_client import ICharacterClient
from app.characters.domain.dtos.character_client.character_client_dto import CharacterClientDTO
from app.characters.domain.dtos.create_character import CreateCharacterDTO
from app.characters.domain.repositories.i_character_repository import ICharacterRepository
from app.classification_types.domain.dtos import classification_type
from app.classification_types.domain.dtos.create_classification_type import CreateClassificationTypeDTO
from app.classification_types.domain.dtos.find_classification_type import FindClassificationTypeDTO
from app.classification_types.domain.repositories.i_classification_type_repository import IClassificationTypeRepository
from app.episodes.domain.dtos.create_episode import CreateEpisodeDTO
from app.episodes.domain.flows.populate_all_episodes_flow import PopulateAllEpisodesFlow
from app.locations.domain.dtos.create_location import CreateLocationDTO
from app.locations.domain.dtos.find_location import FindLocationDTO
from app.locations.domain.repositories.i_location_repository import ILocationRepository
from app.origins.domain.dtos.create_origin import CreateOriginDTO
from app.origins.domain.dtos.find_origin import FindOriginDTO
from app.origins.domain.repositories.i_origin_repository import IOriginRepository
from app.species.domain.dtos.create_specie import CreateSpecieDTO
from app.species.domain.dtos.find_specie import FindSpecieDTO
from app.species.domain.repositories.i_specie_repository import ISpecieRepository


class PopulateAllCharactersUsecase:
    def __init__(
        self, 
        character_repository: ICharacterRepository, 
        character_client: ICharacterClient, 
        specie_repository: ISpecieRepository, 
        type_repository: IClassificationTypeRepository,
        origin_repository: IOriginRepository,
        location_repository: ILocationRepository,
        populate_all_episodes_flow: PopulateAllEpisodesFlow
    ) -> None:
        self.character_repository = character_repository
        self.character_client = character_client
        self.specie_repository = specie_repository
        self.type_repository = type_repository
        self.origin_repository = origin_repository
        self.location_repository = location_repository
        self.populate_all_episodes_flow = populate_all_episodes_flow

    def execute(self) -> None:
        self.populate_all_episodes_flow.execute()
        all_existing_characters = self.character_repository.get()
        if len(all_existing_characters) == 0:
            characters = []
            for character_client in self.character_client.fetch_all():
                characters.append(
                    CreateCharacterDTO(
                        name=character_client.name,
                        status=character_client.status.lower(),
                        specie_id=self.__handle_specie(character_client),
                        type_id=self.__handle_type(character_client),
                        gender=character_client.gender.lower(),
                        origin_id=self.__handle_origin(character_client),
                        location_id=self.__handle_location(character_client),
                        image=character_client.image,
                        api_id=character_client.id,
                    )
                )
            self.character_repository.create_many(characters)

    def __handle_specie(self, character_client: CharacterClientDTO) -> str:
        found_specie = self.specie_repository.get(
            FindSpecieDTO(name=character_client.specie)
        )
        if len(found_specie) == 0:
            return self.specie_repository.create(
                CreateSpecieDTO(name=character_client.specie)
            ).id
        return found_specie[0].id

    def __handle_type(self, character_client: CharacterClientDTO) -> str:
        found_type = self.type_repository.get(
            FindClassificationTypeDTO(name=character_client.character_type)
        )
        if len(found_type) == 0:
            return self.type_repository.create(
                CreateClassificationTypeDTO(name=character_client.character_type)
            ).id
        return found_type[0].id

    def __handle_origin(self, character_client: CharacterClientDTO) -> str:
        found_origin = self.origin_repository.get(
            FindOriginDTO(name=character_client.origin)
        )
        if len(found_origin) == 0:
            return self.origin_repository.create(
                CreateOriginDTO(name=character_client.origin)
            ).id
        return found_origin[0].id

    def __handle_location(self, character_client: CharacterClientDTO) -> str:
        found_location = self.location_repository.get(
            FindLocationDTO(name=character_client.location)
        )
        if len(found_location) == 0:
            return self.location_repository.create(
                CreateLocationDTO(name=character_client.location)
            ).id
        return found_location[0].id