from sqlalchemy import create_engine

from sqlalchemy.orm import Session

# from src.fast_zero.configuracoes import ConfiguracoesLegais
from fast_zero.configuracoes import ConfiguracoesLegais

motorzinho = create_engine(ConfiguracoesLegais().DATABASE_URL)

def devolve_sessao(): # pragma: no cover
    # "pragma: no cover" eh para os casos em que nao podemos testar.
    # Nesse caso, eh por causa da substituicao da sessao nos testes, com a instrucao "meu_app.dependency_overrides[meu_get_session] = override_meu_get_session"
    with Session(motorzinho) as sessao_top:
        # return sessao_top
        # Foi trocado "return" por "yield" por causa do "fastapi.Depends" utilizado nas funções de app_dedezao.py
        yield sessao_top

