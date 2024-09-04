import flet as ft
import time

def main(page: ft.Page):
    t = ft.Text()
    page.add(t)  # it's a shortcut for page.controls.append(t) and then page.update()

    page.add(
        ft.Row(controls=[
            ft.Text("A"),
            ft.Text("B"),
            ft.Text("C")
        ])
    )

    page.add(
        ft.Row(controls=[
            ft.TextField(label="Your name"),
            ft.ElevatedButton(text="Say my name!")
        ])
    )

    for i in range(10):
        page.controls.append(ft.Text(f"Line {i}"))
        if i > 4:
            page.controls.pop(0)
        page.update()
        time.sleep(1)


ft.app(target=main)