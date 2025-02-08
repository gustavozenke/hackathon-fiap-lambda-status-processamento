from abc import ABC

import boto3

from domain.interfaces.status_processamento_repository_interface import StatusProcessamentoRepositoryInterface


class StatusProcessamentoRepository(StatusProcessamentoRepositoryInterface, ABC):
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table('status_processamento')

    def put_item(self, item: dict) -> None:
        self.table.put_item(Item=item)

    def table_query(self, key_condition: str, expression_attr_values: dict):
        response = self.table.query(
            KeyConditionExpression=key_condition,
            ExpressionAttributeValues=expression_attr_values
        )
        return response.get('Items', [])
