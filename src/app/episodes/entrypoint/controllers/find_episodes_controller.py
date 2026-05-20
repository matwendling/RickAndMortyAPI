from dataclasses import asdict

from app.episodes.domain.dtos.find_episode import FindEpisodeDTO
from app.episodes.domain.usecases.find_episodes_usecase import FindEpisodesUsecase
from app.episodes.entrypoint.requests.find_episode_request import FindEpisodeRequest
from framework.dependency_injector import DependencyInjector


class FindEpisodesController:
    def run(self, where: FindEpisodeRequest) -> list[dict]:
        dependency_injector = DependencyInjector()
        usecase = FindEpisodesUsecase(
            dependency_injector.get_episode_repository_adapter()
        )
        res = usecase.execute(
            FindEpisodeDTO(
                url=where.url,
                num=where.num,
                season=where.season
            )
        )
        return [asdict(e) for e in res]