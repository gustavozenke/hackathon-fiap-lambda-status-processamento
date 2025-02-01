from abc import ABC
from typing import Optional

import boto3

from domain.entities.video import Video
from domain.interfaces.video_repository import VideoRepository


class VideoRepositoryImpl(VideoRepository, ABC):
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table('status-processamento')

    def criar_status_video(self, video: Video) -> None:
        self.table.put_item(
            Item={
                'username': video.nome_video,
                'status': video.status,
                'data_hora_atualizacao_status': video.data_hora_atualizacao_status,
                'nome_video': video.nome_video
            }
        )

    def consultar_status_video(self, username: str, nome_video: str) -> Optional[Video]:
        response = self.table.get_item(Key={'video_id': nome_video})
        item = response.get('Item')
        if item:
            return Video(item['username'], item['status'], item['data_hora_atualizacao_status'],  item['nome_video'])
        return None

    def atualizar_status_video(self, username: str, nome_video: str, status: str) -> None:
        self.table.update_item(
            Key={'username': username},
            UpdateExpression='SET status = :status',
            ExpressionAttributeValues={':status': status}
        )
