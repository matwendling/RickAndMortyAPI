

from app.classification_types.domain.dtos.classification_type import ClassificationTypeDTO
from app.classification_types.domain.dtos.find_classification_type import FindClassificationTypeDTO
from app.classification_types.domain.repositories.i_classification_type_repository import IClassificationTypeRepository


class FindClassificationTypesUsecase:
    def __init__(
            self, classification_type_repository: IClassificationTypeRepository
        ):
            self.classification_type_repository = classification_type_repository
    
    def execute(self, where: FindClassificationTypeDTO) -> ClassificationTypeDTO:
        return self.classification_type_repository.get(where)