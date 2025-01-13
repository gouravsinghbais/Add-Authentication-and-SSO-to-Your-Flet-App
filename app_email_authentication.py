import flet as ft
from descope import DescopeClient

client = DescopeClient(project_id="your_project_id")

def main(page: ft.Page):
    def login_user(email):
        try:
            client.otp.send_email(email)
            page.add(ft.Text("OTP sent to your email!"))
        except Exception as e:
            page.add(ft.Text(f"Error: {e}"))

    email_input = ft.TextField(label="Email")
    login_button = ft.ElevatedButton(text="Login", on_click=lambda _: login_user(email_input.value))
    page.add(email_input, login_button)

ft.app(target=main)