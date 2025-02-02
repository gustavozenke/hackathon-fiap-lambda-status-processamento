from abc import abstractmethod, ABC

from domain.entities.video import Video


class StatusProcessamentoRepository(ABC):
    @abstractmethod
    def criar_status_video(self, video: Video) -> None:
        pass

    @abstractmethod
    def consultar_status_video(self, nome_usuario: str) -> Video:
        pass
