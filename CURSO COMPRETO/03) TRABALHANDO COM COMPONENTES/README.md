# TRABALHANDO COM COMPONENTES
Os componentes no FastHTML são estruturas reutilizáveis que permitem criar aplicações web mais organizadas e modulares. Com eles, é possível encapsular blocos de código, facilitando a manutenção e a personalização.

## O QUE SÃO COMPONENTES NO FASTHTML?
Componentes no FastHTML são abstrações de elementos HTML que podem conter lógica embutida e atributos dinâmicos. Eles são usados para:
- Reduzir a duplicação de código.
- Facilitar a reutilização de elementos comuns em várias páginas.
- Organizar melhor a aplicação.

Exemplo de componentes básicos: **Botões**, **Cards**, **Listas**, entre outros.

## CRIANDO COMPONENTES PERSONALIZADOS:
### PASSO 1: CRIANDO UM COMPONENTE:
No FastHTML, componentes são definidos como funções Python que retornam elementos HTML. Um exemplo de componente simples é um **card**.

```python
from fasthtml.common import Div, H3, P

def Card(title, content):
    """Componente de Card personalizado."""
    return Div(
        H3(title),
        P(content),
        class_="card"
    )
```

### PASSO 2: USANDO O COMPONENTE:
Você pode utilizar o componente criado diretamente em suas rotas. Por exemplo, criando uma lista de cards:

```python
@routes("/")
def homepage():
    return Div(
        Card("Card 1", "Este é o conteúdo do primeiro card."),
        Card("Card 2", "Este é o conteúdo do segundo card."),
        class_="card-container"
    )
```

## CONCLUSÃO:
Trabalhar com componentes no FastHTML permite construir páginas organizadas e escaláveis. Ao encapsular lógica e estrutura em funções reutilizáveis, você melhora a manutenção do código e acelera o desenvolvimento. Este exemplo mostrou como criar e estilizar componentes de maneira simples e prática.