import flet as ft

def main(page):
    first_name = ft.ElevatedButton()
    last_name = ft.ElevatedButton()

    c = ft.Column(controls=[
        first_name,
        last_name
    ])

    #first_name.disabled = True
    c.disabled = True
    page.add(c)
ft.app(target=main)