from fasthtml.common import fast_app, serve, Div, Form, Input, Button, Ul, Li, A
from database import get_tasks, add_task, complete_task

# Configuração do FastHTML
app, routes = fast_app()

@routes("/")
def task_manager():
    tasks = get_tasks()
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
    description = request.form.get("description")
    if description:
        add_task(description)
    return redirect("/")

@routes("/complete/<int:task_id>")
def mark_complete(task_id):
    complete_task(task_id)
    return redirect("/")

# Inicia o servidor
serve()
