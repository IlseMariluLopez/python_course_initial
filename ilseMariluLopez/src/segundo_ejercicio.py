def fibonacci(*args) -> list[float]:

    limite = args[0]
    serie = [0, 1]

    while len(serie) < limite:
        siguiente = serie[-1] + serie[-2]
        serie.append(siguiente)

    return serie[:limite]

resultado = fibonacci(10)
print(f"La serie de Fibonacci es: {resultado}")
