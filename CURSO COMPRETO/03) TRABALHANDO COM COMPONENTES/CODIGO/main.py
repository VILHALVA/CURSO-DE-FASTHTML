from fasthtml.common import fast_app, serve, Div, H3, P

# Inicializa o app
app, routes = fast_app()

# Componente Card
def Card(title, content):
    """Componente de Card personalizado."""
    return Div(
        H3(title),
        P(content),
        class_="card"
    )

# Rota principal
@routes("/")
def homepage():
    return Div(
        Card("Título 1", "Conteúdo do primeiro card."),
        Card("Título 2", "Conteúdo do segundo card."),
        Card("Título 3", "Conteúdo do terceiro card."),
        class_="card-container"
    )

# Inicia o servidor
serve()
