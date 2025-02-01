from application.usecases.atualizar_status_video import AtualizarStatusVideo
from application.usecases.consultar_status_video import ConsultarStatusVideo
from application.usecases.criar_status_video import CriarStatusVideo


class VideoService:
    def __init__(self, video_repository):
        self.create_video_use_case = CriarStatusVideo(video_repository)
        self.update_video_status_use_case = AtualizarStatusVideo(video_repository)
        self.get_video_status_use_case = ConsultarStatusVideo(video_repository)

    def criar_status_video(self, username, nome_video):
        return self.create_video_use_case.execute(username, nome_video)

    def atualizar_status_video(self, username, nome_video, status):
        return self.update_video_status_use_case.execute(username, nome_video, status)

    def consultar_status_video(self, username, nome_video):
        return self.get_video_status_use_case.execute(username, nome_video)
