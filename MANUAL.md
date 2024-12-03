# MANUAL
## PRÉ-REQUISITOS:
Antes de começar, certifique-se de que você possui os seguintes requisitos:

- **Python 3.7 ou superior**: FastHTML é compatível com Python 3.7+. Você pode verificar a versão instalada executando:
  
  ```bash
  python --version
  ```

- **Pip**: O gerenciador de pacotes do Python deve estar instalado. Verifique com:
  
  ```bash
  pip --version
  ```

- **Ambiente Virtual (opcional, mas recomendado)**: Para isolar as dependências do seu projeto.

## PASSO 1: CONFIGURANDO O AMBIENTE DE DESENVOLVIMENTO:
### 1.1. CRIAR UM AMBIENTE VIRTUAL (OPCIONAL):
Criar um ambiente virtual é uma boa prática para gerenciar dependências do projeto sem afetar outras aplicações no seu sistema.

```bash
# No Windows
python -m venv venv
venv\Scripts\activate

# No macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

Após a ativação, seu prompt de comando deverá exibir o nome do ambiente virtual, por exemplo, `(venv)`.

## PASSO 2: INSTALANDO O FASTHTML:
Com o ambiente configurado, prossiga para a instalação do FastHTML utilizando o `pip`.

```bash
pip install python-fasthtml
```

Este comando instalará o FastHTML e suas dependências necessárias.

## PASSO 3: CRIANDO O PRIMEIRO PROJETO COM FASTHTML:
Vamos criar uma aplicação simples que exibe "Olá, Mundo!".

### 3.1. ESTRUTURA DO PROJETO:
Crie uma pasta para o seu projeto e navegue até ela:

```bash
mkdir meu_primeiro_fasthtml
cd meu_primeiro_fasthtml
```

Dentro dessa pasta, crie um arquivo chamado `main.py`:

```bash
touch main.py
```

### 3.2. ESCREVENDO O CÓDIGO DA APLICAÇÃO:
Abra o arquivo `main.py` no seu editor de texto favorito e adicione o seguinte código:

```python
# main.py

from fasthtml.common import fast_app, serve
from fasthtml.common import Div, P

# Cria a instância da aplicação e das rotas
app, routes = fast_app()

# Define a rota principal
@routes("/")
def homepage():
    return Div(
        P("Olá, Mundo!")
    )

# Executa o servidor
serve()
```

**Explicação do Código:**

- **Importações**:
  - `fast_app` e `serve` são utilizados para criar e executar a aplicação.
  - `Div` e `P` são componentes HTML utilizados para estruturar o conteúdo.

- **Criação da Aplicação**:
  - `app, routes = fast_app()` cria instâncias para a aplicação e suas rotas.

- **Definição da Rota**:
  - `@routes("/")` define a rota raiz (`/`) da aplicação.
  - A função `homepage` retorna um elemento `Div` contendo um parágrafo `P` com o texto "Olá, Mundo!".

- **Execução do Servidor**:
  - `serve()` inicia o servidor local para hospedar a aplicação.

### 3.3. EXECUTANDO A APLICAÇÃO:
No terminal, certifique-se de estar no diretório do projeto e execute:

```bash
python main.py
```

Você verá uma saída semelhante a esta:

```
Servidor rodando em http://localhost:5001
```

Abra o seu navegador e acesse `http://localhost:5001`. Você deverá ver a mensagem "Olá, Mundo!" exibida na página.

## PASSO 4: ADICIONANDO INTERATIVIDADE COM HTMX:
Vamos tornar nossa aplicação um pouco mais interativa adicionando um botão que, ao ser clicado, altera o texto exibido.

### 4.1. ATUALIZANDO O CÓDIGO:
Modifique o arquivo `main.py` para incluir uma nova rota que será chamada via HTMX:

```python
# main.py

from fasthtml.common import fast_app, serve
from fasthtml.common import Div, P, Button

# Cria a instância da aplicação e das rotas
app, routes = fast_app()

# Define a rota principal
@routes("/")
def homepage():
    return Div(
        P("Olá, Mundo!"),
        Button("Clique para mudar o texto", hx_get="/mudar", hx_target="p")
    )

# Define a rota para mudar o texto
@routes("/mudar")
def mudar_texto():
    return P("Texto alterado com sucesso!")

# Executa o servidor
serve()
```

**Explicação das Novas Adições:**

- **Button**: Adicionamos um botão que, ao ser clicado, faz uma requisição GET para a rota `/mudar` usando HTMX.
  - `hx_get="/mudar"`: Define a URL para onde a requisição será enviada.
  - `hx_target="p"`: Especifica que a resposta da requisição deve substituir o elemento `<p>` existente na página.

### 4.2. TESTANDO A INTERATIVIDADE:
Salve as alterações e reinicie o servidor (se estiver rodando, pressione `Ctrl+C` para parar e execute novamente `python main.py`).

Acesse `http://localhost:5001` no navegador. Agora, além do texto "Olá, Mundo!", você verá um botão com o texto "Clique para mudar o texto". Ao clicar no botão, o parágrafo será atualizado para "Texto alterado com sucesso!" sem recarregar a página.

## CONCLUSÃO:
Parabéns! Você instalou o FastHTML e criou sua primeira aplicação web interativa. FastHTML combina a simplicidade do Python com ferramentas modernas para oferecer uma experiência de desenvolvimento ágil e eficiente. Continue explorando a documentação oficial e a comunidade FastHTML para aprofundar seus conhecimentos e criar aplicações cada vez mais robustas e dinâmicas.