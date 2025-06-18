from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from http import HTTPStatus

from fast_zero.schemas_do_dedezao import Mensagem, UsuarioEsquema, UsuarioPublico, UsuarioDB, UsuarioLista

app_dedezinho = FastAPI()

database = []

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
def create_user(usuario: UsuarioEsquema):
    
#   breakpoint()
    
# usuario = UsuarioEsquema(username='andre', email='andre@souzex.com', password='12345')
# usuario.model_dump() = {'username': 'andre', 'email': 'andre@souzex.com', 'password': '12345'}
# **usuario.model_dump() = "username='andre', email='andre@souzex.com', password='12345'"
    user_with_id = UsuarioDB(
        id=len(database) + 1,
        **usuario.model_dump()
    )
    
    database.append(user_with_id)
    
    return user_with_id

@app_dedezinho.get('/users/', response_model=UsuarioLista)
def read_users():
    return {'users': database}

@app_dedezinho.put('/users/{usuario_id}', response_model=UsuarioPublico)
def update_user(usuario_id: int, usuario: UsuarioEsquema):
    
    if usuario_id < 1 or usuario_id > len(database):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail = "Nao achou nada") # HTTP 404
    
    user_with_id = UsuarioDB(
        id=usuario_id,
        **usuario.model_dump()
    )
    database[usuario_id - 1] = user_with_id
    
    return user_with_id

# @app_dedezinho.delete('/users/{usuario_id}', response_model=UsuarioPublico)
@app_dedezinho.delete('/users/{usuario_id}', response_model=Mensagem)
def delete_user(usuario_id: int):
    
    if usuario_id < 1 or usuario_id > len(database):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail = "Nao achou nada") # HTTP 404
    
    # user_with_id = database[usuario_id - 1]
    del database[usuario_id - 1]
    
    # return user_with_id
    return {'message':'Usuário deletado!'}
    
@app_dedezinho.get('/users/{usuario_id}', response_model=UsuarioPublico)
def get_user(usuario_id: int):
    
    if usuario_id < 1 or usuario_id > len(database):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail = "Nao achou nada") # HTTP 404
    
    user_with_id = database[usuario_id - 1]
    
    return user_with_id    