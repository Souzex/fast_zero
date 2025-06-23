import pytest

from fastapi.testclient import TestClient
from src.fast_zero.app_dedezao import app_dedezinho
from http import HTTPStatus

from src.fast_zero.schemas_do_dedezao import UsuarioPublico
from src.fast_zero.modelitos_dede import Usuario

'''
# foi para tests/conftest.py
@pytest.fixture()    
def clientao():
    return TestClient(app_dedezinho)

'''
def testaozao_read_root_deve_retornar_ok_e_ola_mundo(clientao):
    # clientao = TestClient(app_dedezinho)
    resposta = clientao.get('/')
    assert resposta.status_code == HTTPStatus.OK # 200
    assert resposta.json() == {'message':'Olá mundo Webinar'}
    # return None
    
def testaozao_read_root_html_deve_retornar_ok_e_ola_mundo(clientao):
    # clientao = TestClient(app_dedezinho)
    resposta = clientao.get('/em_html')
    assert resposta.status_code == HTTPStatus.OK # 200
    assert resposta.text == """
    <html>
      <head>
        <title>Nosso Olá Mundao de meu deus</title>
      </head>
      <body>
        <h1>Olá mundo Web</h1>
      </body>
    </html> """
    # return None    
   
def testezinho_read_users(clientao):
    # clientao = TestClient(app_dedezinho)
    resposta = clientao.get('/users/')
    assert resposta.status_code == HTTPStatus.OK
    '''
    assert resposta.json() == { 'users': [
        { 'username': 'alice',
          'email': 'alice@souzex.com',
          'id': 1
        },
    ] }
    '''
    assert resposta.json() == {'users': []}
    
def testezinho_read_users_with_only_user(clientao, meu_usuario_de_teste):    

    esquema_usuario = UsuarioPublico.model_validate(meu_usuario_de_teste).model_dump()
    resposta = clientao.get('/users/')
    assert resposta.status_code == HTTPStatus.OK
    assert resposta.json() == {'users': [esquema_usuario]} 
        
'''
def testezinho_create_user(clientao):
    # clientao = TestClient(app_dedezinho)
    resposta = clientao.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@souzex.com',
            'password': '12345',
        },
    )
    assert resposta.status_code == HTTPStatus.CREATED # 201
    assert resposta.json() == {
        'username': 'alice',
        'email': 'alice@souzex.com',
        'id': 1,
    }
'''   
def testezinho_get_user(clientao):
    # clientao = TestClient(app_dedezinho)
    resposta = clientao.get('/users/1')
    assert resposta.status_code == HTTPStatus.OK
    assert resposta.json() == { 
        'username': 'alice',
        'email': 'alice@souzex.com',
        'id': 1
    }
    
def testezinho_update_user(clientao, meu_usuario_de_teste):
    # clientao = TestClient(app_dedezinho)
    resposta = clientao.put(
        '/users/1',
        json={
            'id': 1,
            'username': 'vanderlei',
            'email': 'alice@vanderlei.com',
            'password': '12345'
        },
    )
    assert resposta.status_code == HTTPStatus.OK
    assert resposta.json() == { 
        'username': 'vanderlei',
        'email': 'alice@vanderlei.com',
        'id': 1
    }

def testezinho_delete_user(clientao, meu_usuario_de_teste):
    # clientao = TestClient(app_dedezinho)
    resposta = clientao.delete('/users/1')
    assert resposta.status_code == HTTPStatus.OK
    assert resposta.json() == {'message':'Usuário deletado!'} 