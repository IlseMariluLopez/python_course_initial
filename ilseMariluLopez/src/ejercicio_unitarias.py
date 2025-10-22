import request


class Cliente:
    def __init__(self, nombre: str, correo:str):
        self.nombre = nombre
        self.correo = correo

    def validar_email(self) -> bool:
        return "@" in self.correo and "." in self .correo
    
class HttpClient:
    def __init__(self, url):
        self.url = url

    def request(self, id):
        response = request.get(f"{self.url}/{id}")

http = HttpClient("http://localhost:80/url/example.com")


        
    
client = Cliente("ilse","correo@gmail.com")
print(client.validar_email())