from abc import abstractmethod, ABC

from domain.entities.video import Video


class StatusProcessamentoRepositoryInterface(ABC):
    @abstractmethod
    def put_item(self, video: Video) -> None:
        pass

    @abstractmethod
    def table_query(self, key_condition: str, expression_attr_values: dict):
        pass
