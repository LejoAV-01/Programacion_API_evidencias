import pyodbc
from estudiante import Estudiante
from curso import Curso


SERVER = 'ALEJANDRO\SQLEXPRESS' 
DATABASE = 'GestionEstudiantesCursos'
DRIVER = 'ODBC Driver 17 for SQL Server' 

class GestionSistema:
    def __init__(self):
        self.conn_str = (
            f'DRIVER={DRIVER};'
            f'SERVER={SERVER};'
            f'DATABASE={DATABASE};'
            f'Trusted_Connection=yes;'
        )
        self.conn = None
        self.cursor = None
        self._conectar()

    def _conectar(self):
        try:
            self.conn = pyodbc.connect(self.conn_str)
            self.cursor = self.conn.cursor()
            print("Conexión a la base de datos exitosa.")
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            print(f"Error al conectar a la base de datos: {sqlstate}")
            self.conn = None
            self.cursor = None

    def _desconectar(self):
        if self.conn:
            self.cursor.close()
            self.conn.close()
            print("Conexión a la base de datos cerrada.")

    def registrar_estudiante(self, estudiante):
        try:
            if self.conn and self.cursor:
                self.cursor.execute("INSERT INTO Estudiantes (Identificador, NombreCompleto, CorreoElectronico) VALUES (?, ?, ?)",
                                    estudiante.identificador, estudiante.nombre_completo, estudiante.correo_electronico)
                self.conn.commit()
                print(f"Estudiante {estudiante.nombre_completo} registrado.")
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            print(f"Error al registrar estudiante: {sqlstate}")
            self.conn.rollback()

    def registrar_curso(self, curso):
        try:
            if self.conn and self.cursor:
                self.cursor.execute("INSERT INTO Cursos (Identificador, Nombre, Descripcion, CantidadCreditos) VALUES (?, ?, ?, ?)",
                                    curso.identificador, curso.nombre, curso.descripcion, curso.cantidad_creditos)
                self.conn.commit()
                print(f"Curso {curso.nombre} registrado.")
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            print(f"Error al registrar curso: {sqlstate}")
            self.conn.rollback()

    def inscribir_estudiante_en_curso(self, estudiante_id, curso_id):
        try:
            if self.conn and self.cursor:
                self.cursor.execute("SELECT Identificador FROM Estudiantes WHERE Identificador = ?", estudiante_id)
                estudiante_existe = self.cursor.fetchone()
                self.cursor.execute("SELECT Identificador FROM Cursos WHERE Identificador = ?", curso_id)
                curso_existe = self.cursor.fetchone()

                if estudiante_existe and curso_existe:
                    self.cursor.execute("INSERT INTO Inscripciones (EstudianteIdentificador, CursoIdentificador) VALUES (?, ?)",
                                        estudiante_id, curso_id)
                    self.conn.commit()
                    print(f"Estudiante {estudiante_id} inscrito en el curso {curso_id}.")
                else:
                    print("Error: Estudiante o curso no encontrado.")
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            print(f"Error al inscribir estudiante en curso: {sqlstate}")
            self.conn.rollback()

    def listar_cursos_de_estudiante(self, estudiante_id):
        try:
            if self.conn and self.cursor:
                self.cursor.execute("""
                    SELECT c.Identificador, c.Nombre, c.Descripcion, c.CantidadCreditos
                    FROM Inscripciones i
                    JOIN Cursos c ON i.CursoIdentificador = c.Identificador
                    WHERE i.EstudianteIdentificador = ?
                """, estudiante_id)
                cursos = self.cursor.fetchall()
                if cursos:
                    print(f"Cursos del estudiante con ID {estudiante_id}:")
                    for curso in cursos:
                        print(f"  ID: {curso[0]}, Nombre: {curso[1]}, Descripción: {curso[2]}, Créditos: {curso[3]}")
                else:
                    print(f"El estudiante con ID {estudiante_id} no está inscrito en ningún curso.")
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            print(f"Error al listar cursos del estudiante: {sqlstate}")

    def eliminar_inscripcion(self, estudiante_id, curso_id):
        try:
            if self.conn and self.cursor:
                self.cursor.execute("DELETE FROM Inscripciones WHERE EstudianteIdentificador = ? AND CursoIdentificador = ?",
                                    estudiante_id, curso_id)
                if self.cursor.rowcount > 0:
                    self.conn.commit()
                    print(f"Inscripción del estudiante {estudiante_id} en el curso {curso_id} eliminada.")
                else:
                    print(f"No se encontró la inscripción del estudiante {estudiante_id} en el curso {curso_id}.")
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            print(f"Error al eliminar inscripción: {sqlstate}")
            self.conn.rollback()

    def __del__(self):
        self._desconectar()