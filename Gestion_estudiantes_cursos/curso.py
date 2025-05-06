class Curso:
    def __init__(self, identificador, nombre, descripcion, cantidad_creditos):
        self.identificador = identificador
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad_creditos = cantidad_creditos

    def __str__(self):
        return f"ID: {self.identificador}, Nombre: {self.nombre}, Créditos: {self.cantidad_creditos}"