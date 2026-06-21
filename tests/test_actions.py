# usando click para clicar em um elemento
def test_click(page):
    page.goto("https://automationexercise.com/")
    page.pause()
    # clicar com o botão direito do mouse
    page.get_by_role("link", name="Website for automation").click(button='right')