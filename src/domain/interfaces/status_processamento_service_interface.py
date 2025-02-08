from abc import abstractmethod, ABC

from domain.entities.video import Video


class StatusProcessamentoServiceInterface(ABC):
    @abstractmethod
    def incluir_evento_processamento(self, video: Video):
        pass

    @abstractmethod
    def consultar_eventos_usuario(self, nome_usuario: str):
        pass
