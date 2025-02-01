import json

from application.service.video_service import VideoService
from infraestructure.repositories.video_repository_impl import VideoRepositoryImpl

video_repository = VideoRepositoryImpl()
video_service = VideoService(video_repository)


def lambda_handler(event, context):
    http_method = event['httpMethod']
    path = event['resource']
    body = event['body']

    if http_method == 'POST' and path == '/videos':
        username = body['username']
        nome_video = body['nome_video']
        result = video_service.criar_status_video(username, nome_video)
        return {'statusCode': 200, 'body': json.dumps(result)}

    elif http_method == 'GET' and path == '/videos/{nome_video}':
        nome_video = body['nome_video']
        result = video_service.consultar_status_video(nome_video)
        return {'statusCode': 200, 'body': json.dumps(result)}

    elif http_method == 'PUT' and path == '/videos/{nome_video}/status':
        username = body['username']
        nome_video = body['nome_video']
        status = body['status']
        result = video_service.atualizar_status_video(username, nome_video, status)
        return {'statusCode': 200, 'body': json.dumps(result)}

    return {'statusCode': 404, 'body': json.dumps({'message': 'Route not found'})}


if __name__ == '__main__':
    event = {
        "httpMethod": "POST",
        "resource": "/videos",
        "body": {
            "username": "usuario teste",
            "nome_video": "video teste"
        }
    }
    lambda_handler(event, None)
