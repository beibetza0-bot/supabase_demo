import os

from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

class ModelContactos():

    def __init__(self) -> None:
        try:
            self.supabase: Client = create_client(
                os.environ.get("SUPABASE_URL"),
                os.environ.get("SUPABASE_KEY")
            )
        except Exception as error:
            print(f"ERROR 100: {error.args[0]}")

    def guardarFoto(self, archivo):
        if hasattr(archivo, "filename") and archivo.filename:
            nombre_archivo = os.path.basename(archivo.filename)
            with open("static/imagenes/" + nombre_archivo, "wb") as f:
                f.write(archivo.raw)
            return nombre_archivo
        return None

    def obtenerContactos(self):
        response = self.supabase.table("contactos").select("*").execute()
        return response.data

    def buscarContacto(self, id_contacto):
        response = self.supabase.table("contactos").select("*").eq("id", id_contacto).execute()
        return response.data

    def insertarContacto(self, nombre, email, telefono, foto=None):
        response = self.supabase.table("contactos").insert({
            "nombre": nombre,
            "email": email,
            "telefono": telefono,
            "foto": foto
        }).execute()
        return response.data

    def actualizarContacto(self, id_contacto, nombre, email, telefono, foto=None):
        datos = {
            "nombre": nombre,
            "email": email,
            "telefono": telefono
        }
        if foto:
            datos["foto"] = foto

        response = self.supabase.table("contactos").update(datos).eq("id", id_contacto).execute()
        return response.data

    def borrarContacto(self, id_contacto):
        response = self.supabase.table("contactos").delete().eq("id", id_contacto).execute()
        return response.data
                   