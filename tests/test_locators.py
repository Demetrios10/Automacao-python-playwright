
def test_get_by_role(page):
    # Acessar a página inicial
    page.goto("https://automationexercise.com/")
    # Acessar a página de login
    page.get_by_role("link", name="Signup / Login").click() 
    # Clicar no botão de login sem preencher os campos para verificar a mensagem de erro
    page.get_by_role("button", name="Login").click()
    # Clicar no botão de cadastro sem preencher os campos para verificar a mensagem de erro
    page.get_by_role("button", name="Signup").click() 

    
def test_get_by_text(page):
    # Acessar a página inicial e clicar no link "Home" para verificar se o link está funcionando corretamente
    page.goto("https://automationexercise.com/") 
    # Adicionar uma pausa para permitir que a página carregue completamente antes de interagir com os elementos
    page.pause()
    # Acessar a página inicial e clicar no link "Website for automation practice" para verificar se o link está funcionando corretamente
    page.get_by_text("Full-Fledged practice website for").click()