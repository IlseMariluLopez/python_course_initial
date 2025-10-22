from abc import ABC, abstractmethod
from dependency_injector import containers, providers


class IRepositorioBD(ABC):
    @abstractmethod
    def guardar(self, pedido):
        pass

class RepositorioDB(IRepositorioBD):
    def guardar(self, pedido):
        print(f"Pedido {pedido} almacenado exitosamente")

class ApiTercerosAdapter(IRepositorioBD):
    def guardar(self, pedido):
        print(f"Guardado de forma distinta{pedido}")


class ServicePedido:
    def __init__(self, repositorio: IRepositorioBD):
        self.repo = repositorio

    def crear_pedido(self, pedido: str):
        print("Notificacion por mensaje")
        print("Impresion de orden")
        self.repositorio.guardar(pedido)
        print("Notificacion de almacenado")

#Dependency injector with pip package
class Contenedor(containers.DeclarativeContainer):
    repositorio = providers.Singleton(RepositorioDB)
    service = providers.Factory(ServicePedido, repositorio=repositorio)

container = Contenedor()
service_instance = container.service()
service_instance_two = container.service()

service_instance.crear_pedido("Pan de muerto")
service_instance_two.crear_pedido("Pan de muerto")

