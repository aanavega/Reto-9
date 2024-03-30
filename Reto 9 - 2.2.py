def numerosimpares(*args) -> int:
    impares = 1
    for num in args:
        impares = num+2
    return impares

if __name__ == "__main__":
    i = 1
    while(i <= 999):
        print("Numero: " + str(i))
        i += 2

def numerospares(*args) -> int:
    pares = 1
    for num in args:
        pares = num+2
    return pares

if __name__ == "__main__":
    i = 2
    while(i <= 1000):
        print("Numero: " + str(i))
        i += 2