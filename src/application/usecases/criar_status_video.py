from datetime import datetime

from domain.entities.video import Video


class CriarStatusVideo:
    def __init__(self, video_repository):
        self.video_repository = video_repository

    def execute(self, username, status_processamento, nome_video):
        video = Video(username, status_processamento, str(datetime.now()), nome_video)
        self.video_repository.criar_status_video(video)
        return {
            "nome_video": nome_video,
            "username": username,
            "status": video.status
        }
