import pytest

from fastapi.testclient import TestClient

from src.fast_zero.app_dedezao import app_dedezinho
# from src.fast_zero.modelitos_dede import tabela_registro
from src.fast_zero.modelitos_dede import tabela_registro, Usuario
from src.fast_zero.coisas_do_banco import devolve_sessao

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

@pytest.fixture()    
# def clientao():
def clientao(sessaozona):    

    print("OOOOOiiiiiiieeeeeeeeeeeeeeeeeeeeee!!!!!!!!!!!!!!!!!!")
    print(sessaozona.__dict__['bind']) # print(sessaozona.__dict__)

    def override_devolve_sessao():
        yield sessaozona # return sessaozona

    # return TestClient(app_dedezinho)
    with TestClient(app_dedezinho) as clientoso:
        app_dedezinho.dependency_overrides[devolve_sessao] = override_devolve_sessao
        yield clientoso

    app_dedezinho.dependency_overrides.clear()  

@pytest.fixture()     
def sessaozona():
    '''
    Valid SQLite URL forms are:
    sqlite:///:memory: (or, sqlite://)
    sqlite:///relative/path/to/file.db
    sqlite:////absolute/path/to/file.db
    '''
    # motorzinho = create_engine('sqlite:///:memory:') # proprio do sqlite; "banco de dados" volatil, permitindo que o erro de "mapped_column(unique=True)" nao aconteca
    motorzinho = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool
    )
    
    tabela_registro.metadata.create_all(motorzinho)
    
    with Session(motorzinho) as sessao_top:
        yield sessao_top
    
    tabela_registro.metadata.drop_all(motorzinho)

@pytest.fixture()     
def meu_usuario_de_teste(sessaozona):
    meu_usuario = Usuario(username='dedezao', password='senha123', email='dedezao@dedezao.com')
    
    sessaozona.add(meu_usuario)
    sessaozona.commit()
    sessaozona.refresh(meu_usuario)
    
    return meu_usuario
