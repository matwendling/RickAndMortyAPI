from abc import ABC, abstractmethod

class IMigration(ABC):
    name: str

    @property
    @abstractmethod
    def query(self) -> str: ...
    
    @property
    @abstractmethod
    def params(self) -> list: ...