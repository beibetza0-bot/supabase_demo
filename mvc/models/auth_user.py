import os
from supabase import create_client, Client
from dotenv import load_dotenv
import logging

load_dotenv()

logger = logging.getLogger(__name__)

class AuthUsers:

    def __init__(self) -> None:
        try:
            self.supabase: Client = create_client(
                os.environ.get("SUPABASE_URL", ""),
                os.environ.get("SUPABASE_KEY", "")
            )
        except Exception as error:
            logger.error(f"ERROR 100: {str(error)}")
            print(f"ERROR 100: {str(error)}")

    def iniciarSesion(self, email: str, password: str) -> str | None:
        try:
            response = self.supabase.auth.sign_in_with_password(
                {"email": email, "password": password}
            )
            return response.session.access_token  # type: ignore
        except Exception as error:
            logger.error(f"ERROR 101: {str(error)}")
            print(f"ERROR 101: {str(error)}")
            return None

    def registrarUsuario(self, email: str, password: str) -> str | None:
        try:
            response = self.supabase.auth.sign_up(
                {"email": email, "password": password}
            )
            print("Usuario registrado exitosamente")
            return response.user.id  # type: ignore
        except Exception as error:
            logger.error(f"ERROR 102: {str(error)}")
            print(f"ERROR 102: {str(error)}")
            return None
        