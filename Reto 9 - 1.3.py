if __name__ == "__main__":
# Definir desde que valor se evaluara la condicion
    n: int = 50

# Definir la condicion del bucle con lambda
while n >= 2:
    if n % 2 == 0:
        pares = lambda n: n - 2
        n -= 2
        print(str(n))
    if n == 2: break
