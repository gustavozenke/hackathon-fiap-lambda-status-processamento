from datetime import datetime

from domain.entities.video import Video


class CriarStatusVideo:
    def __init__(self, video_repository):
        self.video_repository = video_repository

    def execute(self, nome_usuario, status_processamento, nome_video):
        video = Video(nome_usuario, status_processamento, str(datetime.now()), nome_video)
        self.video_repository.criar_status_video(video)
        return {
            "nome_video": nome_video,
            "nome_usuario": nome_usuario,
            "status": video.status.name
        }
