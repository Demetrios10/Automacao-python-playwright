
def test_get_by_role(page):
    page.goto("https://automationexercise.com/") # Acessar a página inicial
    page.get_by_role("link", name="Signup / Login").click() # Acessar a página de login
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="Signup").click()
    
    # o comando get_by_role é utilizado para localizar elementos com base em seu papel (role) e nome (name).
    # No exemplo acima, o código acessa a página inicial do site "https://automationexercise.com/",
    # clica no link "Signup / Login" para acessar a página de login, em seguida, clica nos botões "Login" e "Signup".
    # O comando get_by_role é útil para localizar elementos de forma mais semântica, 
    # permitindo que os testes sejam mais legíveis e menos propensos a 
    # falhas devido a mudanças na estrutura do DOM.