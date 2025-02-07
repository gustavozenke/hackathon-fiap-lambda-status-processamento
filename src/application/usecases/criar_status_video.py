from datetime import datetime

from domain.entities.video import Video


class CriarStatusVideo:
    def __init__(self, video_repository):
        self.video_repository = video_repository

    def execute(self, nome_usuario, status_processamento, nome_video, url_video):
        data_hora_inclusao = str(datetime.now())
        video = Video(nome_usuario, status_processamento, data_hora_inclusao, nome_video, url_video)
        self.video_repository.criar_status_video(video)
        return {
            "nome_usuario": nome_usuario,
            "data_hora_inclusao": data_hora_inclusao,
            "nome_video": nome_video,
            "status_processamento": video.status.name
        }
