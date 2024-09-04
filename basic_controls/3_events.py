import flet as ft
import time

def main(page: ft.Page):
    t = ft.Text()
    page.add(t)  # it's a shortcut for page.controls.append(t) and then page.update()

    def button_clicked(e: ft.ControlEvent):
        print(e.data)
        page.add(ft.Text("Clicked!"))

    page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))


ft.app(target=main)
