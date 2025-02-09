from abc import abstractmethod, ABC


class StatusProcessamentoRepository(ABC):
    @abstractmethod
    def put_item(self, item: dict):
        pass

    @abstractmethod
    def table_query(self, key_condition: str, expression_attr_values: dict):
        pass
