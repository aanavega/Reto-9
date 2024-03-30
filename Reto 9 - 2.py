# Definir funcion para hallar el cuadrado de los numeros
def cuadradonumeros(*args) -> int:
    cuadrado = 1
    for num in args:
        cuadrado = num**2
    return cuadrado

# Definir las variables de la funcion
if __name__ == "__main__":
    i = 1

# Definir la condicion del bucle
    while(i <= 100):
        print("Numero: " + str(i) + " y su cuadrado: " + str(cuadradonumeros(i)))
    
# Sumarle una unidad a la variable para que continue el bucle
        i += 1