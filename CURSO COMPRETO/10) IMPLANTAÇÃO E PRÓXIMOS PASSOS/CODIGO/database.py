import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from cachetools import TTLCache, cached

# Criação do cache com TTL de 10 minutos
cache = TTLCache(maxsize=100, ttl=600)

def init_db():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()

    # Criar tabela de usuários
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)

    # Criar tabela de tarefas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0,
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)
    
    conn.commit()
    conn.close()

# Função para adicionar um novo usuário
def add_user(username, password):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    hashed_password = generate_password_hash(password)
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    conn.close()

# Função para verificar as credenciais de um usuário
@cached(cache)
def check_user(username, password):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, password FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()

    if user and check_password_hash(user[1], password):
        return user[0]  # Retorna o ID do usuário
    return None

# Função para adicionar uma tarefa
def add_task(user_id, description):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (description, user_id) VALUES (?, ?)", (description, user_id))
    conn.commit()
    conn.close()

# Função para obter as tarefas de um usuário com cache
@cached(cache)
def get_tasks(user_id):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, description, completed FROM tasks WHERE user_id = ?", (user_id,))
    tasks = cursor.fetchall()
    conn.close()
    return tasks

# Função para completar uma tarefa
def complete_task(task_id):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

# Inicializa o banco de dados
init_db()
