# Definir funcion para hallar los numeros pares descendientes
def numerospares(*args) -> int:
    pares = 1
    for num in args:
        pares = num-2
    return pares

# Definir las variables de la funcion
if __name__ == "__main__":
    n = 50

# Definir la condicion del bucle
    while (n >= 2):
        if n % 2 == 0:
            n-=2
            print(str(n))

# Establecer un fin al bucle
        if n == 2: break






