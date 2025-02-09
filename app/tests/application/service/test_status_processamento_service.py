import unittest
from unittest.mock import MagicMock

from application.service.status_processamento_service import StatusProcessamentoService
from domain.entities.video import Video
from domain.enums.status_processamento import StatusProcessamento
from domain.interfaces.status_processamento_repository import StatusProcessamentoRepository


class TestStatusProcessamentoService(unittest.TestCase):

    def setUp(self):
        self.mock_repository = MagicMock(spec=StatusProcessamentoRepository)
        self.service = StatusProcessamentoService(self.mock_repository)

    def test_incluir_evento_processamento(self):
        # Arrange
        video = Video(
            nome_usuario="user1",
            status=StatusProcessamento.PROCESSAMENTO_FINALIZADO_SUCESSO,
            data_hora="2025-02-09T12:00:00Z",
            nome_video="video1",
            url_video="http://teste_unitario.com/video1")

        # Act
        self.service.incluir_evento_processamento(video)

        # Assert
        expected_item = {
            'nome_usuario': "user1",
            'status_processamento': "PROCESSAMENTO_FINALIZADO_SUCESSO",
            'data_hora_inclusao': "2025-02-09T12:00:00Z",
            'nome_video': "video1",
            'url_video': "http://teste_unitario.com/video1"
        }
        self.mock_repository.put_item.assert_called_once_with(expected_item)

    def test_consultar_eventos_usuario(self):
        # Arrange
        nome_usuario = "user1"
        expected_response = {
            'Items': [
                {'nome_video': 'video1', 'status_processamento': 'PROCESSAMENTO_INICIADO'},
                {'nome_video': 'video2', 'status_processamento': 'PROCESSAMENTO_EM_ANDAMENTO'}
            ]
        }
        self.mock_repository.table_query.return_value = expected_response

        # Act
        result = self.service.consultar_eventos_usuario(nome_usuario)

        # Assert
        expected_key_condition = "nome_usuario = :nome"
        expected_expression_attr_values = {":nome": nome_usuario}
        self.mock_repository.table_query.assert_called_once_with(expected_key_condition, expected_expression_attr_values)
        self.assertEqual(result, expected_response['Items'])
