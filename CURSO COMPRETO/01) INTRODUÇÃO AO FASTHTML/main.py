from fasthtml.common import fast_app, serve
from fasthtml.common import Div, P, Button

# Instância da aplicação e configuração das rotas
app, routes = fast_app()

@routes("/")
def homepage():
    return Div(
        P("Bem-vindo ao FastHTML!"),
        Button("Clique para mudar a mensagem", hx_get="/mudar", hx_target="p")
    )

@routes("/mudar")
def mudar_mensagem():
    return P("Obrigado por explorar o FastHTML!")

# Inicializa o servidor
serve()
