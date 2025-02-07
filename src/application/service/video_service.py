from application.usecases.consultar_status_video import ConsultarStatusVideo
from application.usecases.criar_status_video import CriarStatusVideo


class VideoService:
    def __init__(self, video_repository):
        self.create_video_use_case = CriarStatusVideo(video_repository)
        self.get_video_status_use_case = ConsultarStatusVideo(video_repository)

    def criar_status_video(self, nome_usuario, status_processamento, nome_video, url_video):
        return self.create_video_use_case.execute(nome_usuario, status_processamento, nome_video, url_video)

    def consultar_status_video(self, nome_usuario):
        return self.get_video_status_use_case.execute(nome_usuario)
