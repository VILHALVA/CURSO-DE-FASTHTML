# ESTRUTURA BÁSICA DE UM PROJETO
Ao criar um projeto com FastHTML, é essencial organizar os arquivos e pastas para facilitar o desenvolvimento e a manutenção. Este capítulo abordará a estrutura ideal de um projeto, incluindo os principais arquivos e funções necessários para uma aplicação funcional e escalável.

## ESTRUTURA GERAL DE PASTAS:
Um projeto FastHTML pode começar simples, mas conforme cresce, sua organização se torna crucial. Aqui está um exemplo de estrutura básica:

```
CODIGO/
├── main.py
├── static/
│   ├── css/
│   │   └── estilo.css
│   ├── js/
│   │   └── interacoes.js
│   └── images/
├── templates/
│   ├── base.html
│   └── home.html
└── requirements.txt
```

## DESCRIÇÃO DOS COMPONENTES:
1. **`main.py`**: O arquivo principal da aplicação, contendo as rotas e configurações iniciais.
2. **`static/`**: Pasta para arquivos estáticos, como CSS, JavaScript e imagens.
3. **`templates/`**: Diretório para templates HTML reutilizáveis.
4. **`requirements.txt`**: Lista de dependências necessárias para rodar o projeto.

## CONSTRUINDO O PROJETO:
### PASSO 1: CRIANDO O ARQUIVO PRINCIPAL (`MAIN.PY`):
O arquivo `main.py` é o ponto de entrada da aplicação e geralmente contém:
- A inicialização do app.
- Definição das rotas.
- Configuração do servidor.

Exemplo:

```python
from fasthtml.common import fast_app, serve, load_template
from fasthtml.common import Div, P, H1

app, routes = fast_app()

# Rota principal
@routes("/")
def homepage():
    return Div(
        H1("Bem-vindo ao FastHTML!"),
        P("Estrutura básica de um projeto.")
    )

# Servidor rodando
serve()
```

## PASSO 2: ADICIONANDO TEMPLATES:
Os templates são úteis para separar o conteúdo HTML do código Python. Vamos criar a pasta `templates` e adicionar dois arquivos:
- **`base.html`**: Template base com estrutura compartilhada.
- **`home.html`**: Template específico para a página inicial.

**Exemplo: `templates/base.html`**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/css/estilo.css">
    <title>{% block title %}FastHTML App{% endblock %}</title>
</head>
<body>
    <header>
        <h1>FastHTML Framework</h1>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
```

**Exemplo: `templates/home.html`**
```html
{% extends "base.html" %}

{% block title %}Home{% endblock %}

{% block content %}
<p>Esta é a página inicial usando templates no FastHTML!</p>
{% endblock %}
```

## PASSO 3: USANDO O TEMPLATE NO CÓDIGO:
Atualize o `main.py` para usar os templates criados:

```python
@routes("/")
def homepage():
    return load_template("home.html")
```

## PASSO 4: ARQUIVOS ESTÁTICOS:
Crie estilos e scripts para sua aplicação dentro da pasta `static/`.

- **`static/css/estilo.css`**
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f9;
    color: #333;
}

header {
    background-color: #0073e6;
    color: white;
    padding: 10px 20px;
    text-align: center;
}
```

- **`static/js/interacoes.js`**
```javascript
console.log("Scripts carregados com sucesso!");
```

Para carregar esses arquivos no HTML, adicione as referências no template `base.html`:

```html
<link rel="stylesheet" href="/static/css/estilo.css">
<script src="/static/js/interacoes.js" defer></script>
```

## EXECUTANDO O PROJETO:
Após configurar a estrutura, inicie o servidor:

1. Instale as dependências:
   ```bash
   pip install fasthtml
   ```

2. Execute o projeto:
   ```bash
   python main.py
   ```

3. Acesse no navegador: [http://localhost:5001](http://localhost:5001).


## EXPLICAÇÃO DA ESTRUTURA:
- **Separação de Preocupações**: O uso de templates e pastas específicas para arquivos estáticos permite uma organização mais limpa e modular.
- **Flexibilidade**: Adicionar novos templates, rotas ou estilos fica mais simples com essa estrutura.
- **Escalabilidade**: Projetos maiores podem adotar convenções semelhantes para manter o código sustentável.

Essa estrutura é apenas uma base; conforme sua aplicação cresce, você pode incluir camadas adicionais, como integração com banco de dados, middleware e autenticação.

## CONCLUSÃO:
Com uma estrutura bem definida, é mais fácil gerenciar o desenvolvimento e a manutenção de projetos FastHTML. Este exemplo inicial permite que você compreenda como organizar pastas, arquivos estáticos e templates, preparando o terreno para funcionalidades mais avançadas.