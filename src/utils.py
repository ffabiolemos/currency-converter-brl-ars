import json
from pathlib import Path


def load_exchange_rates():
    """
    Carrega as taxas de câmbio a partir do arquivo JSON.
    Retorna um dicionário com as taxas.
    """
    base_path = Path(__file__).resolve().parent.parent
    data_path = base_path / "data" / "exchange_rates.json"

    try:
        with open(data_path, "r", encoding="utf-8") as file:
            exchange_rates = json.load(file)
        return exchange_rates

    except FileNotFoundError:
        raise FileNotFoundError(
            "Arquivo exchange_rates.json não encontrado na pasta data."
        )

    except json.JSONDecodeError:
        raise ValueError(
            "Erro ao ler o arquivo JSON. Verifique a estrutura do exchange_rates.json."
        )
