import json
import os
from typing import Any

from app.characters.domain.clients.i_character_client import ICharacterClient
from app.characters.domain.repositories.i_character_repository import ICharacterRepository
from app.characters.infra.clients.rest_api_character_client import RestAPICharacterClient
from app.characters.infra.repositories.psycopg_character_repository import PsycopgCharacterRepository
from app.classification_types.domain.repositories.i_classification_type_repository import IClassificationTypeRepository
from app.classification_types.infra.repositories.psycopg_classification_type import PsycopgClassificationTypeRepository
from app.episodes.domain.repositories.i_episode_repository import IEpisodeRepository
from app.episodes.infra.repositories.psycopg_episode_repository import PsycopgEpisodeRepository
from app.locations.domain.repositories.i_location_repository import ILocationRepository
from app.locations.infra.repositories.psycopg_location_repository import PsycopgLocationRepository
from app.origins.domain.repositories.i_origin_repository import IOriginRepository
from app.origins.infra.repositories.psycopg_origin_repository import PsycopgOriginRepository
from app.species.domain.repositories.i_specie_repository import ISpecieRepository
from app.species.infra.repositories.psycopg_specie_repository import PsycopgSpecieRepository


class DependencyInjector:
	def __init__(self) -> None:
		self.injections = {
			"database": {
				"psycopg": {
					"character_repository": PsycopgCharacterRepository,
					"specie_repository": PsycopgSpecieRepository,
					"type_repository": PsycopgClassificationTypeRepository,
					"origin_repository": PsycopgOriginRepository,
					"location_repository": PsycopgLocationRepository,
					"episode_repository": PsycopgEpisodeRepository
				}
			},
			"client": {
				"rickandmorty": {
					"character_client": RestAPICharacterClient,
				}
			}
		}

	def get_character_repository_adapter(self) -> ICharacterRepository:
		return self.__load_adapter("database", "character_repository")

	def get_specie_repository_adapter(self) -> ISpecieRepository:
		return self.__load_adapter("database", "specie_repository")

	def get_type_repository_adapter(self) -> IClassificationTypeRepository:
		return self.__load_adapter("database", "type_repository")

	def get_origin_repository_adapter(self) -> IOriginRepository:
		return self.__load_adapter("database", "origin_repository")

	def get_location_repository_adapter(self) -> ILocationRepository:
		return self.__load_adapter("database", "location_repository")
	
	def get_episode_repository_adapter(self) -> IEpisodeRepository:
		return self.__load_adapter("database", "episode_repository")
	
	def get_character_client(self) -> ICharacterClient:
		return self.__load_adapter("client", "character_client")

	def __injections_payload_reader(self) -> dict:
		file_path = os.getenv("INJECTIONS_PATH")
		if file_path is None or len(file_path) == 0:
			raise FileNotFoundError("File could not be found or is empty.")
		with open(file_path) as json_data:
			return json.load(json_data)
		
	def __load_adapter(self, context: str, interface_name: str) -> Any:
		payload = self.__injections_payload_reader()
		payload_context = payload.get(context)
		if payload_context is not None:
			return self.injections[context][payload_context][interface_name]()