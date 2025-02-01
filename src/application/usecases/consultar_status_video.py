class ConsultarStatusVideo:
    def __init__(self, video_repository):
        self.video_repository = video_repository

    def execute(self, username, nome_video):
        video = self.video_repository.consultar_status_video(username, nome_video)
        return {"nome_video": video.nome_video, "status": video.status}
