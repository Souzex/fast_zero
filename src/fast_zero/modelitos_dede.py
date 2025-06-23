from sqlalchemy.orm import registry, Mapped, mapped_column
from sqlalchemy import func
from datetime import datetime

tabela_registro = registry()

@tabela_registro.mapped_as_dataclass
class Usuario:
    __tablename__ = 'usuario'
    id: Mapped[int] = mapped_column(init=False, primary_key=True) # primary_key faz AUTO INCREMENT por padrao; init gera automaticamente o valor de 'id'; init nao eh obrigatorio quando usado com primary_key
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now()) # o 'now' é do servidor do banco de dados
    # updated_at: Mapped[datetime] = mapped_column(init=False, onupdate=func.now()) # o 'now' é do servidor do banco de dados
    
    
    