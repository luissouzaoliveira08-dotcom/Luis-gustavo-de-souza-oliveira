def eh_primo(numero):
    """Retorna True se o número for primo, e False caso contrário."""
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False  # Elimina os pares logo de cara

    # Testa os divisores ímpares até a raiz quadrada do número
    # (Matematicamente, se não houver divisor até aqui, não haverá depois)
    limite = int(numero ** 0.5) + 1
    for i in range(3, limite, 2):
        if numero % i == 0:
            return False
    return True


def listar_primos_ate(limite):
    """Retorna uma lista com todos os números primos até o limite estipulado."""
    primos = []
    for num in range(2, limite + 1):
        if eh_primo(num):
            primos.append(num)
    return primos


# --- Bloco de Execução ---
# Este bloco roda automaticamente quando você executa o arquivo no VS Code
if __name__ == "__main__":
    print("-" * 40)
    print("   GERADOR DE NÚMEROS PRIMOS ")
    print("-" * 40)

    try:
        limite_usuario = int(
            input("Digite até qual número você quer buscar primos: ")
        )

        if limite_usuario < 2:
            print("Não existem números primos menores que 2.")
        else:
            resultado = listar_primos_ate(limite_usuario)
            print(f"\nNúmeros primos encontrados até {limite_usuario}:")
            print(resultado)
            print(f"Total de números primos encontrados: {len(resultado)}")

    except ValueError:
        print("Por favor, digite um número inteiro válido.")