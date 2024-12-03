from fasthtml.common import fast_app, serve, Div, Form, Input, Button, H2, Ul, Li, A, redirect, session
from database import add_user, check_user, add_task, get_tasks, complete_task

# Configuração do FastHTML
app, routes = fast_app()

# Chave secreta para sessões
app.secret_key = 'super_secret_key'

@routes("/login", methods=["GET", "POST"])
def login(request):
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        user_id = check_user(username, password)
        if user_id:
            session["user_id"] = user_id
            return redirect("/tasks")
        else:
            return Div("Usuário ou senha inválidos.", class_="error")

    return Div(
        Form(
            Input(type="text", name="username", placeholder="Nome de usuário", required=True),
            Input(type="password", name="password", placeholder="Senha", required=True),
            Button("Entrar", type="submit"),
            action="/login", method="post", class_="login-form"
        ),
        class_="container"
    )

@routes("/register", methods=["GET", "POST"])
def register(request):
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        add_user(username, password)
        return redirect("/login")

    return Div(
        Form(
            Input(type="text", name="username", placeholder="Nome de usuário", required=True),
            Input(type="password", name="password", placeholder="Senha", required=True),
            Button("Cadastrar", type="submit"),
            action="/register", method="post", class_="register-form"
        ),
        class_="container"
    )

@routes("/tasks")
def task_manager():
    if "user_id" not in session:
        return redirect("/login")

    user_id = session["user_id"]
    tasks = get_tasks(user_id)
    task_list = Ul(
        *[
            Li(
                f"{task[1]} - {'Concluída' if task[2] else 'Pendente'}",
                A("Concluir", href=f"/complete/{task[0]}", class_="complete-link") if not task[2] else "",
                class_="task-item"
            )
            for task in tasks
        ]
    )

    return Div(
        H2("Gerenciamento de Tarefas"),
        Form(
            Input(type="text", name="description", placeholder="Nova tarefa", required=True),
            Button("Adicionar", type="submit"),
            action="/add-task", method="post", class_="task-form"
        ),
        task_list,
        class_="container"
    )

@routes("/add-task", methods=["POST"])
def add_new_task(request):
    if "user_id" not in session:
        return redirect("/login")

    user_id = session["user_id"]
    description = request.form.get("description")
    add_task(user_id, description)
    return redirect("/tasks")

@routes("/complete/<int:task_id>")
def complete_task_route(task_id):
    complete_task(task_id)
    return redirect("/tasks")

@routes("/logout")
def logout():
    session.pop("user_id", None)
    return redirect("/login")

# Inicia o servidor
serve()
