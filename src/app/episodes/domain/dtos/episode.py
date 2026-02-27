from dataclasses import dataclass

@dataclass
class EpisodeDTO:
    id: str
    url: str
    num: int
    season: int