def pascal_triangle(num_lines):
    """
    Função para gerar o Triângulo de Pascal até a num_lines-ésima linha.
    """
    triangle = []
    for i in range(num_lines):  # Ajuste para incluir a linha num_lines
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle

def combination(n, k):
    """
    Função para calcular a combinação C(n, k).
    """
    if k == 0 or k == n:
        return 1
    if k > n:
        return 0  # Caso k seja maior que n, a combinação é zero
    return combination(n-1, k-1) + combination(n-1, k)

def main():
    """
    Função principal para gerar o Triângulo de Pascal e mostrar a combinação C(n, k).
    """
    num_lines = int(input("Digite o número de linhas do Triângulo de Pascal: "))
    n = int(input("Digite o valor de n (linha para a combinação): "))
    k = int(input("Digite o valor de k (coluna para a combinação): "))

    # Verificar se é possível calcular C(n, k)
    if k > n:
        print(f"Não é possível calcular C({n}, {k}) porque k ({k}) é maior que n ({n}).")
    elif n >= num_lines:
        print(f"Não é possível calcular C({n}, {k}) porque n ({n}) deve ser menor que o número de linhas ({num_lines}).")
    else:
        # Gerar o Triângulo de Pascal
        triangle = pascal_triangle(num_lines)

        # Mostrar o Triângulo de Pascal
        print("\nTriângulo de Pascal até a linha", num_lines)
        for row in triangle:
            print(row)

        # Calcular a combinação C(n, k)
        comb = combination(n, k)
        print(f"\nA combinação C({n}, {k}) é: {comb}")

        # Mostrar onde está a combinação no Triângulo de Pascal
        print(f"O valor {comb} está localizado na linha {n} e coluna {k} do Triângulo de Pascal.")

if __name__ == "__main__":
    main()
