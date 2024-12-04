# SIMPLES BOTÕES COM FLASTHTML
Este projeto é uma aplicação web simples criada com o **FastHTML**, uma biblioteca minimalista que utiliza o **Hypertext Preprocessor (HTMX)** para criar páginas dinâmicas e interativas. A aplicação consiste em uma página inicial com três botões que, ao serem clicados, mudam o conteúdo da página sem necessidade de recarregar toda a página. O fluxo da aplicação é controlado por rotas que respondem a diferentes URLs.

## O QUE O APP FAZ?
- **Página Inicial**: Exibe três botões que, ao serem clicados, alteram o texto exibido na página.
- **Mudança de Conteúdo Dinâmico**: Cada botão está associado a uma URL específica que, quando acessada, retorna uma nova mensagem com um estilo diferente.
- **Interatividade**: O comportamento da página é manipulado sem recarregar a página, aproveitando-se da tecnologia HTMX para realizar requisições AJAX no backend e atualizar o conteúdo da página dinamicamente.

## EXECUTANDO ESSE PROJETO:
1. **Instalação das Dependências::**
   - Entre no diretório `PROJETO` e execute o comando:

   ```bash
   pip install -r requirements.txt
   ```

2. **Execução do Aplicativo:**
   - Para executar o arquivo Python, utilize o comando abaixo no terminal, dentro do diretório `./CODIGO`:
   ```bash
   python main.py
   ```

3. **Acesse a página inicial:** 
   - Acesse [http://localhost:5001](http://localhost:5001) no navegador. 

---

## EXPLICAÇÃO DO CÓDIGO:
### IMPORTAÇÕES:
```python
from fasthtml.common import fast_app, serve
from fasthtml.common import Div, P, Button
```
1. **`from fasthtml.common import fast_app, serve`**: 
   - **`fast_app`**: Função que inicializa a aplicação FastHTML. Ela retorna dois objetos: o servidor da aplicação e as rotas configuradas para a aplicação.
   - **`serve`**: Função que inicia o servidor web. Ele ficará escutando as requisições HTTP e retornando as respostas conforme as rotas definidas.

2. **`from fasthtml.common import Div, P, Button`**: 
   - **`Div`**: Componente HTML `div`, utilizado para agrupar elementos.
   - **`P`**: Componente HTML `p`, usado para definir parágrafos de texto.
   - **`Button`**: Componente HTML `button`, utilizado para criar botões na página.

### INICIALIZAÇÃO DA APLICAÇÃO:
```python
# Instância da aplicação e configuração das rotas
app, routes = fast_app()
```
- **`fast_app()`**: Inicializa a aplicação FastHTML e cria o objeto `app` que representa a aplicação, bem como o objeto `routes`, que contém as rotas que serão mapeadas para funções específicas.

### FUNÇÃO DA PÁGINA INICIAL:
```python
# Função da página inicial
@routes("/")
def homepage():
    return Div(
        # Botões para mudar as mensagens
        Button("Clique para mudar a mensagem", hx_get="/mudar", hx_target="p", style="margin-bottom: 10px; padding: 10px 20px; font-size: 16px;"),
        Button("Clique para ver outra mensagem", hx_get="/outra", hx_target="p", style="margin-bottom: 10px; padding: 10px 20px; font-size: 16px;"),
        Button("Clique para mais interatividade", hx_get="/interatividade", hx_target="p", style="margin-bottom: 10px; padding: 10px 20px; font-size: 16px;"),
        
        P("Bem-vindo ao FastHTML!", style="font-size: 24px; margin-bottom: 20px;"),
        style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100vh; text-align: center;"
    )
```
- **`@routes("/")`**: O decorador `@routes` associa a função `homepage` à rota `/` (a página inicial). Quando um usuário acessar a URL raiz da aplicação, a função `homepage()` será executada.
- **`Div(...)`**: A função `homepage()` retorna um `Div`, que agrupa os elementos HTML dentro dele.
- **Botões**:
  - **`Button("Clique para mudar a mensagem", hx_get="/mudar", hx_target="p", ...)`**: Cria um botão. O atributo `hx_get="/mudar"` faz com que, ao clicar no botão, o navegador faça uma requisição GET para a URL `/mudar`. O atributo `hx_target="p"` indica que o conteúdo retornado será inserido dentro do elemento `<p>`.
  - A mesma lógica se aplica para os outros botões, mas com as rotas `/outra` e `/interatividade`.
- **`P("Bem-vindo ao FastHTML!")`**: Exibe o texto "Bem-vindo ao FastHTML!" na página.
- **`style="..."`**: A propriedade `style` aplica um conjunto de estilos CSS para centralizar o conteúdo na página.

### FUNÇÕES PARA AS OUTRAS ROTAS:
```python
# Função para mudar a mensagem
@routes("/mudar")
def mudar_mensagem():
    return P("Obrigado por explorar o FastHTML!", style="font-size: 20px; color: green;")

# Função para outra mensagem
@routes("/outra")
def outra_mensagem():
    return P("Você clicou no segundo botão!", style="font-size: 20px; color: blue;")

# Função para interatividade
@routes("/interatividade")
def interatividade():
    return P("Agora você tem mais interatividade!", style="font-size: 20px; color: red;")
```
- **`@routes("/mudar")`**: A função `mudar_mensagem()` é mapeada para a rota `/mudar`. Quando um usuário clica no botão associado a essa rota, o texto na página muda para "Obrigado por explorar o FastHTML!".
- **`@routes("/outra")`**: Similar à função anterior, mas exibe a mensagem "Você clicou no segundo botão!".
- **`@routes("/interatividade")`**: Exibe a mensagem "Agora você tem mais interatividade!" quando o botão correspondente é clicado.

Em cada uma dessas funções, o texto retornado está envolto por um elemento `P`, que tem um estilo específico para cada mensagem (como cor e tamanho da fonte).

### INICIALIZAÇÃO DO SERVIDOR:
```python
# Inicializa o servidor
serve()
```
- **`serve()`**: Essa função inicia o servidor web da aplicação FastHTML. O servidor começa a escutar as requisições HTTP nas rotas definidas e retorna as respostas apropriadas para cada uma delas.

### RESUMO GERAL:
- Este projeto cria uma aplicação web simples com 3 botões na página inicial.
- Quando um usuário clica em um botão, uma nova mensagem é exibida na página sem recarregar o navegador, graças à integração com HTMX.
- O código utiliza o FastHTML, que é uma biblioteca que simplifica a criação de páginas dinâmicas com Python.

Esse tipo de estrutura permite criar sites rápidos e interativos com muito menos código do que frameworks tradicionais, como Flask ou Django, aproveitando a simplicidade de uma biblioteca minimalista como o FastHTML.