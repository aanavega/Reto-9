# Reto-9

### Codigo numero 1

- De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.

```Python
if __name__ == "__main__":

# Definir variable dentro de la funcion
    i: int = 1

# Definir condicion del bucle
while (i <= 100):

# Definir funcion lambda para hallar el cuadrado del numero
    cuadrado = (lambda i: i**2)(i)
    print("Numero: " + str(i) + " y su cuadrado: " + str(cuadrado))
    i +=1
```

```Python
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
```

```Python
if __name__ == "__main__":

# Definir desde que valor se evaluara la condicion
    n: int = 50

# Definir la condicion del bucle con lambda
while n >= 2:
    numerospares = (lambda n: n % 2)(n)
    print (n)
    n -= 2
```
