def somar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero")
    return a / b

if __name__ == "__main__":
    print("EXECUTANDO APLICAÇÃO DENTRO DO CONTÊINER DOCKER")
    print(f" - Resultado da soma (10 + 5): {somar(10, 5)}")
    print(f" - Resultado da multiplicação (4 * 3): {multiplicar(4, 3)}")
    print(f" - Resultado da divisão (20 / 4): {dividir(20, 4)}")
    print("Aplicação executada com SUCESSO")
