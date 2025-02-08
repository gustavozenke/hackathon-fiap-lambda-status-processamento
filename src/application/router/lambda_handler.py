import json
from datetime import datetime

from domain.entities.video import Video
from domain.enums.status_processamento import StatusProcessamento
from application.service.status_processamento_service import StatusProcessamentoService
from infraestructure.repositories.status_processamento_repository import StatusProcessamentoRepository
from utils.gateway_event import event

status_processamento_repository = StatusProcessamentoRepository()
service = StatusProcessamentoService(status_processamento_repository)


def lambda_handler(event, context):
    if event.get('Records', None):
        return sqs_controller(event)
    elif event.get('resource', None):
        return gateway_controller(event)


def gateway_controller(event):
    http_method = event['httpMethod']
    path = event['path'].split('/')[1]
    nome_usuario = event['path'].split('/')[2]

    if http_method == 'GET' and path == 'status-processamento':
        result = service.consultar_eventos_usuario(nome_usuario)
        return {'statusCode': 200, 'body': json.dumps(result)}

    return {'statusCode': 404, 'body': json.dumps({'message': 'Route not found'})}


def sqs_controller(event):
    body = json.loads(event['Records'][0]['body'])
    nome_usuario = body['nome_usuario']
    nome_video = body['nome_video']
    url_video = body['url_video']
    status_processamento = StatusProcessamento.converter_para_enum(body['status_processamento'])

    video = Video(nome_usuario, status_processamento, str(datetime.now()), nome_video, url_video)

    service.incluir_evento_processamento(video)
    return {'statusCode': 200, 'body': "Success"}


if __name__ == '__main__':
    lambda_handler(event, None)
