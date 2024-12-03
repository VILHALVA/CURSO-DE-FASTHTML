# MANIPULAÇÃO DE DADOS NO BACKEND
Manipular dados no backend é uma parte central do desenvolvimento web. Com **FastHTML**, a manipulação de dados pode ser feita utilizando frameworks e bibliotecas padrão do Python, como:

1. **SQLite ou Bancos de Dados Relacionais** ( [via sqlite](https://github.com/VILHALVA/CURSO-DE-SQLITE) ou ORMs como SQLAlchemy).
2. **Arquivos JSON ou CSV** para armazenamento leve.
3. **APIs Externas** para consumir e transformar dados de fontes externas.

Vamos explorar os conceitos e criar um exemplo prático.

## EXEMPLO: APLICAÇÃO DE GERENCIAMENTO DE TAREFAS:
Neste exemplo, desenvolveremos uma aplicação de tarefas com as seguintes funcionalidades:
- Listar tarefas armazenadas no backend.
- Adicionar novas tarefas.
- Marcar tarefas como concluídas.

### ESTRUTURA DO PROJETO:
```
CODIGO/
├── main.py
├── database.py
├── static/
│   └── css/
│       └── style.css
└── templates/
    └── base.html
```

**1. Banco de Dados SQLite**:

Criaremos um banco de dados SQLite para armazenar as tarefas.

**Arquivo: `database.py`**

```python
import sqlite3

# Inicialização do banco de dados
def init_db():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

# Funções CRUD
def get_tasks():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, description, completed FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def add_task(description):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (description) VALUES (?)", (description,))
    conn.commit()
    conn.close()

def complete_task(task_id):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

# Inicialize o banco ao importar
init_db()
```

**2. Backend com FastHTML**

**Arquivo: `main.py`**

```python
from fasthtml.common import fast_app, serve, Div, Form, Input, Button, Ul, Li, A
from database import get_tasks, add_task, complete_task

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

serve()
```

**3. Estilização com CSS**

**Arquivo: `static/css/style.css`**

```css
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f9;
    margin: 0;
    padding: 0;
}

.container {
    max-width: 600px;
    margin: 40px auto;
    padding: 20px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.task-form {
    margin-bottom: 20px;
    display: flex;
    gap: 10px;
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

ul {
    list-style-type: none;
    padding: 0;
}

li {
    background: #f9f9f9;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin-bottom: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.complete-link {
    color: green;
    text-decoration: none;
}

.complete-link:hover {
    text-decoration: underline;
}
```


## EXECUTANDO O PROJETO:
1. Instale dependências:
   ```bash
   pip install python-fasthtml
   ```

2. Execute o servidor:
   ```bash
   python main.py
   ```

3. Abra no navegador: [http://localhost:5001](http://localhost:5001).

## EXPLICAÇÃO:
1. **Banco de Dados**:
   - O banco de dados SQLite armazena as tarefas com atributos: `id`, `description`, e `completed`.

2. **Rotas no Backend**:
   - A rota `/` exibe todas as tarefas e um formulário para adicionar novas.
   - A rota `/add-task` adiciona uma nova tarefa ao banco de dados.
   - A rota `/complete/<id>` marca uma tarefa como concluída.

3. **Estilo**:
   - O CSS melhora a interface, tornando-a mais acessível e visualmente agradável.

