
# Meus super esquemas

from pydantic import BaseModel, EmailStr, ConfigDict

class Mensagem(BaseModel):
    message: str
    
class UsuarioEsquema(BaseModel):
    username: str    
    email: EmailStr
    password: str

class UsuarioPublico(BaseModel):
    id: int
    username: str    
    email: EmailStr
    # para uso em fast_zero.testes_legais.test_app_do_dedezao.py, funcao "testezinho_read_users_with_only_user"
    # vai tentar achar os atributos que possuem os mesmos nomes dos atributos do schema UsuarioPublico
    # 'model_config' eh um atributo/funcao/classe do pydantic
    model_config = ConfigDict(from_attributes=True)
 
# Sem uso a partir das últimas alterações da aula 05 no projeto  
# class UsuarioDB(UsuarioEsquema):
#    id: int

class UsuarioLista(BaseModel):
    users: list[UsuarioPublico]
    
     
