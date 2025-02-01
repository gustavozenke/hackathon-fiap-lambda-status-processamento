class ConsultarStatusVideo:
    def __init__(self, video_repository):
        self.video_repository = video_repository

    def execute(self, nome_usuario):
        return self.video_repository.consultar_status_video(nome_usuario)
