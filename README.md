# Projeto L
Este é o repositório do *backend* do projeto que foi proposto como desafio do *hackathon* que foi realizado no 1° LABootcamp.

# Desafio
Construir uma solução que possibilitasse ao usuário a visualização de todos os seus dados armazenados pela plataforma Wikilegis.

## Requisitos
- Construir uma solução onde fosse separado as camadas de frontend e backend
- Utilizar o framework React
- Utilizar a linguagem de consulta GraphQL
- Utilizar Docker para isolamento de ambiente
- Apresentar uma solução relacionada a [LGPD](http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709.htm)


## Solução proposta
A solução proposta foi a construção de uma API utilizando [Django](https://docs.djangoproject.com/en/2.2/) e [Graphene-Django](https://docs.graphene-python.org/projects/django/en/latest/) que possibilitasse a consulta por meio de GraphQL e retornasse informações referentes as sugestões e votos de um usuário específico no Wikilegis.

A API contida neste repositório será consultada pelo [frontend](https://github.com/labhackercd/projetoL-frontend).


## Executando o projeto
Para execução deste projeto é necessário realizar a instalaçã do [Docker](https://docs.docker.com/install/) e [Docker-Compose](https://docs.docker.com/compose/install/). Foi utilizado a imagem do Python 3.6 Alpine para a construção do container desta aplicação

Para executar a aplicação é necessário executar o seguinte comando:

```bash
docker-compose up
```

Após a execução deste comando a aplicação e *backend* estára rodando dentro do container que está mapeado na porta **8000** do host.


## Acessando a aplicação
A aplicação poderá ser acessada através do link:
**http://localhost:8000/graphql/**


# Link úteis
* https://graphql.org/learn/
* https://www.howtographql.com/
* https://graphene-python.org/
