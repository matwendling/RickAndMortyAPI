from dataclasses import dataclass

@dataclass
class CreateEpisodeCharacterDTO:
    character_id: str
    episode_id: str