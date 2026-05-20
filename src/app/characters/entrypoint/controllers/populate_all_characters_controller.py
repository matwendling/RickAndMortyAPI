from app.characters.domain.usecases.populate_all_characters_usecase import PopulateAllCharactersUsecase
from app.episodes.domain.flows.populate_all_episodes_flow import PopulateAllEpisodesFlow
from framework.dependency_injector import DependencyInjector

class PopulateAllCharactersController:
	def run(self) -> None:
		dependency_injector = DependencyInjector()
		usecase = PopulateAllCharactersUsecase(
			dependency_injector.get_character_repository_adapter(),
			dependency_injector.get_character_client(),
			dependency_injector.get_specie_repository_adapter(),
			dependency_injector.get_type_repository_adapter(),
			dependency_injector.get_origin_repository_adapter(),
			dependency_injector.get_location_repository_adapter(),
			PopulateAllEpisodesFlow(
				dependency_injector.get_episode_repository_adapter(),
				dependency_injector.get_episode_client(),
			)
		)
		usecase.execute()