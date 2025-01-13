import flet as ft

def main(page: ft.Page):
    page.title = "My CMS"
    page.add(ft.Text("Welcome to the CMS! Please log in to continue."))

ft.app(target=main)