# Importa a função responsável por carregar as taxas de câmbio
# a partir do arquivo JSON
from src.utils import load_exchange_rates


def convert_brl_to_ars(amount_brl):
    """
    Converte um valor em Real Brasileiro (BRL) para Peso Argentino (ARS).

    Parâmetros:
    amount_brl (float): Valor em reais a ser convertido.

    Retorna:
    float: Valor convertido para pesos argentinos.
    """

    # Carrega as taxas de câmbio do arquivo JSON
    rates = load_exchange_rates()

    # Obtém a taxa de conversão específica de BRL para ARS
    rate = rates.get("BRL_ARS")

    # Valida se a taxa existe no arquivo
    # Caso não exista, lança um erro para evitar cálculos incorretos
    if rate is None:
        raise ValueError("Taxa BRL_ARS não encontrada.")

    # Realiza a conversão multiplicando o valor em reais pela taxa
    amount_ars = amount_brl * rate

    # Retorna o valor convertido
    return amount_ars

