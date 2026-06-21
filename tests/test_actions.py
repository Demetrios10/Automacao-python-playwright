# usando click para clicar em um elemento
def test_click(page):
    page.goto("https://automationexercise.com/")
    page.pause()
    # clicando escolhendo posição
    page.get_by_role("link", name="Website for automation").click(position= {"x":10 ,"y":10})