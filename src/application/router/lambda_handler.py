import json

from application.service.video_service import VideoService
from domain.enums.status_processamento import StatusProcessamento
from infraestructure.repositories.video_repository_impl import VideoRepositoryImpl

video_repository = VideoRepositoryImpl()
video_service = VideoService(video_repository)


def lambda_handler(event, context):

    try:
        http_method = event['httpMethod']
        path = event['resource']
        body = event['body']
        nome_usuario = body['nome_usuario']
        nome_video = body['nome_video']
        status_processamento = StatusProcessamento.converter_para_enum(body['status_processamento'])

        if http_method == 'POST' and path == '/videos':
            result = video_service.criar_status_video(nome_usuario, status_processamento, nome_video)
            return {'statusCode': 200, 'body': json.dumps(result)}

        elif http_method == 'GET' and path == '/videos/{nome_video}':
            result = video_service.consultar_status_video(nome_usuario)
            return {'statusCode': 200, 'body': json.dumps(result)}

        return {'statusCode': 404, 'body': json.dumps({'message': 'Route not found'})}
    except ValueError as error:
        return {'statusCode': 400, 'body': json.dumps({'message': f'Evento invalido. Erro: {error.args}'})}


if __name__ == '__main__':
    event = {
        "httpMethod": "POST",
        "resource": "/videos",
        "body": {
            "nome_usuario": "usuario teste",
            "nome_video": "video teste",
            "status_processamento": "PROCESSAMENTO_NAO_INICIADO"
        }
    }
    lambda_handler(event, None)
