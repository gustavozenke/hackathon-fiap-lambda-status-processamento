class AtualizarStatusVideo:
    def __init__(self, video_repository):
        self.video_repository = video_repository

    def execute(self, username, video_id, status):
        self.video_repository.atualizar_status_video(username, video_id, status)
        return {
            "video_id": video_id,
            "username": username,
            "status": status
        }
