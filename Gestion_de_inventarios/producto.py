class Producto:
    def __init__(self, identificador, nombre, descripcion, precio, cantidad):
        self.identificador = identificador
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad

    def actualizar(self, nombre=None, descripcion=None, precio=None, cantidad=None):
        if nombre is not None:
            self.nombre = nombre
        if descripcion is not None:
            self.descripcion = descripcion
        if precio is not None:
            self.precio = precio
        if cantidad is not None:
            self.cantidad = cantidad

    def __str__(self):
        return f"{self.identificador}: {self.nombre} - {self.descripcion} - ${self.precio:.2f} - Stock: {self.cantidad}"
