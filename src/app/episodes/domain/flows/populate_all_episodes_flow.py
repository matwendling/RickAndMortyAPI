from app.episodes.domain.clients.i_episode_client import IEpisodeClient
from app.episodes.domain.dtos.create_episode import CreateEpisodeDTO
from app.episodes.domain.repositories.i_episode_repository import IEpisodeRepository


class PopulateAllEpisodesFlow:
    def __init__(
            self,
            episode_repository: IEpisodeRepository,
            episode_client: IEpisodeClient,
        ) -> None:
            self.episode_repository = episode_repository
            self.episode_client = episode_client

    def execute(self) -> None:
        all_existing_episodes = self.episode_repository.get()
        if len(all_existing_episodes) == 0:
            episodes = []
            for episode_client in self.episode_client.fetch_all():
                episodes.append(
                    CreateEpisodeDTO(
                        name=episode_client.name,
                        num=episode_client.num,
                        season=episode_client.season
                    )
                )
            self.episode_repository.create_many(episodes)