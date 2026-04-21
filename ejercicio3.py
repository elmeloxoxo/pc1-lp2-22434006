class Estudiante:
    total_estudiantes = 0
    def __init__(self,nombre=str,codigo=str,ciclo=int):
        self.nombre = nombre
        self.codigo = codigo
        self.ciclo = ciclo

        if not (1<= self.ciclo<=10):
            raise ValueError

    
