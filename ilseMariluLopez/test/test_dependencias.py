from dependencias.di_01 import RepositorioBD, ServicePedidos
from unittest.mock import MagicMock

def test_crear_pedido_llama_a_guardar():
    # Creamos un mock del repositorio
    mock_repo = MagicMock(spec=RepositorioBD)
    
    # Inyectamos el mock en el servicio
    service = ServicePedidos(mock_repo)
    
    # Definimos un pedido de prueba
    pedido_prueba = "hamburguesita"
    
    # Ejecutamos el método a probar
    service.crear_pedido(pedido_prueba)
    
    # Verificamos que 'guardar' fue llamado exactamente una vez con el pedido correcto
    mock_repo.guardar.assert_called_once_with(pedido_prueba)
