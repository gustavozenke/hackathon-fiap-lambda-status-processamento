from enum import Enum


class StatusProcessamento(Enum):
    PROCESSAMENTO_NAO_INICIADO = "Processamento não iniciado"
    PROCESSAMENTO_INICIADO = "Processamento iniciado"
    PROCESSAMENTO_EM_ANDAMENTO = "Processamento em andamento"
    PROCESSAMENTO_FINALIZADO_SUCESSO = "Processamento finalizado com sucesso"
    PROCESSAMENTO_FINALIZADO_ERRO = "Processamento finalizado com erro"

    @staticmethod
    def converter_para_enum(valor: str):
        for status in StatusProcessamento:
            if status.name == valor:
                return status
        raise ValueError(f"Status processmento invalido: '{valor}'")
