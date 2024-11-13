# 07 - Lista de Itens usando ListView
import flet as ft


def main(page: ft.Page):
    page.title = "ListView"
    label = ft.Text("ListView")
    lista = ft.ListView(spacing=10, expand=True)
    for i in range(100):
        lista.controls.append(ft.Text(f"Estamos na linha {i}"))

    page.add(label, lista)


ft.app(target=main)
