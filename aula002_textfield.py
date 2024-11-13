import flet as ft


def main(page):
    def login(e):
        if not entrada_nome.value:
            entrada_nome.error_text = "Por favor preencha o seu nome."
            page.update()
        if not entrada_senha.value:
            entrada_senha.error_text = "Campo de senha obrigatório."
            page.update()

        else:
            nome = entrada_nome.value
            senha = entrada_senha.value
            # print(f"Nome: {nome}\nSenha: {senha}")
            page.clean()
            page.add(ft.Text(f"Ola, {nome}\n seja bem vindo a nossa aplicação"))

    entrada_nome = ft.TextField(label="Digite o seu Nome")
    entrada_senha = ft.TextField(label="Digite a sua Senha")
    button = ft.ElevatedButton("Clique em mim!!!", on_click=login)

    page.add(entrada_nome, entrada_senha, button)


ft.app(target=main)
