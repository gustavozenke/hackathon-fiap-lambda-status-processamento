import os
import sys
import unittest
from unittest.mock import patch, MagicMock, ANY

import boto3

from infraestructure.repositories.status_processamento_repository_impl import StatusProcessamentoRepositoryImpl

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src")))


class TestStatusProcessamentoRepositoryImpl(unittest.TestCase):

    @patch.object(boto3, 'resource')
    def test_put_item(self, mock_boto_resource):
        # Arrange
        mock_dynamodb_resource = MagicMock()
        mock_table = MagicMock()
        mock_boto_resource.return_value = mock_dynamodb_resource
        mock_dynamodb_resource.Table.return_value = mock_table

        repository = StatusProcessamentoRepositoryImpl()

        item = {
            'nome_video': 'video_teste.mp4',
            'nome_usuario': 'usuario_teste',
            'tamanho': 500,
            'formato': 'mp4',
            'data_hora_inclusao': '2025-02-09T10:00:00'
        }

        # Act
        repository.put_item(item)

        # Assert
        mock_table.put_item.assert_called_once_with(Item=item)

    @patch.object(boto3, 'resource')
    def test_table_query_retorna_resultado(self, mock_boto_resource):
        # Arrange
        mock_dynamodb_resource = MagicMock()
        mock_table = MagicMock()
        mock_boto_resource.return_value = mock_dynamodb_resource
        mock_dynamodb_resource.Table.return_value = mock_table


        repository = StatusProcessamentoRepositoryImpl()

        key_condition = "nome_usuario = :nome"
        expression_attr_values = {":nome": "user1"}
        mock_table.query.return_value = {
            'Items': [
                {'nome_video': 'video1', 'status_processamento': 'PROCESSAMENTO_FINALIZADO_SUCESSO'},
                {'nome_video': 'video2', 'status_processamento': 'PROCESSAMENTO_FINALIZADO_SUCESSO'}
            ]
        }

        # Act
        result = repository.table_query(key_condition, expression_attr_values)

        # Assert
        self.assertEqual(result['Items'][0]['nome_video'], 'video1')
        self.assertEqual(result['Items'][1]['nome_video'], 'video2')
