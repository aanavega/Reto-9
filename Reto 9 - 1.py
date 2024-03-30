if __name__ == "__main__":

# Definir variable dentro de la funcion
    i: int = 1

# Definir condicion del bucle
while (i <= 100):

# Definir funcion lambda para hallar el cuadrado del numero
    cuadrado = (lambda i: i**2)(i)
    print("Numero: " + str(i) + " y su cuadrado: " + str(cuadrado))
    i +=1

