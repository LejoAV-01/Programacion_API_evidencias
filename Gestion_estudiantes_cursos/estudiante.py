class Estudiante:
    def __init__(self, identificador, nombre_completo, correo_electronico):
        self.identificador = identificador
        self.nombre_completo = nombre_completo
        self.correo_electronico = correo_electronico

    def __str__(self):
        return f"ID: {self.identificador}, Nombre: {self.nombre_completo}, Correo: {self.correo_electronico}"