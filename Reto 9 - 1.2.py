if __name__ == "__main__":
    
# Definir primera variable
    i: int = 1

# Definir condicion del primer bucle con lambda
    while (i <= 999):
        impares = lambda i: i + 2
        print("Numeros impares " +str(i))
        i += 2

# Definir segunda variable
    i: int = 2

# Definir condicion del segundo bucle con lambda
    while (i <= 1000):
        pares = lambda i: i + 2
        print("Numeros pares " + str(i))
        i += 2

