from pydantic import BaseModel

class RateBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome da Moeda.
    """
    apikey: str = 'fca_live_Ae2r3i5KHIMJ60edGDfuR83R0bpikwp3fUpxZw5Y'
    currencies: str = 'BRL'
    base_currency: str = "USD" 

