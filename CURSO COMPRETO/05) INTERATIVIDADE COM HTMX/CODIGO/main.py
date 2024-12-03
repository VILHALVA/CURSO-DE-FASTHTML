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
