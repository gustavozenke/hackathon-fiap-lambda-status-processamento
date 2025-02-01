class AtualizarStatusVideo:
    def __init__(self, video_repository):
        self.video_repository = video_repository

    def execute(self, username, nome_video, status):
        self.video_repository.atualizar_status_video(username, nome_video, status)
        return {
            "nome_video": nome_video,
            "username": username,
            "status": status
        }
