from ctypes import alignment
import flet as ft
from flet import (
    Text,
    Page,
    TextField,
    FilledButton,
    Row,
    Divider,
    Column,
    Row,
    Container,
    padding,
    border_radius,
)


def main(page: Page):
    text_fields = {
        "contratante": TextField(label="Nome do Contratante", autofocus=True),
        "medida_judicial": TextField(label="Medida Judicial"),
        "outra_parte": TextField(label="Outra Parte"),
        "prolabore": TextField(label="Prolabore", prefix_text="R$ "),
        "exito": TextField(label="Exito", suffix_text=" %"),
        "foro": TextField(label="Foro"),
        "data_contrato": TextField(label="Data Contrato"),
    }

    def gera_contrato(e):
        for key, texto in text_fields.items():
            if not texto.value:
                texto.error_text = "Campo obrigatório"
            else:
                texto.error_text = None

            texto.update()

        page.update()

    titulo = Text(
        value="Gerador de Contrato de Prestação de Serviços Advocatícios",
        size=20,
        weight="bold",
    )

    fields_session = Container(
        content=Column(
            [
                Row(controls=[titulo]),
                Row(controls=[text_fields["contratante"]]),
                Row(
                    controls=[
                        text_fields["medida_judicial"],
                        text_fields["outra_parte"],
                    ]
                ),
                Row(controls=[text_fields["prolabore"], text_fields["exito"]]),
                Row(
                    controls=[text_fields["foro"], text_fields["data_contrato"]]
                ),
            ],
            alignment="center",
            spacing=10,
        ),
        alignment=ft.alignment.center,
        padding=padding.all(10),
        border_radius=border_radius.all(12),
    )

    btn_gerar = FilledButton(text="Gerar Contrato", on_click=gera_contrato)

    page.add(
        Container(
            content=Column(
                [fields_session, Divider(), Row(controls=[btn_gerar])]
            ),
            alignment=ft.alignment.center,
            width=800,
        )
    )


ft.app(target=main)
