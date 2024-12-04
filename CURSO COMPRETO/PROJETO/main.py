from fasthtml.common import fast_app, serve
from fasthtml.common import Div, P, Button

# Instância da aplicação e configuração das rotas
app, routes = fast_app()

# Função da página inicial
@routes("/")
def homepage():
    return Div(
        # Botões para mudar as mensagens
        Button("Clique para mudar a mensagem", hx_get="/mudar", hx_target="p", style="margin-bottom: 10px; padding: 10px 20px; font-size: 16px;"),
        Button("Clique para ver outra mensagem", hx_get="/outra", hx_target="p", style="margin-bottom: 10px; padding: 10px 20px; font-size: 16px;"),
        Button("Clique para mais interatividade", hx_get="/interatividade", hx_target="p", style="margin-bottom: 10px; padding: 10px 20px; font-size: 16px;"),
        
        P("Bem-vindo ao FastHTML!", style="font-size: 24px; margin-bottom: 20px;"),
        style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100vh; text-align: center;"
    )

# Função para mudar a mensagem
@routes("/mudar")
def mudar_mensagem():
    return P("Obrigado por explorar o FastHTML!", style="font-size: 20px; color: green;")

# Função para outra mensagem
@routes("/outra")
def outra_mensagem():
    return P("Você clicou no segundo botão!", style="font-size: 20px; color: blue;")

# Função para interatividade
@routes("/interatividade")
def interatividade():
    return P("Agora você tem mais interatividade!", style="font-size: 20px; color: red;")

# Inicializa o servidor
serve()
