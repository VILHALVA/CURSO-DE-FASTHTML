# INTERATIVIDADE COM HTMX
O **HTMX** é uma biblioteca JavaScript que facilita a criação de interatividade em páginas web sem a necessidade de escrever muito código JavaScript. Ele permite realizar requisições HTTP assíncronas diretamente em elementos HTML, atualizando partes específicas da página, ideal para interfaces reativas e modernas.

No **FastHTML**, HTMX é integrado facilmente para criar funcionalidades como:
- Atualizações dinâmicas de conteúdo.
- Requisições POST e GET dinâmicas.
- Carregamento de seções sob demanda.

## CONFIGURAÇÃO INICIAL:
1. **Instale o HTMX**:
   Inclua o script do HTMX no template base:
   ```html
   <script src="https://unpkg.com/htmx.org"></script>
   ```

2. **Estrutura do Projeto**:
   Organize o projeto para incluir rotas que manipulam requisições HTMX.
   ```
   CODIGO/
   ├── main.py
   ├── static/
   │   └── css/
   │       └── style.css
   └── templates/
       └── base.html
   ```

## EXEMPLO PRÁTICO:
Vamos criar uma página que carrega dinamicamente uma lista de itens e permite adicionar novos itens usando HTMX.

**1. Arquivo Principal: `main.py`**

```python
from fasthtml.common import fast_app, serve, Div, H1, Ul, Li, Button, Form, Input, Label

app, routes = fast_app()

# Lista inicial
items = ["Item 1", "Item 2", "Item 3"]

@routes("/")
def homepage():
    """Página principal com lista interativa."""
    return Div(
        H1("Lista Interativa com HTMX"),
        Ul(*[Li(item, class_="list-item") for item in items], id="item-list"),
        Form(
            Div(
                Label("Novo Item:", for_="new-item"),
                Input(type="text", id="new-item", name="new-item", required=True),
            ),
            Button("Adicionar", type="submit"),
            hx_post="/add-item",  # Ação dinâmica com HTMX
            hx_target="#item-list",  # Atualiza apenas a lista
            hx_swap="beforeend",    # Insere o novo item no final
        ),
        class_="container"
    )

@routes("/add-item", methods=["POST"])
def add_item(request):
    """Adiciona um item à lista dinamicamente."""
    new_item = request.form.get("new-item")
    if new_item:
        items.append(new_item)
        return Li(new_item, class_="list-item")
    return "Erro: Nenhum item fornecido", 400

serve()
```

**2. Template Base: `templates/base.html`**

Adicione o script HTMX e estilização básica.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../static/css/style.css">
    <script src="https://unpkg.com/htmx.org"></script>
    <title>Interatividade com HTMX</title>
</head>
<body>
    <header>
        <h1>FastHTML com HTMX</h1>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
```

**3. Arquivo CSS: `static/css/style.css`**

Estilize a página para melhor visualização.

```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f9;
}

.container {
    max-width: 600px;
    margin: 40px auto;
    padding: 20px;
    background: white;
    border: 1px solid #ddd;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
    color: #0073e6;
}

ul {
    padding: 0;
    list-style-type: none;
}

.list-item {
    background: #f9f9f9;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin-bottom: 10px;
}

form {
    margin-top: 20px;
    display: flex;
    gap: 10px;
    align-items: center;
}

input {
    flex: 1;
    padding: 8px;
    border: 1px solid #ddd;
    border-radius: 5px;
}

button {
    padding: 8px 16px;
    background-color: #0073e6;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #005bb5;
}
```

## EXECUTANDO O PROJETO:
1. Execute o servidor:
   ```bash
   python main.py
   ```

2. Acesse o navegador: [http://localhost:5001](http://localhost:5001).

3. Adicione novos itens na lista usando o formulário. Observe que a lista é atualizada dinamicamente sem recarregar a página.

## COMO FUNCIONA?
1. **Requisição HTMX**:
   - O formulário usa `hx-post` para enviar dados ao servidor.
   - `hx-target` especifica o elemento HTML a ser atualizado (neste caso, a lista `<ul>`).
   - `hx-swap` define como o conteúdo recebido será integrado (aqui, inserido no final da lista).

2. **Resposta Dinâmica**:
   - A rota `/add-item` retorna um novo item HTML (`<li>`).
   - HTMX insere o item diretamente no DOM sem recarregar a página.

## CONCLUSÃO:
O HTMX, integrado ao FastHTML, permite criar aplicações interativas e dinâmicas com simplicidade. Ele elimina a necessidade de gerenciar complexidade JavaScript manualmente, acelerando o desenvolvimento de interfaces modernas. 
