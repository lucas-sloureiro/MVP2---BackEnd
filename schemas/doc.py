from pydantic import BaseModel
from typing import Optional, List
from model.doc import Doc

from schemas import ComentarioSchema
from schemas import RateBuscaSchema


class DocSchema(BaseModel):
    """ Define como um novo doc a ser inserido deve ser representado
    """
    doc_num: str = "AG32234"
    descricao: str = "Compra - Importação"
    moeda_ori: str = "USD"
    valor_ori: float = 50.00
    taxa: float = 4.87
    valor_brl: float = 243.69

class DocBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do doc_num.
    """
    doc_num: str = "AG32234"

    
class DocidBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no id do doc.
    """
    id: int = 1

class ListagemDocsSchema(BaseModel):
    """ Define como uma listagem de docs será retornada.
    """
    docs:List[DocSchema]


def apresenta_docs(docs: List[Doc]):
    """ Retorna uma representação do doc seguindo o schema definido em
        DocViewSchema.
    """
    result = []
    for doc in docs:
        result.append({
            "doc_num": doc.doc_num,
            "descricao": doc.descricao,
            "moeda_ori": doc.moeda_ori,
            "valor_ori": doc.valor_ori,
            "taxa": doc.taxa,
            "valor_brl": doc.valor_brl,
            "id": doc.id,
        })

    return {"docs": result}


class DocViewSchema(BaseModel):
    """ Define como um doc será retornado: doc + comentários.
    """
    id: int = 1
    doc_num: str = "AG32234"
    descricao: str = "Compra - Importação"
    moeda_ori: str = "USD"
    valor_ori: float = 50.00
    taxa: float = 4.87
    valor_brl: float = 243.69
    total_cometarios: int = 1
    comentarios:List[ComentarioSchema]


class DocDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    doc_num: str

def apresenta_doc(doc: Doc):
    """ Retorna uma representação do doc seguindo o schema definido em
        DocViewSchema.
    """
    return {
        "doc_num": doc.doc_num,
        "descricao": doc.descricao,
        "moeda_ori": doc.moeda_ori,
        "valor_ori": doc.valor_ori,
        "taxa": doc.taxa,
        "valor_brl": doc.valor_brl,
        "total_cometarios": len(doc.comentarios),
        "comentarios": [{"texto": c.texto} for c in doc.comentarios]
    }
