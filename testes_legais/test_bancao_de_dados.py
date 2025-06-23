from src.fast_zero.modelitos_dede import Usuario # from src.fast_zero.modelitos_dede import Usuario, tabela_registro
from sqlalchemy import select # from sqlalchemy import create_engine, select
# from sqlalchemy.orm import Session

'''    
def testizinho_create_user():

    # motorzinho = create_engine('sqlite:///banco_de_dados.db')
    motorzinho = create_engine('sqlite:///:memory:') # proprio do sqlite; "banco de dados" volatil, permitindo que o erro de "mapped_column(unique=True)" nao aconteca
    tabela_registro.metadata.create_all(motorzinho)
    # sessao_top = Session(motorzinho)
    with Session(motorzinho) as sessao_top:
        usuario = Usuario(username='dedezao', password='senha123', email='alice@souzex.com')
        sessao_top.add(usuario)
        sessao_top.commit() # Design Pattern: Unit of Work 
        # sessao_top.refresh(usuario) # sincroniza o registro criado no banco com o objeto 'usuario', trazendo valores de colunas criados la no banco, como 'created_at' e 'id'
        resultado = sessao_top.scalar(
            select(Usuario).where(Usuario.email == 'alice@souzex.com')
        )
    assert usuario.username == 'dedezao'
'''
'''
def testizinho_create_user(sessaozona):
    usuario = Usuario(username='dedezao', password='senha123', email='alice@souzex.com')
    sessaozona.add(usuario)
    sessaozona.commit() # Design Pattern: Unit of Work
    resultado = sessaozona.scalar(
        select(Usuario).where(Usuario.email == 'alice@souzex.com')
    )
    assert usuario.username == 'dedezao'
'''