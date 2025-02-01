from abc import ABC

import boto3

from domain.entities.video import Video
from domain.interfaces.video_repository import VideoRepository


class VideoRepositoryImpl(VideoRepository, ABC):
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table('status_processamento')

    def criar_status_video(self, video: Video) -> None:
        self.table.put_item(
            Item={
                'nome_usuario': video.nome_usuario,
                'status_processamento': video.status.name,
                'data_hora_inclusao': video.data_hora_atualizacao_status,
                'nome_video': video.nome_video
            }
        )

    def consultar_status_video(self, nome_usuario: str):
        response = self.table.query(
            KeyConditionExpression="nome_usuario = :nome",
            ExpressionAttributeValues={":nome": nome_usuario}
        )
        return response.get('Items', [])
