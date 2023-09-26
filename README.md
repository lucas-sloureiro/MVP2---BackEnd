# API - Cadastro de gols do Brasileirão - Lucas Loureiro

Este pequeno projeto faz parte do MVP da PUC, sprint **Arquitetura de Software** 

## API Externa

A API utilizada informa uma taxa de conversão em 3 rotas distintas para USD, EUR e GBP.
A API Key utilizada:
fca_live_Ae2r3i5KHIMJ60edGDfuR83R0bpikwp3fUpxZw5Y

---
## Como executar 


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
