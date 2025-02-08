from domain.entities.video import Video
from domain.interfaces.status_processamento_service_interface import StatusProcessamentoServiceInterface


class StatusProcessamentoService(StatusProcessamentoServiceInterface):
    def __init__(self, repository):
        self.repository = repository

    def incluir_evento_processamento(self, video: Video):
        item = {
            'nome_usuario': video.nome_usuario,
            'status_processamento': video.status.name,
            'data_hora_inclusao': video.data_hora_inclusao,
            'nome_video': video.nome_video,
        }

        if video.url_video is not None:
            item['url_video'] = video.url_video

        self.repository.put_item(item)

    def consultar_eventos_usuario(self, nome_usuario: str):
        key_condition = "nome_usuario = :nome"
        expression_attr_values = {
            ":nome": nome_usuario
        }

        return self.repository.table_query(key_condition, expression_attr_values)
