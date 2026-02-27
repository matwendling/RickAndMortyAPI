from dataclasses import dataclass

@dataclass
class EpisodeDTO:
    url: str
    num: int
    season: int