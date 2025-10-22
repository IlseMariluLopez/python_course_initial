import time

#print("Time", time.time())
#sum([i**2 for i in range(100000)])
#print("Time", time.time())


def decorador(func):
    def envoltura():
        print("Iicio")
        func()
        print("Final")
    return envoltura

def decorador_tiempo_calc(func):
    def wrapper(*args):
        inicio = time.time()
        

@decorador
def saludo():
    print("Hola mundo")


saludo()

#funcion_decorada = decorador(saludo)
#funcion_decorada()


