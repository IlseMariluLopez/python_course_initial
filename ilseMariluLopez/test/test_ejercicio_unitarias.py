import requests
from unittest.mock import Mock, MagicMock
from src.ejercicio_unitarias import Cliente, HttpClient

def test_validar_email_succes():
    #Arrange
    email_valido = "ilse@gmail.com"

    #llamada
    cliente_test = Cliente("ilse", email_valido)

    #Assert
    assert cliente_test.validar_email() is True

def test_request_succes(monkeypatch):

    #arragne
    id = 10
    http_mock = Mock(status_code = 200)
    http_mock.json.return_value = {'some' : 'data'}
    monkeypatch.setattr('requests.get', lambda url:http_mock)

    #act
    http_client = HttpClient('http://localhost:80/url/example.com')
    response = http_client.make_request(id)

    #assert
    assert response is not None

