
# Meus super esquemas

from pydantic import BaseModel, EmailStr

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
    
class UsuarioDB(UsuarioEsquema):
    id: int

class UsuarioLista(BaseModel):
    users: list[UsuarioPublico]
    
     
