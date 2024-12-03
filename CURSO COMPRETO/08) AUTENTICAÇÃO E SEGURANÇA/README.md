# AUTENTICAÇÃO E SEGURANÇA
A autenticação e segurança são aspectos essenciais para proteger dados e garantir que apenas usuários autorizados possam acessar recursos específicos de uma aplicação web. Integrar autenticação e aplicar práticas de segurança é fundamental em qualquer aplicação, especialmente quando ela manipula informações sensíveis, como dados de usuários.

No **FastHTML**, podemos implementar autenticação básica e boas práticas de segurança de forma simples, utilizando bibliotecas Python como `werkzeug` (para hashing de senhas) e sessões para manter o estado do usuário.

## CONCEITO:
Autenticação é o processo de identificar e verificar se um usuário é quem ele afirma ser, geralmente utilizando um **nome de usuário** e uma **senha**.

**1. Criação de uma Tabela de Usuários**

Primeiro, vamos criar uma tabela de usuários no banco de dados SQLite para armazenar as credenciais (nome de usuário e senha).

**Arquivo: `database.py`**

```python
import sqlite3

# Função para inicializar o banco de dados
def init_db():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    
    # Criação das tabelas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()

# Função para adicionar um novo usuário
def add_user(username, password):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

# Função para verificar as credenciais de um usuário
def check_user(username, password):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    stored_password = cursor.fetchone()
    conn.close()
    
    return stored_password and stored_password[0] == password
```

* **Explicação**:
- A tabela `users` armazena as credenciais dos usuários (nome de usuário e senha).
- As funções `add_user()` e `check_user()` são responsáveis por adicionar um novo usuário ao banco de dados e verificar se as credenciais fornecidas são válidas, respectivamente.

**2. Implementação de Autenticação com Sessões**

Agora, vamos implementar um sistema de autenticação utilizando sessões. Isso permitirá que o FastHTML "lembre" os usuários durante sua navegação pela aplicação.

**Arquivo: `main.py`**

```python
from fasthtml.common import fast_app, serve, Div, Form, Input, Button, H2, A, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
from database import add_user, check_user

# Configuração do FastHTML
app, routes = fast_app()

# Inicializando a sessão
app.secret_key = 'super_secret_key'

@routes("/login", methods=["GET", "POST"])
def login(request):
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        # Verifica as credenciais
        if check_user(username, password):
            session["user"] = username  # Salva o nome de usuário na sessão
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

@routes("/tasks")
def task_manager():
    # Verifica se o usuário está logado
    if "user" not in session:
        return redirect("/login")

    username = session["user"]
    return Div(
        H2(f"Bem-vindo, {username}!"),
        A("Sair", href="/logout"),
        class_="container"
    )

@routes("/logout")
def logout():
    session.pop("user", None)  # Remove o usuário da sessão
    return redirect("/login")

# Inicia o servidor
serve()
```

* **Explicação**:
- A rota `/login` recebe os dados de nome de usuário e senha. Se as credenciais forem válidas, a sessão do usuário é criada e ele é redirecionado para a página de tarefas (`/tasks`).
- A rota `/tasks` verifica se o usuário está autenticado (se existe uma sessão ativa). Se o usuário não estiver logado, ele é redirecionado para a página de login.
- A rota `/logout` encerra a sessão do usuário e o redireciona para a página de login.

## GERAÇÃO DE SENHAS SEGURAS COM `WERKZEUG`:
Ao armazenar senhas no banco de dados, é importante **nunca armazenar senhas em texto simples**. Utilizamos a biblioteca `werkzeug.security` para gerar e verificar senhas de forma segura.

Para adicionar um usuário com senha segura, você pode modificar a função `add_user` no `database.py`:

```python
from werkzeug.security import generate_password_hash

def add_user(username, password):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    hashed_password = generate_password_hash(password)  # Criptografa a senha
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    conn.close()
```

No login, ao verificar a senha, usamos `check_password_hash` para comparar a senha fornecida com a senha armazenada:

```python
from werkzeug.security import check_password_hash

def check_user(username, password):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    stored_password = cursor.fetchone()
    conn.close()
    
    return stored_password and check_password_hash(stored_password[0], password)
```

**3. Segurança de Sessões**

A segurança de sessões é crucial para garantir que as informações do usuário não sejam comprometidas. Aqui estão algumas boas práticas de segurança:

1. **Usar uma chave secreta**: A chave secreta (`app.secret_key`) é usada para assinar as sessões, garantindo que não possam ser manipuladas.
2. **Armazenamento de Senhas**: Sempre use **hashing** seguro para armazenar senhas, nunca as armazene em texto simples.
3. **Controle de Sessão**: Quando o usuário se desloga, remova todas as informações sensíveis da sessão (como o nome de usuário).

## CONCLUSÃO:
A autenticação e segurança são fundamentais para proteger qualquer aplicação web. Utilizando **FastHTML** e **SQLite**, você pode implementar uma autenticação básica com **sessões** e garantir que as credenciais sejam armazenadas de maneira segura. Para melhorar a segurança, sempre utilize boas práticas, como o uso de **hashing de senhas** e controle rigoroso de **sessões**.

Essa implementação é uma base para construir aplicações web seguras e pode ser expandida conforme as necessidades do seu projeto, adicionando mais camadas de segurança e funcionalidades de autenticação avançada.