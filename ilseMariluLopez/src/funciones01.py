def saludar(nombre: str ) -> str:
    """Funcion devuelve un saludo"""
    return f"Hola como estas {nombre}?"

print(saludar("ilse"))


#Funcion con argumento por default 
def saludo_generico(nombre = "Usuario"):
    return f"Hola {nombre}"

print(saludo_generico("Ilse Marilu"))

#Funcion con argumento kwargs

#Lambda
def suma(num1: int, num2: int) -> int:
    #suma dos numeros 
    return num1 + num2

suma_lambda = lambda n1, n2: n1 + n2

print(suma(2,3))
print(suma_lambda(2,3))

#Map y filter

lista_numeros = [1,2,3,4,5]

tipo_dato = type(map(lambda x: x**2, lista_numeros))

print(f"Tipo dato {tipo_dato}")


cuadrados = list(map(lambda x: x**2, lista_numeros))

print(cuadrados)

#filter
pares = list(filter(lambda x: x % 2 == 0, lista_numeros))
print(pares)
