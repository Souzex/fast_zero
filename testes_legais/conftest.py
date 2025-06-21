import pytest

from fastapi.testclient import TestClient

from src.fast_zero.app_dedezao import app_dedezinho

from sqlalchemy import create_engine

from src.fast_zero.modelitos_dede import tabela_registro

from sqlalchemy.orm import Session

@pytest.fixture()    
def clientao():
    return TestClient(app_dedezinho)
    
@pytest.fixture()     
def sessaozona():

'''
Valid SQLite URL forms are:
 sqlite:///:memory: (or, sqlite://)
 sqlite:///relative/path/to/file.db
 sqlite:////absolute/path/to/file.db
'''

    motorzinho = create_engine('sqlite:///:memory:') # proprio do sqlite; "banco de dados" volatil, permitindo que o erro de "mapped_column(unique=True)" nao aconteca
    tabela_registro.metadata.create_all(motorzinho)
    
    with Session(motorzinho) as sessao_top:
        yield sessao_top
    
    tabela_registro.metadata.drop_all(motorzinho)

''' 
   # aparentemente funciona como acima       
    motorzinho = create_engine('sqlite:///banco_de_dados.db')
    tabela_registro.metadata.create_all(motorzinho)
    
    with Session(motorzinho) as sessao_top:
        yield sessao_top
        tabela_registro.metadata.drop_all(motorzinho)
'''