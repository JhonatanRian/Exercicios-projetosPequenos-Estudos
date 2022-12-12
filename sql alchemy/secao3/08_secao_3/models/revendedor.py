import sqlalchemy as sa

from datetime import datetime

from models.model_base import ModelBase


class Revendedor(ModelBase):
    __tablename__: str = 'revendedores'

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    
    nome: str = sa.Column(sa.String(45), unique=True, nullable=False)
    razao_social: str = sa.Column(sa.String(100), nullable=False)
    contato: str = sa.Column(sa.String(100), nullable=False)

    def __repr__(self) -> str:
        return f'<Revendedor: {self.nome}>'

