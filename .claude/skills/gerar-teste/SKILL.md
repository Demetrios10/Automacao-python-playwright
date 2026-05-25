---
description: Gera testes automatizados em Python com Playwright e Pytest seguindo o padrao do projeto
invocation: user
---

# Gerar Teste Automatizado

Voce e um especialista em automacao de testes com Playwright + Python.
O site alvo dos testes e o https://automationexercise.com/

## Regras obrigatorias

1. Page Object Model: Sempre crie uma classe POM separada em pages/
2. Seletores: Priorize get_by_role(), get_by_placeholder(), get_by_text(). Evite CSS/XPath frageis
3. Fixtures: Use a fixture page do conftest.py
4. Nomenclatura: snake_case em portugues (ex: test_login_com_sucesso)
5. Assertions: Use expect() do Playwright, nunca assert com is_visible()
6. Estrutura do teste: Um arquivo por funcionalidade em tests/
7. Dados de teste: Use dados realistas (nomes, emails, enderecos)
8. Independencia: Cada teste deve funcionar isoladamente, sem depender de outros

## Fluxo de trabalho

1. Use o Playwright MCP para navegar ate a pagina alvo
2. Inspecione os elementos interativos (campos, botoes, links, textos)
3. Crie o Page Object em pages/nome_da_pagina.py
4. Crie o teste em tests/test_nome_da_funcionalidade.py
5. Execute o teste com pytest --headed para validar visualmente

Se o argumento $ARGUMENTS for fornecido, use-o como a URL e descricao da pagina alvo.

## Exemplo de Page Object

O Page Object gerado deve seguir este padrao (exemplo real da pagina de login):

```python
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.campo_email = page.get_by_placeholder("Email Address")
        self.campo_senha = page.get_by_placeholder("Password")
        self.botao_login = page.get_by_role("button", name="Login")

    def fazer_login(self, email, senha):
        self.campo_email.fill(email)
        self.campo_senha.fill(senha)
        self.botao_login.click()
```

## Exemplo de Teste

O teste gerado deve seguir este padrao:

```python
from playwright.sync_api import expect
from pages.login_page import LoginPage

def test_login_com_sucesso(page):
    page.goto("https://automationexercise.com/login")
    login = LoginPage(page)
    login.fazer_login(email="teste@teste.com", senha="123456")
    expect(page.get_by_text("Logged in as")).to_be_visible()
```