# Reto-9

### Punto numero 1

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

### Punto numero 2

- De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).

```Python

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
```

```Python
# Definir la primera funcion para hallar los numeros impares
def numerosimpares(*args) -> int:
    impares = 1
    for num in args:
        impares = num+2
    return impares

# Definir las variables de la funcion
if __name__ == "__main__":
    i = 1

# Definir la condicion del primer bucle
    while(i <= 999):
        print("Numero: " + str(i))
        i += 2

# Definir la segunda funcion para hallar los numeros pares
def numerospares(*args) -> int:
    pares = 1
    for num in args:
        pares = num+2
    return pares

# Definir las variables de la funcion
if __name__ == "__main__":
    i = 2

# Definir la condicion del segundo bucle
    while(i <= 1000):
        print("Numero: " + str(i))
        i += 2

```

```Python
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
```

### Punto numero 3

```Python
# Definimos funcion para calcular la potencia de algun numero entero elevado a otro
def potencia(base, exponente):
  
# Hacemos una serie de condicionales para los distintos casos que se pueden dar
  if exponente == 0:
    return 1
  elif exponente == 1:
    return base
  else:
    return base * potencia(base, exponente - 1)

# Definimos las variables de la funcion
if __name__ == "__main__":
  base = int(input("Ingrese un numero para la base: "))
  exponente = int(input("Ingrese un numero para el exponente: "))
  resultado = potencia(base, exponente)
  print("La potencia de " + str(base) + " elevado a " + str(exponente) + " es: " +str(resultado))
```

### Punto numero 4

- Utilice la siguiente plantilla de code para contar el tiempo:

```Python
import time

start_time = time.time()
# instrucciones sobre las cuales se quiere medir tiempo de ejecución
end_time = time.time()

timer = end_time - start_time
print(timer)
```

Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa. Importante: Revisar este hilo.



### Punto numero 5

- Crear cuenta en stackoverflow y adjuntar imagen en el repo

<a href='https://postimg.cc/MnZLS171' target='_blank'><img src='https://i.postimg.cc/wjDYDV34/Captura-de-pantalla-2024-03-22-a-la-s-20-32-09.png' border='0' alt='Captura-de-pantalla-2024-03-22-a-la-s-20-32-09'/></a>


### Punto numero 6

- Cosas de adultos....ir a linkedin y crear perfil....NO IMPORTA que estén iniciando, si tienen tiempo para redes poco útiles como fb, insta, o tiktok tienen tiempo para crear un perfil mamalón. Dejar enlace en el repo.

<a href='https://postimg.cc/nXkCsf96' target='_blank'><img src='https://i.postimg.cc/5tcvRx4N/Captura-de-pantalla-2024-03-22-a-la-s-20-37-08.png' border='0' alt='Captura-de-pantalla-2024-03-22-a-la-s-20-37-08'/></a>




