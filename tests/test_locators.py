def test_get_by_role(page):
    page.goto("https://automationexercise.com/")
    page.pause()
    page.get_by_role("link", name="Signup / Login").click()
    page.get_by_role("button", name="Login").click()
    

# isso é um teste de exemplo para demonstrar o uso do método get_by_role do Playwright. Ele navega até a página de login e tenta clicar no botão de login sem preencher os campos de email e senha, o que deve resultar em uma mensagem de erro.
    
    