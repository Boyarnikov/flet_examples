import flet as ft


class MyButton(ft.ElevatedButton):
    def __init__(self, text, on_click):
        super().__init__()
        self.bgcolor = ft.colors.ORANGE_300
        self.color = ft.colors.GREEN_800
        self.text = text
        self.on_click = on_click


def main(page: ft.Page):
    def ok_clicked(e):
        print("OK clicked")

    def cancel_clicked(e):
        print("Cancel clicked")

    page.add(
        MyButton(text="OK", on_click=ok_clicked),
        MyButton(text="Cancel", on_click=cancel_clicked),
        ft.ElevatedButton(text="basic")
    )


ft.app(target=main)