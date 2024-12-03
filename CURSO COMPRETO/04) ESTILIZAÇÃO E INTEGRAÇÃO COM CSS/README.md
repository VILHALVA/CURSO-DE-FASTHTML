# ESTILIZAÇÃO E INTEGRAÇÃO COM CSS
O FastHTML permite estilizar aplicações web usando CSS (Cascading Style Sheets), integrando estilos externos ou internos para criar interfaces elegantes e responsivas. A estilização e a separação de estilos em arquivos CSS externos são práticas fundamentais para manter o código organizado e reutilizável.

## COMO INTEGRAR CSS NO FASTHTML?
Existem duas formas principais de adicionar CSS a um projeto FastHTML:
1. **CSS Externo**: Arquivos CSS são colocados em uma pasta dedicada, como `static/css/`, e vinculados aos templates ou rotas.
2. **CSS Inline**: Adiciona estilos diretamente aos elementos no código.

### 1. CSS EXTERNO:
**Passo 1: Configuração do Projeto**

Estrutura básica com arquivo CSS externo:
```
meu_projeto/
├── main.py
├── static/
│   └── css/
│       └── estilo.css
└── templates/
    └── base.html
```

**Passo 2: Criar o Arquivo CSS**

Adicione estilos no arquivo `static/css/estilo.css`:
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f9;
    color: #333;
}

header {
    background-color: #0073e6;
    color: white;
    text-align: center;
    padding: 20px;
}

button {
    background-color: #0073e6;
    color: white;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
    border-radius: 5px;
}

button:hover {
    background-color: #005bb5;
}
```

**Passo 3: Vincular o CSS ao Template**

Edite o template `templates/base.html` para incluir o arquivo CSS:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/css/estilo.css">
    <title>{% block title %}Minha App FastHTML{% endblock %}</title>
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```

**Passo 4: Usar o CSS no Código**

Crie uma rota no `main.py` para exibir o conteúdo estilizado:
```python
from fasthtml.common import fast_app, serve, Div, H1, Button

app, routes = fast_app()

@routes("/")
def home():
    return Div(
        H1("Bem-vindo ao FastHTML!"),
        Button("Clique Aqui"),
        class_="container"
    )

serve()
```

### 2. CSS INLINE:
Adicione estilos diretamente aos elementos no código Python utilizando o atributo `style`.

Exemplo:
```python
@routes("/inline")
def inline_styling():
    return Div(
        H1("Título com Estilo Inline", style="color: blue; text-align: center;"),
        Button("Botão Inline", style="background-color: red; color: white; border: none;"),
        style="margin: 20px; padding: 10px; border: 1px solid #ccc;"
    )
```

Embora funcional, **o CSS inline é recomendado apenas para estilos rápidos ou provisórios**, pois dificulta a manutenção do código.

## ESTILIZAÇÃO AVANÇADA: USANDO CSS COM CLASSES E IDS:
### CSS COM CLASSES:
Classes são usadas para estilizar elementos reutilizáveis. No FastHTML, você pode definir classes em elementos HTML.

Exemplo:
```python
@routes("/classes")
def classes_example():
    return Div(
        H1("Título com Classe", class_="titulo"),
        Button("Botão Estilizado", class_="botao"),
    )
```

CSS correspondente:
```css
.titulo {
    font-size: 24px;
    color: #0073e6;
    text-align: center;
}

.botao {
    background-color: #0073e6;
    color: white;
    padding: 10px;
    border: none;
    cursor: pointer;
    border-radius: 5px;
}

.botao:hover {
    background-color: #005bb5;
}
```

### CSS COM IDS:
IDs são usados para estilizar elementos únicos. No FastHTML, você pode definir IDs em elementos HTML.

Exemplo:
```python
@routes("/ids")
def ids_example():
    return Div(
        H1("Título com ID", id="titulo-principal"),
        Button("Botão com ID", id="botao-principal"),
    )
```

CSS correspondente:
```css
#titulo-principal {
    font-size: 30px;
    font-weight: bold;
    color: darkgreen;
    text-align: center;
}

#botao-principal {
    background-color: orange;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 8px;
}

#botao-principal:hover {
    background-color: darkorange;
}
```

## CONCLUSÃO:
O FastHTML facilita a integração de CSS, permitindo criar páginas elegantes e responsivas. A separação de responsabilidades, com estilos em arquivos externos, é a melhor prática para escalabilidade e manutenção. CSS inline, classes e IDs oferecem flexibilidade para ajustar detalhes ou criar estilos exclusivos rapidamente.

