from abc import abstractmethod, ABC

from src.domain.entities.video import Video


class VideoRepository(ABC):
    @abstractmethod
    def criar_status_video(self, video: Video) -> None:
        pass

    @abstractmethod
    def consultar_status_video(self, username: str, nome_video: str) -> Video:
        pass

    @abstractmethod
    def atualizar_status_video(self, username: str, nome_video: str, status: str) -> None:
        pass
