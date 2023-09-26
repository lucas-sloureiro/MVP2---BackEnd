from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base, Comentario


class Doc(Base):
    __tablename__ = 'doc'

    id = Column("pk_doc", Integer, primary_key=True)
    doc_num = Column(String(140))
    descricao = Column(String(140))
    moeda_ori = Column(String(140))
    valor_ori = Column(Float)
    taxa = Column(Float)
    valor_brl = Column(Float)
    data_insercao = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o doc e o comentário.
    # Essa relação é implicita, não está salva na tabela 'doc',
    # mas aqui estou deixando para SQLAlchemy a responsabilidade
    # de reconstruir esse relacionamento.
    comentarios = relationship("Comentario")

    def __init__(self, doc_num:str, descricao:str, moeda_ori:str,
                 valor_ori:float, taxa:float, valor_brl:float,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Doc

        Arguments:
            doc_num: ref ao documento lançado.
            descricao: detalhe do doc.
            moeda_ori: moeda do doc.
            valor_ori: valor do documento.
            taxa: taxa de conversão para BRL.
            valor_brl: Valor convertido para BRL.
            data_insercao: Data de quando o doc foi inserido à base.
        """
        self.doc_num = doc_num
        self.descricao = descricao
        self.moeda_ori = moeda_ori
        self.valor_ori = valor_ori
        self.taxa = taxa
        self.valor_brl = valor_brl
        
       
        # Se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

    def adiciona_comentario(self, comentario:Comentario):
        """ Adiciona um novo comentário ao Doc
        """
        self.comentarios.append(comentario)

