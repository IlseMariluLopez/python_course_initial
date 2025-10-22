#yield

def conteo_to_limit(limit: int ):
    """Conteo desde cero hasta el limite"""

    print("Inicio de la funcion tradicional")
    list = []
    for i in range(limit):
        print("En la posición", i) 
        list.append(i)
    print("Finaliza la fucion tradicional")
    return list


def conteo_gen(limit: int):
    print("Inicio de generador")
    for i in range(limit):
        print("En la posicion", i)
        yield i
    print("Fin del generador")

conteo_to_limit(10)
print(type(conteo_gen(10)))


for numero in conteo_to_limit(8):
    print("En tradicional", numero)

for numero in conteo_gen(8):
    print("El generador", numero)