import pytest
import pytest_html

def test_abrir_google(page):
    page.goto("https://www.google.com")
    print(page.title())
    assert "Google" in page.title()