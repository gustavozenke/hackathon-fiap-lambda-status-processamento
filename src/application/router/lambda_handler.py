import json

from application.service.video_service import VideoService
from domain.enums.status_processamento import StatusProcessamento
from infraestructure.repositories.video_repository_impl import VideoRepositoryImpl

video_repository = VideoRepositoryImpl()
video_service = VideoService(video_repository)


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
        result = video_service.consultar_status_video(nome_usuario)
        return {'statusCode': 200, 'body': json.dumps(result)}

    return {'statusCode': 404, 'body': json.dumps({'message': 'Route not found'})}


def sqs_controller(event):
    body = json.loads(event['Records'][0]['body'])
    nome_usuario = body['nome_usuario']
    nome_video = body['nome_video']
    status_processamento = StatusProcessamento.converter_para_enum(body['status_processamento'])
    result = video_service.criar_status_video(nome_usuario, status_processamento, nome_video)
    return {'statusCode': 200, 'body': json.dumps(result)}


# if __name__ == '__main__':
#     lambda_handler(event, None)
