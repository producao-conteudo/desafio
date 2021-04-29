## Desafio

Precisamos desenvolver uma ferramenta para criação de Cards de conteúdo esportivos (Insights).

### 1. Interace HTTP REST API

Ações da API

- Criar card
- Ler card
- Remover card
- Atualizar card
- Listar card
  - Filtrar por tags

Um card possui os campos: 
```
{
  "id": // identificador
  "texto" // texto do card
  "data_criacao" // data da criação do card
  "data_modificacao" // data da última alteração do card
  "tags" // tags vinculas ao card
}
```

- Criar Tag
- Ler Tag
- Remover Tag
- Atualizar Tag

```
Uma tag possui os campos:
{
  "id" // identificador
  "name" // nome da tag
}
```

Temos uma estimativa de milhares de criações de cards diariamente. A preocupação com performance será avaliada.

### 2. CLI para importação dos card

Necessitamos importar os conteúdos do nosso sistema de dados esportivos para gerar nossos cards e precisamos de uma ferramenta para auxiliar essa tarefa.


Dado um csv de "cards", faça um CLI (Command Line Interface) que importe os dados para o Insights.

CSV exemplo:

```
text,tag
Lorem ipsum dolor sit amet., tag1;tag2;tag3
Mauris fringilla non quam vel lacinia,tag3
Cras in tempus libero,
```
### 3. Interface WEB

Após termos nossa api desenvolvida, precisamos viabilizar uma interface frontend para nossos usuários interagirem.

Nosso time de UX desenhou as [telas](https://www.sketch.com/s/3f91077d-21c0-4040-8fae-b89d69809d9b/a/Qb0ZjVe) e disponibilizou para você!

Dê preferência aos frameworks como o Vuetify para aproveitar os componentes já prontos.

Clique no box com o botão de play para entrar no modo de navegação com os hotspots que indicam o fluxo.

Clique em cada uma das telas e utilize a funcionalidade de "Inspector" para ter acesso ao guia de css.

Os ícones utilizados no projeto são do [Material Design](https://material.io/resources/icons/?style=baseline)

Utilize o botão "Download Assets" para baixar a marca do produto Insights.


### Requerimentos:
- Linguagens de programação backend:
  - Python
  - NodeJs
  - C#
- Framework frontend
  - VueJS
  - ReactJS
  - Angular
- Fidelidade de layout
- Code Style
- Teste unitário
- Documentação
  - Descrição
  - Como rodar
  - API DOC (openapi/swagger)

