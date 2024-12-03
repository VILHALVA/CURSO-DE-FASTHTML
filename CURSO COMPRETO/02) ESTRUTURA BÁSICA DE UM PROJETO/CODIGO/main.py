from fasthtml.common import fast_app, serve, load_template
from fasthtml.common import Div, H1, P, A

# Inicializa o app e define rotas
app, routes = fast_app()

# Dados de exemplo: lista de posts
posts = [
    {"id": 1, "title": "Primeiro Post", "content": "Bem-vindo ao primeiro post!"},
    {"id": 2, "title": "Segundo Post", "content": "Explorando o FastHTML é muito fácil."},
    {"id": 3, "title": "Terceiro Post", "content": "Continue aprendendo e criando!"},
]

# Rota inicial: exibe lista de posts
@routes("/")
def home():
    post_links = [A(post["title"], href=f"/post/{post['id']}") for post in posts]
    return load_template("home.html", posts=post_links)

# Rota de detalhes de um post
@routes("/post/{id}")
def post_detail(id: int):
    post = next((p for p in posts if p["id"] == int(id)), None)
    if not post:
        return Div(H1("Post não encontrado"), P("Verifique o ID e tente novamente."))
    return load_template("post_detail.html", post=post)

# Inicializa o servidor
serve()
