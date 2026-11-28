import web

from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class ActualizarContacto:

    def GET(self):
        datos = web.input(id=None)
        contacto = None

        if datos.id:
            modelo = ModelContactos()
            resultado = modelo.buscarContacto(datos.id)
            if resultado:
                contacto = resultado[0]

        return render.actualizar_contacto(contacto)

    def POST(self):
        datos = web.input(id=None, nombre="", email="", telefono="", foto={})

        if datos.id:
            modelo = ModelContactos()
            foto = modelo.guardarFoto(datos.foto)
            modelo.actualizarContacto(datos.id, datos.nombre, datos.email, datos.telefono, foto)

        raise web.HTTPError('303 See Other', {'Location': '/contactos'})
     