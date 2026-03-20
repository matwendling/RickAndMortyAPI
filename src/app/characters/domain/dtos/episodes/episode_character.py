from dataclasses import dataclass

@dataclass
class EpisodeCharacterDTO:
    id: str
    character_id: str
    episode_id: str