from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Doc, Comentario
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
doc_tag = Tag(name="Doc", description="Adição, visualização e remoção de docs à base")
comentario_tag = Tag(name="Comentario", description="Adição de um comentário à um doc cadastrado na base")
rate_tag = Tag(name="Rate", description="Adição de um rate à um doc cadastrado na base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/doc', tags=[doc_tag],
          responses={"200": DocViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_doc(form: DocSchema):
    """Adiciona um novo Doc à base de dados

    Retorna uma representação dos docs e comentários associados.
    """
    doc = Doc(
        doc_num=form.doc_num,
        descricao=form.descricao,
        moeda_ori=form.moeda_ori,
        valor_ori=form.valor_ori,
        taxa=form.taxa,
        valor_brl=form.valor_brl)
    logger.debug(f"Adicionando doc de doc_num: '{doc.doc_num}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando doc
        session.add(doc)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado doc de doc_num: '{doc.doc_num}'")
        return apresenta_doc(doc), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Doc de mesmo doc_num já salvo na base :/"
        logger.warning(f"Erro ao adicionar doc '{doc.doc_num}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar doc '{doc.doc_num}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.put('/doc', tags=[doc_tag],
          responses={"200": DocViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def put_doc(form: DocSchema):
    """Adiciona um novo Doc à base de dados

    Retorna uma representação dos docs e comentários associados.
    """
    doc = Doc(
        doc_num=form.doc_num,
        descricao=form.descricao,
        moeda_ori=form.moeda_ori,
        valor_ori=form.valor_ori,
        taxa=form.taxa,
        valor_brl=form.valor_brl)
    logger.debug(f"Adicionando doc de doc_num: '{doc.doc_num}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando doc
        session.add(doc)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado doc de doc_num: '{doc.doc_num}'")
        return apresenta_doc(doc), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Doc de mesmo doc_num já salvo na base :/"
        logger.warning(f"Erro ao adicionar doc '{doc.doc_num}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar doc '{doc.doc_num}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.get('/docs', tags=[doc_tag],
         responses={"200": ListagemDocsSchema, "404": ErrorSchema})
def get_docs():
    """Faz a busca por todos os Doc cadastrados

    Retorna uma representação da listagem de docs.
    """
    logger.debug(f"Coletando docs ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    docs = session.query(Doc).all()

    if not docs:
        # se não há docs cadastrados
        return {"docs": []}, 200
    else:
        logger.debug(f"%d docs econtrados" % len(docs))
        # retorna a representação de doc
        print(docs)
        return apresenta_docs(docs), 200


@app.get('/doc', tags=[doc_tag],
         responses={"200": DocViewSchema, "404": ErrorSchema})
def get_doc(query: DocBuscaSchema):
    """Faz a busca por um Doc a partir do nome do doc_num

    Retorna uma representação dos docs e comentários associados.
    """
    doc_doc_num = query.doc_num
    logger.debug(f"Coletando dados sobre doc #{doc_doc_num}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    doc = session.query(Doc).filter(Doc.doc_num == doc_doc_num).first()

    if not doc:
        # se o doc não foi encontrado
        error_msg = "Doc não encontrado na base :/"
        logger.warning(f"Erro ao buscar doc '{doc_doc_num}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Doc econtrado: '{doc.doc_num}'")
        # retorna a representação de doc
        return apresenta_doc(doc), 200
    

@app.get('/doc_id', tags=[doc_tag],
         responses={"200": DocViewSchema, "404": ErrorSchema})
def get_doc_id(query: DocidBuscaSchema):
    """Faz a busca por um Doc a partir do id do doc

    Retorna uma representação dos docs e comentários associados.
    """
    doc_id = query.id
    logger.debug(f"Coletando dados sobre doc #{doc_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    doc = session.query(Doc).filter(Doc.id == doc_id).first()

    if not doc:
        # se o doc não foi encontrado
        error_msg = "Doc não encontrado na base :/"
        logger.warning(f"Erro ao buscar doc '{doc_id}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Doc econtrado: '{doc.id}'")
        # retorna a representação de doc
        return apresenta_doc(doc), 200
    

@app.delete('/doc', tags=[doc_tag],
            responses={"200": DocDelSchema, "404": ErrorSchema})
def del_doc(query: DocidBuscaSchema):
    """Deleta um Doc a partir do id do doc

    Retorna uma mensagem de confirmação da remoção.
    """
    doc_id = query.id
    print(doc_id)
    logger.debug(f"Deletando dados sobre doc #{doc_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Doc).filter(Doc.id == doc_id).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado doc #{doc_id}")
        return {"mesage": "Doc removido", "id": doc_id}
    else:
        # se o doc não foi encontrado
        error_msg = "Doc não encontrado na base :/"
        logger.warning(f"Erro ao deletar doc #'{doc_id}', {error_msg}")
        return {"mesage": error_msg}, 404


@app.post('/cometario', tags=[comentario_tag],
          responses={"200": DocViewSchema, "404": ErrorSchema})
def add_comentario(form: ComentarioSchema):
    """Adiciona de um novo comentário à um docs cadastrado na base identificado pelo id

    Retorna uma representação dos docs e comentários associados.
    """
    doc_id  = form.doc_id
    logger.debug(f"Adicionando comentários ao doc #{doc_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca pelo doc
    doc = session.query(Doc).filter(Doc.id == doc_id).first()

    if not doc:
        # se doc não encontrado
        error_msg = "Doc não encontrado na base :/"
        logger.warning(f"Erro ao adicionar comentário ao doc '{doc_id}', {error_msg}")
        return {"mesage": error_msg}, 404

    # criando o comentário
    texto = form.texto
    comentario = Comentario(texto)

    # adicionando o comentário ao doc
    doc.adiciona_comentario(comentario)
    session.commit()

    logger.debug(f"Adicionado comentário ao doc #{doc_id}")

    # retorna a representação de doc
    return apresenta_doc(doc), 200


@app.get('/https://api.freecurrencyapi.com/v1/latest/', tags=[rate_tag],
         responses={"200": DocViewSchema, "404": ErrorSchema})
def get_rate(query: RateBuscaSchema):
    """Faz a busca por um da taxa de conversão para BRL.
    """
    doc_base_currency = query.base_currency
    logger.debug(f"Coletando dados sobre doc #{doc_base_currency}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    doc = session.query(Doc).filter(Doc.base_currency == doc_base_currency).first()

    if not doc:
        # se o doc não foi encontrado
        error_msg = "Doc não encontrado na base :/"
        logger.warning(f"Erro ao buscar doc '{doc_base_currency}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Doc econtrado: '{doc.base_currency}'")
        # retorna a representação de doc
        return apresenta_doc(doc), 200
