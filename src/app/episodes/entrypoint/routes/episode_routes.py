from fastapi import APIRouter
from app.episodes.entrypoint.controllers.find_episodes_controller import FindEpisodesController
from app.episodes.entrypoint.requests.find_episode_request import FindEpisodeRequest

episode_route = APIRouter(prefix="/episodes")

@episode_route.post("/find")
def get_episodes(where: FindEpisodeRequest = FindEpisodeRequest()) -> list[dict]:
    return FindEpisodesController().run(where)