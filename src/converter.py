from src.utils import load_exchange_rates


def convert_brl_to_ars(amount_brl):
    rates = load_exchange_rates()

    rate = rates.get("BRL_ARS")
    if rate is None:
        raise ValueError("Taxa BRL_ARS não encontrada.")

    amount_ars = amount_brl * rate
    return amount_ars
