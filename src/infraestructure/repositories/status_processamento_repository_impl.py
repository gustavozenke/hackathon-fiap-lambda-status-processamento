import boto3

from domain.interfaces.status_processamento_repository import StatusProcessamentoRepository


class StatusProcessamentoRepositoryImpl(StatusProcessamentoRepository):
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table('status_processamento')

    def put_item(self, item: dict) -> None:
        return self.table.put_item(Item=item)

    def table_query(self, key_condition: str, expression_attr_values: dict):
        return self.table.query(
            KeyConditionExpression=key_condition,
            ExpressionAttributeValues=expression_attr_values
        )
