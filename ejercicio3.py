class Estudiante:
#Metodo Constructor
    total_estudiantes = 0
    def __init__(self,nombre:str,codigo:str,ciclo:int):
        self.nombre = nombre
        self.codigo = codigo
        self.ciclo = ciclo

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

print(Est1)
print(Est2)

# print(Est1 == Est2)
# if Est1 == Est2 :
#     print ("Ese estudiante ya existe por lo tanto no puede ser registrado.")


    
