class Estudiante:
#Metodo Constructor
    total_estudiantes = 0
    def __init__(self,nombre:str,codigo:str,ciclo:int):
        self.nombre = nombre
        self.codigo = codigo
        self.ciclo = ciclo

        #atributo de clase para contar el total de estudiantes
        Estudiante.total_estudiantes +=1

#Validaciones
        if not (1<= self.ciclo<=10):
            raise ValueError
    
    def __str__(self):
         return  f"[{self.codigo}] {self.nombre} (Ciclo {self.ciclo})"
    
    def __repr__(self):
        return f"Estudiante({self.nombre!r},{self.codigo!r},{self.ciclo!r})"

    def __eq__(self,other):
        if not isinstance (other, Estudiante):
            return NotImplemented
        return self.codigo == other.codigo
    

Est1 = Estudiante("Juan Kiro","22435416",10)
Est2 = Estudiante("Julio Quiroz","22435417",3)
Est3 = Estudiante("Brian Alvarado","54356241",6)


print(Estudiante.total_estudiantes)

# print(Est1)
# print(Est2)
# print(Est1 == Est2)
# if Est1 == Est2 :
#     print ("Ese estudiante ya existe por lo tanto no puede ser registrado.")

class Curso:
    def __init__(self,nombre:str,codigo:str,creditos:int,ciclo_minimo:int,cupo_maximo:int):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
        self.ciclo_minimo = ciclo_minimo
        self.cupo_maximo = cupo_maximo
        self.inscritos = []

    def hay_cupo(self):
        return len(self.inscritos) < self.cupo_maximo
    
    def esta_inscrito(self,estudiante):
        return estudiante in self.inscritos
    
    def inscribir(self,estudiante):
        #Hay cupo disponible?
        if not self.hay_cupo():
            return False
        
        #El estudiante esta inscrito en el curso actualmente?
        if self.esta_inscrito(estudiante):
            print("El estudiante ya se encuentra inscrito")
            return False
        
        #si el ciclo es el minimo para 
        if estudiante.ciclo < self.ciclo_minimo:
            print("El estudiante no cumple con el ciclo minimo")
            return False
        
        self.inscritos.append(estudiante)
        return True
    
    #Cantidad de Inscritos
    def cantidad_inscritos(self):
        return len(self.inscritos)
    
    #Mostrar Curso (DATA)
    def __str__(self):
        return f"[{self.codigo}]{self.nombre}({self.creditos} cred.) - {self.cantidad_inscritos()}/{self.cupo_maximo}"
    

class SistemaMatricula:
    def __init__(self,semestre:str):
        self.semestre = semestre
        self.estudiantes = {}
        self.cursos = {}

    def agregar_estudiante(self,estudiante):
        #Validando si ya existe
        if estudiante.codigo in self.estudiantes :
            print ("el estudiantes ya existe")
        else:
            self.estudiantes[estudiante.codigo] = estudiante

    def agregar_curso(self,curso):
        self.cursos[curso.codigo] = curso

    def matricular(self,codigo_estudiante,codigo_curso):
        #Si el codigo del estudiane no esta en mi diccionario de estudiantes
        if codigo_estudiante not in self.estudiantes:
            print("El estudiante no existe")
            return 
        #Si el codigo del curso no esta en mi diccionario de cursos 
        if codigo_curso not in self.cursos:
            print("El curso no existe o no habido")
            return
        #Obtener Objetos
        estudiante = self.estudiantes[codigo_estudiante]
        curso = self.cursos[codigo_curso]

    #INSCRIBIR
        curso.inscribir(estudiante)
        
    #Cursos del estudiante
    def cursos_del_estudiante(self,codigo_estudiante):
        resultado = [] #Lista para almacenar

        for curso in self.cursos.values(): #Recorre todos los cursos
            for est in curso.inscritos: #Entra a los inscritos de cada curso
                if est.codigo == codigo_estudiante: #Compara codigo
                    resultado.append(curso.nombre) #Agrega el nombre del curso a la lista
                    
        return resultado
    
    def reporte_general(self):
        print("Semestre :",self.semestre)
        print("Total de estudiantes :",len(self.estudiantes))
        print("Total de Cursos: ", len(self.cursos))

        for curso in self.cursos.values():
            print(f"{curso.nombre} - {len(curso.inscritos)}/{curso.cupo_maximo}")


if __name__ == "__main__":

    # 1. Crear sistema
    sistema = SistemaMatricula("2026-I")

    # 2. Crear estudiantes
    e1 = Estudiante("Juan Perez", "1001", 1)
    e2 = Estudiante("Maria Lopez", "1002", 3)
    e3 = Estudiante("Carlos Ruiz", "1003", 4)
    e4 = Estudiante("Ana Torres", "1004", 6)

    # Agregar estudiantes
    sistema.agregar_estudiante(e1)
    sistema.agregar_estudiante(e2)
    sistema.agregar_estudiante(e3)
    sistema.agregar_estudiante(e4)

    # Intentar duplicado
    sistema.agregar_estudiante(e1)

    print("\n--- Cursos ---")

    # 3. Crear cursos
    c1 = Curso("Introducción a la Ingeniería", "C101", 3, 1, 40)
    c2 = Curso("Estructura de Datos", "C102", 4, 3, 35)
    c3 = Curso("Lenguaje de Programación II", "C103", 4, 4, 30)

    # Agregar cursos
    sistema.agregar_curso(c1)
    sistema.agregar_curso(c2)
    sistema.agregar_curso(c3)

    print("\n--- Matrículas ---")

    # 4. Matrículas correctas (mínimo 6)
    sistema.matricular("1001", "C101")
    sistema.matricular("1002", "C101")
    sistema.matricular("1002", "C102")
    sistema.matricular("1003", "C102")
    sistema.matricular("1003", "C103")
    sistema.matricular("1004", "C103")

    # 5. Error: estudiante ciclo bajo
    print("\n--- Error de ciclo ---")
    sistema.matricular("1001", "C103")  # ciclo 1 en curso de ciclo 4

    # 6. Error: duplicado
    print("\n--- Error duplicado ---")
    sistema.matricular("1002", "C101")

    # 7. Mostrar cursos de un estudiante
    print("\n--- Cursos de Maria Lopez ---")
    cursos = sistema.cursos_del_estudiante("1002")
    print(cursos)

    # 8. Reporte general
    print("\n--- Reporte General ---")
    sistema.reporte_general()





    