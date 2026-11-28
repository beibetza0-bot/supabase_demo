import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')


class InsertarContacto:

    def GET(self):
        return render.insertar_contacto()  # type: ignore

    def POST(self):
        formulario = web.input(nombre="", email="", telefono="", foto={})

        print("DEBUG foto:", type(formulario.foto), getattr(formulario.foto, "filename", None))

        modelo = ModelContactos()
        foto = modelo.guardarFoto(formulario.foto)
        print("DEBUG foto guardada como:", foto)
        modelo.insertarContacto(formulario.nombre, formulario.email, formulario.telefono, foto)

        return render.contacto_guardado()  # type: ignore
    