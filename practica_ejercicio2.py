#El puerto de masusa en iquitos necesita un sistema para registrar embarcaciones y sus viajes
class Motor :
    def __init__(self,marca:str,potencia_hp:int):
        self.marca = marca
        self.potencia_hp = potencia_hp

    def __str__(self):
        return f"{self.marca} {self.potencia_hp}HP"
    

#Pruebas de __str__
# mot1 = Motor("Honda",600)
# print(mot1)

class Embarcacion:
    total_embarcaciones = 0
    def __init__(self,nombre:str,tipo:str,capacidad_pasajeros:int,ruta:str,marca_motor:str,potencia_motor:int):
        self.nombre = nombre
        self.tipo = tipo
        self.capacidad_pasajeros = capacidad_pasajeros
        self.ruta = ruta
        self.motor = Motor(marca_motor,potencia_motor)

        Embarcacion.total_embarcaciones =+ 1

        def es_grande(self):
            if self.capacidad_pasajeros > 100:
                return True
            
        def descripcion(self):
            return (f"Nombre: {self.nombre}, Tipo: {self.tipo}"
                    f"Capacidad:{self.capacidad} pasajeros ,Ruta: {self.ruta}"
                    f"Motor: {self.motor}"  
                    )
        def __str__(self):
            return f"[{self.tipo}] {self.nombre} - {self.ruta} (Motor: {self.motor})"

            


    