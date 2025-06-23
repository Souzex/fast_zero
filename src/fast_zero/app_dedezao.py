from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import HTMLResponse

from http import HTTPStatus

from fast_zero.schemas_do_dedezao import Mensagem, UsuarioEsquema, UsuarioPublico, UsuarioLista #, UsuarioDB

# from sqlalchemy import create_engine, select
from sqlalchemy import select

from sqlalchemy.orm import Session

# from src.fast_zero.configuracoes import ConfiguracoesLegais
# from fast_zero.configuracoes import ConfiguracoesLegais

# from src.fast_zero.modelitos_dede import Usuario
from fast_zero.modelitos_dede import Usuario

from fast_zero.coisas_do_banco import devolve_sessao

app_dedezinho = FastAPI()

# Sem uso a partir das últimas alterações da aula 05 no projeto
# database = []

@app_dedezinho.get('/', status_code=HTTPStatus.OK, response_model=Mensagem)
# @app_dedezinho.get('/')
def read_root_web():
    return {'message':'Olá mundo Web'}

'''
# para testar o contrato (http://localhost:8000/ e http://localhost:8000/docs)
@app_dedezinho.get('/', status_code=HTTPStatus.OK, response_model=Mensagem)
# @app_dedezinho.get('/')
def read_root_web():
    return {} # Internal Server Error
#   return {'message':'Olá mundo Web', 'batata':'frita'} # Nao ocorre erro, apenas despreza 'batata'
'''

'''
def read_root():
    return {'message':'Olá mundo'}
'''


@app_dedezinho.get('/em_html', response_class=HTMLResponse)
def read_root_web_html():
    return """
    <html>
      <head>
        <title>Nosso Olá Mundo</title>
      </head>
      <body>
        <h1>Olá mundo Web</h1>
      </body>
    </html> """

@app_dedezinho.post('/users/', status_code=HTTPStatus.CREATED, response_model=UsuarioPublico)
# def create_user(usuario: UsuarioEsquema):
def create_user(
    usuario: UsuarioEsquema, 
    sessao_top: Session = Depends(devolve_sessao)
):

    # sessao_top = devolve_sessao()

    usuario_banco = sessao_top.scalar(
        select(Usuario).where( 
            (Usuario.username == usuario.username) | (Usuario.email == usuario.email)
        )
    )
        
    if usuario_banco:
        if usuario_banco.username == usuario.username:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Usuário já existe'
            )
        elif usuario_banco.email == usuario.email:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='E-mail já existe'
            )
        
    usuario_banco = Usuario(username=usuario.username, email=usuario.email, password=usuario.password)
    sessao_top.add(usuario_banco)
    sessao_top.commit()
    sessao_top.refresh(usuario_banco)
        
    return usuario_banco

'''    
    motorzinho = create_engine(ConfiguracoesLegais().DATABASE_URL)
    with Session(motorzinho) as sessao_top:
        usuario_banco = sessao_top.scalar(
            select(Usuario).where( 
                (Usuario.username == usuario.username) | (Usuario.email == usuario.email)
            )
        )
        
        if usuario_banco:
            if usuario_banco.username == usuario.username:
                raise HTTPException(
                    status_code=HTTPStatus.BAD_REQUEST,
                    detail='Usuário já existe'
                )
            elif usuario_banco.email == usuario.email:
                raise HTTPException(
                    status_code=HTTPStatus.BAD_REQUEST,
                    detail='E-mail já existe'
                )
        usuario_banco = Usuario(username=usuario.username, email=usuario.email, password=usuario.password)
        sessao_top.add(usuario_banco)
        sessao_top.commit()
        sessao_top.refresh(usuario_banco)
        
    return usuario_banco
'''    
      
'''
# breakpoint()
# Apenas para observar as estrtuuras de dados    
# usuario = UsuarioEsquema(username='andre', email='andre@souzex.com', password='12345')
# usuario.model_dump() = {'username': 'andre', 'email': 'andre@souzex.com', 'password': '12345'}
# **usuario.model_dump() = "username='andre', email='andre@souzex.com', password='12345'"
    user_with_id = UsuarioDB(
        id=len(database) + 1,
        **usuario.model_dump()
    )
    
    database.append(user_with_id)
    
    return user_with_id
'''

@app_dedezinho.get('/users/', response_model=UsuarioLista)
def read_users(
    limite_usuarios: int = 100, # http://localhost:1900/users/?limite_usuarios=10
    meu_offset: int = 0,
    sessao_top: Session = Depends(devolve_sessao)
):
    
    usuarios = sessao_top.scalars(
        select(Usuario).limit(limite_usuarios).offset(meu_offset)
    )
    
    # return {'users': database}
    return {'users': usuarios}

@app_dedezinho.put('/users/{usuario_id}', response_model=UsuarioPublico)
def update_user(
    usuario_id: int, 
    usuario: UsuarioEsquema,
    sessao_top: Session = Depends(devolve_sessao)
):
    
    # sessao_top.get(Usuario, usuario_id)    
    usuario_banco = sessao_top.scalar(
        select(Usuario).where(Usuario.id == usuario_id)
    )
    
    if not usuario_banco:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail = "Nao achou nada") # HTTP 404
    
    usuario_banco.username = usuario.username
    usuario_banco.password = usuario.password
    usuario_banco.email    = usuario.email
    
    sessao_top.add(usuario_banco)
    sessao_top.commit()
    sessao_top.refresh(usuario_banco)
    
    return usuario_banco
    
    '''
    if usuario_id < 1 or usuario_id > len(database):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail = "Nao achou nada") # HTTP 404
    
    user_with_id = UsuarioDB(
        id=usuario_id,
        **usuario.model_dump()
    )
    database[usuario_id - 1] = user_with_id
    
    return user_with_id
    '''

# @app_dedezinho.delete('/users/{usuario_id}', response_model=UsuarioPublico)
@app_dedezinho.delete('/users/{usuario_id}', response_model=Mensagem)
def delete_user(
    usuario_id: int,
    sessao_top: Session = Depends(devolve_sessao)
):
    # sessao_top.get(Usuario, usuario_id)    
    usuario_banco = sessao_top.scalar(
        select(Usuario).where(Usuario.id == usuario_id)
    )
    
    if not usuario_banco:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail = "Nao achou nada") # HTTP 404
    
    sessao_top.delete(usuario_banco)
    sessao_top.commit()
    
    return {'message':'Usuário deletado!'}
    '''
    if usuario_id < 1 or usuario_id > len(database):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail = "Nao achou nada") # HTTP 404
    
    # user_with_id = database[usuario_id - 1]
    del database[usuario_id - 1]
    
    # return user_with_id
    return {'message':'Usuário deletado!'}
    '''
    
@app_dedezinho.get('/users/{usuario_id}', response_model=UsuarioPublico)
def get_user(usuario_id: int):
    
    if usuario_id < 1 or usuario_id > len(database):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail = "Nao achou nada") # HTTP 404
    
    user_with_id = database[usuario_id - 1]
    
    return user_with_id    