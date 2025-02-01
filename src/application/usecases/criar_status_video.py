from datetime import datetime

from domain.entities.video import Video


class CriarStatusVideo:
    def __init__(self, video_repository):
        self.video_repository = video_repository

    def execute(self, username, video_id):
        video = Video(username, 'PROCESSAMENTO_NAO_INICIADO', datetime.now(), video_id)
        self.video_repository.criar_status_video(video)
        return {
            "video_id": video_id,
            "username": username,
            "status": video.status
        }
