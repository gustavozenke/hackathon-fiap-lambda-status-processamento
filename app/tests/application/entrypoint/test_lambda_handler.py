import json
import os
import sys
import unittest
from unittest.mock import patch, Mock

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src")))


from infraestructure.repositories.status_processamento_repository_impl import StatusProcessamentoRepositoryImpl
from application.service.status_processamento_service import StatusProcessamentoService
from src.application.entrypoint.lambda_handler import lambda_handler


class TestLambdaFunctions(unittest.TestCase):

    @patch.object(StatusProcessamentoRepositoryImpl, '__init__')
    @patch.object(StatusProcessamentoService, 'incluir_evento_processamento')
    def test_lambda_handler_sqs_event(self, mock_processaamento, mock_repository):
        # Arrange
        event = {
            'Records': [
                {
                    'body': json.dumps({
                        'nome_usuario': 'user1',
                        'nome_video': 'video1',
                        'url_video': 'http://example.com/video1',
                        'status_processamento': 'PROCESSAMENTO_FINALIZADO_SUCESSO'
                    })
                }
            ]
        }
        mock_repository.return_value = None
        mock_processaamento.return_value = None

        # Act
        result = lambda_handler(event, None)

        # Assert
        self.assertEqual(result, {'statusCode': 200, 'body': 'Success'})

    # @patch.object(boto3, 'resource')
    # @patch.object(StatusProcessamentoService, 'consultar_eventos_usuario')
    # @patch('application.entrypoint.lambda_handler.gateway_controller')
    # def test_lambda_handler_gateway_event(self, mock_gateway, mock_processamento, mock_boto):
    #     # Arrange
    #     event = {
    #         'httpMethod': 'GET',
    #         'path': '/status-processamento/user1'
    #     }
    #     mock_processamento.return_value = None
    #     mock_boto.return_value = Mock()
    #     mock_gateway.return_value = {'statusCode': 200, 'body': json.dumps({'status': 'ok'})}
    #
    #     # Act
    #     result = lambda_handler(event, None)
    #
    #     # Asserts
    #     self.assertEqual(result, None)
    #
    # @patch.object(StatusProcessamentoService, 'consultar_eventos_usuario')
    # def test_gateway_controller_get_status(self, mock_processamento):
    #     # Arrange
    #     event = {
    #         'httpMethod': 'GET',
    #         'path': '/status-processamento/user1'
    #     }
    #     mock_processamento.return_value = {'status': 'ok'}
    #
    #     # Act
    #     result = gateway_controller(event)
    #
    #     # Asserts
    #     self.assertEqual(result, {'statusCode': 200, 'body': json.dumps({'status': 'ok'})})
    #
    # @patch.object(boto3, 'resource')
    # def test_gateway_controller_rota_invalida(self, mock_boto):
    #     # Arrange
    #     event = {
    #         'httpMethod': 'POST',
    #         'path': '/status-processamento/user1'
    #     }
    #     mock_boto.return_value = Mock()
    #
    #     # Act
    #     result = gateway_controller(event)
    #
    #     # Assert
    #     self.assertEqual(result, {'statusCode': 404, 'body': json.dumps({'message': 'Rota nao encontrada'})})
    #
    # @patch.object(boto3, 'resource')
    # @patch.object(StatusProcessamentoService, 'incluir_evento_processamento')
    # def test_sqs_controller(self, mock_processamento, mock_boto):
    #     # Arrange
    #     event = {
    #         'Records': [
    #             {
    #                 'body': json.dumps({
    #                     'nome_usuario': 'user1',
    #                     'nome_video': 'video1',
    #                     'url_video': 'http://example.com/video1',
    #                     'status_processamento': 'PROCESSAMENTO_FINALIZADO_SUCESSO'
    #                 })
    #             }
    #         ]
    #     }
    #     mock_processamento.return_value = None
    #     mock_boto.return_value = Mock()
    #
    #     # Act
    #     result = sqs_controller(event)
    #
    #     # Asserts
    #     self.assertEqual(result, {'statusCode': 200, 'body': 'Success'})
