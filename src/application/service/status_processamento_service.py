import logging

from domain.entities.video import Video
from domain.interfaces.status_processamento import StatusProcessamento
from domain.interfaces.status_processamento_repository import StatusProcessamentoRepository

logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)


class StatusProcessamentoService(StatusProcessamento):
    def __init__(self, repository: StatusProcessamentoRepository):
        self.repository = repository

    def incluir_evento_processamento(self, video: Video):
        logger.info(f"Incluindo evento de processamento para o video={video}")

        item = {
            'nome_usuario': video.nome_usuario,
            'status_processamento': video.status.name,
            'data_hora_inclusao': video.data_hora_inclusao,
            'nome_video': video.nome_video,
        }

        if video.url_video is not None:
            item['url_video'] = video.url_video

        response = self.repository.put_item(item)
        logger.info(f"Inclusao do evento realizada com sucesso. Response={response}")

    def consultar_eventos_usuario(self, nome_usuario: str):
        logger.info(f"Consultando eventos do usuario {nome_usuario}")

        key_condition = "nome_usuario = :nome"
        expression_attr_values = {
            ":nome": nome_usuario
        }

        response = self.repository.table_query(key_condition, expression_attr_values)
        logger.info(f"Consulta realizada com sucesso. Response={response}")

        return response.get('Items', [])
