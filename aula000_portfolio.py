from fastapi import background
import flet as ft


def main(page: ft.Page):
    page.title = "Meu portfólio"
    page.scroll = "auto"
    page.theme_mode = "light"
    page.horizontal_alignment = "center"

    # Definição das cores principais
    primary_color = ft.colors.INDIGO_400
    background_color = ft.colors.WHITE
    accent_color = ft.colors.BLUE_100

    page.bgcolor = background_color

    about_session = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Olá meu nome é ...",
                    size=30,
                    weight="bold",
                    color=primary_color,
                ),
                ft.Text(
                    "Djalma Feitosa",
                    size=40,
                    weight="bold",
                    color=primary_color,
                ),
                ft.Divider(),
                ft.ElevatedButton(
                    "Ver Projetos",
                    color=background_color,
                    bgcolor=primary_color,
                ),
            ]
        ),
        alignment=ft.alignment.center,
        padding=ft.padding.all(40),
        border_radius=ft.border_radius.all(12),
        bgcolor=accent_color,
    )

    projects_list = [
        {"title": "Projeto 1", "description": "Descrição do projeto 1"},
        {"title": "Projeto 2", "description": "Descrição do projeto 2"},
        {"title": "Projeto 3", "description": "Descrição do projeto 3"},
    ]
    project_session = ft.Container(
        content=ft.Column(
            [
                ft.Text("Projetos", size=38, color=primary_color),
                ft.Text(
                    "Veja aqui alguns dos meus projetos mais recentes, pode clicar em ver mais para navegar.",
                    size=20,
                    color=ft.colors.BLACK54,
                ),
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text(
                                        project["title"],
                                        size=24,
                                        weight="bold",
                                        color=primary_color,
                                    ),
                                    ft.Text(
                                        project["description"],
                                        size=16,
                                        color=ft.colors.BLACK54,
                                    ),
                                ],
                                spacing=10,
                            ),
                            padding=ft.padding.all(10),
                            bgcolor=accent_color,
                            border_radius=ft.border_radius.all(10),
                            width=200,
                            height=150,
                        )
                        for project in projects_list
                    ],
                    run_spacing=10,
                    spacing=10,
                ),
            ],
            spacing=10,
        ),
        padding=ft.padding.symmetric(horizontal=20, vertical=40),
    )

    contact_session = ft.Container()

    footer = ft.Row(
        [
            ft.Text(
                "Desenvolvido por @setprogramacao :: 2024",
                color=ft.colors.BLACK54,
            )
        ],
        alignment="center",
    )

    page.add(
        ft.Container(
            content=ft.Column(
                [
                    about_session,
                    ft.Divider(),
                    project_session,
                    ft.Divider(),
                    contact_session,
                    ft.Divider(),
                    footer,
                ]
            ),
            width=800,
            alignment=ft.alignment.center,
        )
    )


ft.app(target=main)
