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