from fasthtml.common import fast_app, serve, Div, H1, H2, P, A, Img, Section

app, routes = fast_app()

# Componente Card de Projeto
def ProjectCard(title, description, image_url, link):
    return Div(
        Img(src=image_url, alt=f"Imagem do projeto {title}", class_="project-image"),
        H2(title),
        P(description),
        A("Ver Projeto", href=link, class_="project-link"),
        class_="project-card"
    )

# Página Principal
@routes("/")
def portfolio():
    about_section = Section(
        H1("Meu Portfólio"),
        P("Bem-vindo ao meu portfólio! Aqui você encontra meus principais projetos."),
        class_="about-section"
    )
    project_gallery = Div(
        ProjectCard(
            "Projeto 1",
            "Descrição do primeiro projeto.",
            "/static/images/FOTO.png",
            "https://example.com/projeto1"
        ),
        ProjectCard(
            "Projeto 2",
            "Descrição do segundo projeto.",
            "/static/images/FOTO.png",
            "https://example.com/projeto2"
        ),
        ProjectCard(
            "Projeto 3",
            "Descrição do terceiro projeto.",
            "/static/images/FOTO.png",
            "https://example.com/projeto3"
        ),
        class_="project-gallery"
    )
    return Div(about_section, project_gallery, class_="container")

serve()
