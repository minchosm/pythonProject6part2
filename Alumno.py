class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        if self.nota >= 5:
            return "Enhorabuena has aprobado"
        else:
            return "Has suspendido"



