#arg

#Argumentos poscionales
def procesar_datos(*args) -> None:
    """ecibe elemntos posicionales"""
    print(f"Argumentos: {args}")

procesar_datos(10,50,5,2,7,8,9)   

#Keyword arguments 
def procesar_datos_kw(**kwargs) -> None:
    """ecibe elemntos posicionales"""
    print(f"Argumentos: {kwargs}")

procesar_datos_kw(nombre= "Ilse", status="True")