from mvc.models.model_contactos import ModelContactos

modelo = ModelContactos()
print(modelo.insertarContacto("Prueba", "prueba@email.com", "7770000000"))
print(modelo.obtenerContactos())
