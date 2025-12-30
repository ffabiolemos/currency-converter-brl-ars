# Importa a função responsável pela conversão de BRL para ARS
from src.converter import convert_brl_to_ars


def main():
    """
    Função principal do programa.
    Responsável por interagir com o usuário e exibir o resultado da conversão.
    """

    # Solicita ao usuário o valor em reais (BRL)
    # O input retorna uma string, por isso usamos float() para conversão numérica
    amount_brl = float(input("Digite o valor em BRL: "))

    # Chama a função de conversão e obtém o valor em pesos argentinos
    amount_ars = convert_brl_to_ars(amount_brl)

    # Exibe o resultado formatado com duas casas decimais
    print(f"R$ {amount_brl:.2f} equivalem a {amount_ars:.2f} pesos argentinos.")


# Garante que o código só será executado se este arquivo
# for rodado diretamente, e não quando importado como módulo
if __name__ == "__main__":
    main()


