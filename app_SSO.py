import flet as ft
from descope import DescopeClient
from flet.security import require_authentication
import flet as ft
from descope import DescopeClient

client = DescopeClient(project_id="P2raBpmJgUQnO1elyxDopp3VYxh0")

def main(page: ft.Page):
    def login_user():
        sso_url = client.sso.get_login_url()
        page.add(ft.Text(f"SSO Login URL: {sso_url}"))

    login_button = ft.ElevatedButton(text="Login with SSO", on_click=lambda _: login_user())
    page.add(login_button)

@require_authentication
def protected_page(page: ft.Page):
    page.add(ft.Text("Welcome to the protected page!"))

def profile_page(page: ft.Page):
    user_info = client.me()
    page.add(ft.Text(f"Welcome {user_info['name']}!"))

def logout_user(page: ft.Page):
    client.logout()
    page.add(ft.Text("You have been logged out."))

# Persistent login
def restore_session(page: ft.Page):
    session_token = client.auth.get_saved_token()
    if session_token:
        page.add(ft.Text("Welcome back!"))
    else:
        page.add(ft.Text("Please log in."))

ft.app(target=main)