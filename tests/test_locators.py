
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
    page.goto("https://automationexercise.com/")
    page.pause()
    page.get_by_text("Full-Fledged practice website for").click()

# Acessar a página de login e preencher o campo de email usando o placeholder "Email Address"
def test_get_by_placeholder(page):
    page.goto("https://automationexercise.com/login")
    page.pause()
    page.get_by_placeholder("Name").fill("Teste")

def test_get_by_label(page):
    page.goto("https://bootswatch.com/default/")
    page.pause()
    page.get_by_label("Valid input" , exact=True).fill("Teste")
    page.get_by_label("Recipient's username" , exact=True).fill("Teste")

def test_get_by_title(page):
    page.goto("https://bootswatch.com/default/")
    page.pause()
    page.get_by_title("Source Title").nth(1).click()