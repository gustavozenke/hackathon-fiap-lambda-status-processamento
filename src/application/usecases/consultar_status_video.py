class ConsultarStatusVideo:
    def __init__(self, video_repository):
        self.video_repository = video_repository

    def execute(self, nome_usuario):
        video = self.video_repository.consultar_status_video(nome_usuario)
        return {"nome_video": video.nome_video, "status": video.status}
