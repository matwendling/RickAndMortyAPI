from app.episodes.domain.dtos.episode import EpisodeDTO
from app.episodes.domain.dtos.find_episode import FindEpisodeDTO
from app.episodes.domain.repositories.i_episode_repository import IEpisodeRepository


class FindEpisodesUsecase:
    def __init__(
            self, episode_repository: IEpisodeRepository
        ):
            self.episode_repository = episode_repository

    def execute(self, where: FindEpisodeDTO) -> list[EpisodeDTO]:
        return self.episode_repository.get(where)