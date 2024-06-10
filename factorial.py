#Función para calcular el factorial de un número.
numero=int(input())
def factorial(numero):
    if numero < 0:
        return "NO definido"
    resultado=1
    for i in range (1,numero+1):
        resultado *= i
    return resultado
print(f"{factorial(numero)}")
