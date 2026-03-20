from dataclasses import dataclass

@dataclass
class CreateEpisodeDTO:
    url: str
    num: int
    season: int