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
