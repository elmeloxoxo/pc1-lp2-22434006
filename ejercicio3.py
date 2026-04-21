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
        pass