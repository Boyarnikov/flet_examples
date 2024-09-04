import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    prev_correct = 0

    def validate_int(e):
        nonlocal prev_correct
        print("Changerd text")
        try:
            int(txt_number.value)
            prev_correct = txt_number.value
        except ValueError:
            txt_number.error_text = "Здесь должно быть целове число"
            txt_number.value = prev_correct
            page.update()


    txt_number = ft.TextField(value="0", text_align="right", width=100, on_change=validate_int)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)