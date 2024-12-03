# INTEGRAÇÃO COM BANCOS DE DADOS
Integrar um banco de dados [SQLite](https://github.com/VILHALVA/CURSO-DE-SQLITE) ao **FastHTML** permite que você armazene e manipule dados de forma persistente, o que é essencial para muitas aplicações web, como gerenciadores de tarefas, blogs ou qualquer sistema que precise de armazenamento local.

**SQLite** é uma excelente escolha para aplicativos pequenos e médios, pois é um banco de dados relacional que armazena dados em um único arquivo de disco, sendo fácil de configurar e usar.

A seguir, vamos ver como configurar a integração com SQLite em uma aplicação usando **FastHTML**.

## ESTRUTURA DO PROJETO:
Vamos criar uma aplicação simples de gerenciamento de tarefas onde os dados serão armazenados no banco de dados SQLite.

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

**1. Banco de Dados SQLite: `database.py`**

Primeiro, criamos o banco de dados e as funções CRUD para interagir com ele.

**Arquivo: `database.py`**

```python
import sqlite3

# Função para inicializar o banco de dados
def init_db():
    conn = sqlite3.connect('tasks.db')
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

# Função para obter todas as tarefas
def get_tasks():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, description, completed FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

# Função para adicionar uma tarefa
def add_task(description):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (description) VALUES (?)", (description,))
    conn.commit()
    conn.close()

# Função para marcar uma tarefa como concluída
def complete_task(task_id):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

# Inicializa o banco de dados ao importar
init_db()
```

**2. Backend com FastHTML: `main.py`**

No arquivo `main.py`, criamos as rotas para exibir tarefas, adicionar novas e marcar como concluídas.

**Arquivo: `main.py`**

```python
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
```

**3. Estilização com CSS: `static/css/style.css`**

Vamos adicionar um arquivo CSS simples para melhorar a aparência da nossa aplicação.

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
1. Instale as dependências:
   ```bash
   pip install python-fasthtml
   ```

2. Execute o servidor:
   ```bash
   python main.py
   ```

3. Acesse no navegador: [http://localhost:5001](http://localhost:5001).

## EXPLICAÇÃO:
1. **Banco de Dados**:
   - O banco de dados SQLite é usado para armazenar tarefas com os campos: `id`, `description`, e `completed`.
   - A função `init_db()` inicializa o banco, criando a tabela `tasks` se ela não existir.

2. **Operações CRUD**:
   - **`get_tasks()`**: Recupera todas as tarefas do banco de dados.
   - **`add_task(description)`**: Insere uma nova tarefa no banco de dados.
   - **`complete_task(task_id)`**: Marca uma tarefa como concluída no banco de dados.

3. **Rotas do FastHTML**:
   - A rota `/` exibe o formulário de adição de tarefas e a lista de tarefas.
   - A rota `/add-task` processa a adição de uma nova tarefa.
   - A rota `/complete/<task_id>` marca a tarefa como concluída.

4. **Interface**:
   - Usamos HTML simples e estilizamos com CSS.
   - A interação com o banco de dados é feita no backend, e o frontend é atualizado dinamicamente.


