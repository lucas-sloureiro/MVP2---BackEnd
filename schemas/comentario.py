from pydantic import BaseModel


class ComentarioSchema(BaseModel):
    """ Define como um novo comentário a ser inserido deve ser representado
    """
    doc_id: int = 1
    texto: str = "Hoje tem doc do Gabidoc! |_O_|"
