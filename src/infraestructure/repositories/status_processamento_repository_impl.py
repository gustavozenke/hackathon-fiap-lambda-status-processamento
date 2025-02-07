from abc import ABC

import boto3

from domain.entities.video import Video
from domain.interfaces.status_processamento_repository import StatusProcessamentoRepository


class StatusProcessamentoRepositoryImpl(StatusProcessamentoRepository, ABC):
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table('status_processamento')

    def criar_status_video(self, video: Video) -> None:
        self.table.put_item(
            Item={
                'nome_usuario': video.nome_usuario,
                'status_processamento': video.status.name,
                'data_hora_inclusao': video.data_hora_inclusao,
                'nome_video': video.nome_video,
                'url_video': video.url_video
            }
        )

    def consultar_status_video(self, nome_usuario: str):
        response = self.table.query(
            KeyConditionExpression="nome_usuario = :nome",
            ExpressionAttributeValues={":nome": nome_usuario}
        )
        return response.get('Items', [])
