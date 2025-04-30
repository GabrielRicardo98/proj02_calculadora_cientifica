import math

# Funções matemáticas
def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        raise ValueError("Não é possível dividir por zero.")
    return x / y

def potencia(x, y):
    return x ** y

def radiciacao(x):
    if x < 0:
        raise ValueError("Não é possível calcular a raiz de um número negativo.")
    return math.sqrt(x)

def seno(x):
    return math.sin(math.radians(x))

def cosseno(x):
    return math.cos(math.radians(x))

def tangente(x):
    return math.tan(math.radians(x))

def logaritmo(x, base):
    if x <= 0 or base <= 0 or base == 1:
        raise ValueError("Logaritmo inválido. Número e base devem ser positivos e a base diferente de 1.")
    return math.log(x, base)

# Menu de operações
def mostrar_menu():
    print("\n=== CALCULADORA CIENTÍFICA ===")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potenciação")
    print("6. Radiciação")
    print("7. Seno")
    print("8. Cosseno")
    print("9. Tangente")
    print("10. Logaritmo")
    print("0. Sair")

# Loop principal
def main():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        try:
            if escolha == "0":
                print("Encerrando a calculadora.")
                break

            elif escolha in ["1", "2", "3", "4", "5"]:
                x = float(input("Digite o primeiro número: "))
                y = float(input("Digite o segundo número: "))

                if escolha == "1":
                    print("Resultado:", adicionar(x, y))
                elif escolha == "2":
                    print("Resultado:", subtrair(x, y))
                elif escolha == "3":
                    print("Resultado:", multiplicar(x, y))
                elif escolha == "4":
                    print("Resultado:", dividir(x, y))
                elif escolha == "5":
                    print("Resultado:", potencia(x, y))

            elif escolha == "6":
                x = float(input("Digite o número: "))
                print("Resultado:", radiciacao(x))

            elif escolha == "7":
                x = float(input("Digite o ângulo em graus: "))
                print("Resultado (seno):", seno(x))

            elif escolha == "8":
                x = float(input("Digite o ângulo em graus: "))
                print("Resultado (cosseno):", cosseno(x))

            elif escolha == "9":
                x = float(input("Digite o ângulo em graus: "))
                print("Resultado (tangente):", tangente(x))

            elif escolha == "10":
                x = float(input("Digite o número: "))
                base = float(input("Digite a base do logaritmo: "))
                print("Resultado:", logaritmo(x, base))

            else:
                print("Opção inválida. Tente novamente.")

        except ValueError as e:
            print("Erro:", e)
        except Exception as e:
            print("Erro inesperado:", e)

if __name__ == "__main__":
    main()
