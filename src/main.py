from src.converter import convert_brl_to_ars


def main():
    amount_brl = float(input("Digite o valor em BRL: "))
    amount_ars = convert_brl_to_ars(amount_brl)

    print(f"R$ {amount_brl:.2f} equivalem a {amount_ars:.2f} pesos argentinos.")


if __name__ == "__main__":
    main()

