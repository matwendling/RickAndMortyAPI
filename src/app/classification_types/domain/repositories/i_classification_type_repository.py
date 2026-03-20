from abc import ABC, abstractmethod

from app.classification_types.domain.dtos.create_classification_type import CreateClassificationTypeDTO
from app.classification_types.domain.dtos.classification_type import ClassificationTypeDTO
from app.classification_types.domain.dtos.find_classification_type import FindClassificationTypeDTO
from app.classification_types.domain.dtos.update_classification_type import UpdateClassificationTypeDTO

class IClassificationTypeRepository(ABC):
    @abstractmethod
    def create(self, create: CreateClassificationTypeDTO) -> ClassificationTypeDTO:
        """
        Creates a new classification type.

        Args:
            create: DTO containing the data of the classification type that will be created.
        
        Returns:
            ClassificationTypeDTO: A new classification type.
        """
    
    @abstractmethod
    def get(self, where: FindClassificationTypeDTO) -> list[ClassificationTypeDTO]:
        """
        Searches for one or multiple classification types following specific filter criteria.

        Args:
            where: DTO containing filter criteria.

        Returns:
            list[ClassificationTypeDTO]: Returns a list of all the classification types matching the filter.
        """

    @abstractmethod
    def update(self, uuid: str, update: UpdateClassificationTypeDTO) -> str:
        """
        Updates one or more data of a classification type.

        Args:
            uuid: UUID of the classification type to be updated.
            update: DTO containing which fields of the classification type will be updated.

        Returns:
            str: Returns the UUID of the classification type.
        """

    @abstractmethod
    def delete(self, uuid: str) -> None:
        """
        Deletes an classification type.

        Args:
            uuid: UUID of the classification type to be deleted.

        Returns:
            None: No return, since the classification type doesn't exist anymore. 
        """