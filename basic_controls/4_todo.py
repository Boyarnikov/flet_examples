import flet as ft

def main(page):
    def create_add_clicked(console_text):
        def inner(e):
            print(console_text)

        return inner


    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text="What's needs to be done?", width=300)
    page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))

    page.add(ft.ElevatedButton("HELLO WORLD", on_click=create_add_clicked("HELLO WORLD")))
    page.add(ft.ElevatedButton("HI", on_click=create_add_clicked("HI!")))

ft.app(target=main)