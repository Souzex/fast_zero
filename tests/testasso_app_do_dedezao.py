from fastapi.testclient import TestClient
from src.fast_zero.app_dedezao import app_dedezinho
from http import HTTPStatus

def testaozao_read_root_deve_retornar_ok_e_ola_mundo():
    clientao = TestClient(app_dedezinho)
    response = clientao.get('/')
    assert response.status_code == HTTPStatus.OK # 200
    assert response.json() == {'message':'Olá mundo Webinar'}
    # return None