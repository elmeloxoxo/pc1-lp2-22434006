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

        Embarcacion.total_embarcaciones += 1

    def es_grande(self):
        if self.capacidad_pasajeros > 100:
            return True
            
    def descripcion(self):
        return (f"Nombre: {self.nombre}, Tipo: {self.tipo}"
                f"Capacidad:{self.capacidad_pasajeros} pasajeros ,Ruta: {self.ruta}"
                f"Motor: {self.motor}"  
                    )
    def __str__(self):
        return f"[{self.tipo}] {self.nombre} - {self.ruta} (Motor: {self.motor})"
        
    def __eq__(self,other):
        if isinstance (other, Embarcacion):
            return self.nombre == other.nombre
        return NotImplemented
        
class Puerto:
    def __init__(self,nombre:str,ciudad:str):
        self.nombre = nombre
        self.ciudad = ciudad
        self.embarcaciones = []
    
    def registrar(self,embarcacion):
        if embarcacion in self.embarcaciones :
            print("Ya esta registrada esa embarcacion")
        else:
            self.embarcaciones.append(embarcacion)

    def buscar_por_ruta (self,ruta):
        resultado=[]
        for embarcacion in self.embarcaciones:
            if ruta.lower() in embarcacion.ruta.lower():
                resultado.append(embarcacion)
        return resultado
    
    def listar_grandes (self):
        return [embarcacion for embarcacion in self.embarcaciones if embarcacion.es_grande()]
    
    def listar_grandes_simple(self):
        grandes = []
        for embarcacion in self.embarcaciones:
            if embarcacion.es_grande():
                grandes.append(embarcacion)
        return grandes
            
    def reporte(self):
                total = len(self.embarcaciones)
                grandes = len(self.listar_grandes())
                print(f"Puerto: {self.nombre}")
                print(f"Ciudad: {self.ciudad}")
                print(f"Total de embarcaciones: {total}")
                print(f"Embarcaciones grandes: {grandes}")
                print("Lista de embarcaciones:")

                for e in self.embarcaciones :
                    print(f"-{e.nombre}")

    #PROGRAMA DE PRUEBA

if __name__ == "__main__":
    puerto = Puerto("Puerto Masusa", "Iquitos")

    e1 = Embarcacion("Amazon Star", "deslizador", 30, "Iquitos - Nauta", "Honda", 150)
    e2 = Embarcacion("Rio Loreto", "motonave", 300, "Iquitos - Yurimaguas", "Yamaha", 500)
    e3 = Embarcacion("Selva Travel", "lancha", 80, "Iquitos - Santa Rosa", "Suzuki", 200)
    e4 = Embarcacion("Peque Peque ", "peque-peque", 12, "Iquitos - Tamshiyacu", "Honda", 40)

    puerto.registrar(e1)
    puerto.registrar(e2)
    puerto.registrar(e3)
    puerto.registrar(e4)

    repetida = Embarcacion("Amazon Star", "deslizador", 35, "Iquitos - Nauta", "Honda", 160)
    puerto.registrar(repetida)

    print("\nBusqueda por ruta 'Iquitos':")
    resultados = puerto.buscar_por_ruta("Iquitos")
    for embarcacion in resultados:
        print(embarcacion)

    print("\nEmbarcaciones grandes:")
    grandes = puerto.listar_grandes_simple()
    for embarcacion in grandes:
        print(embarcacion)

    print("\nReporte general:")
    puerto.reporte()

    print(f"\nTotal de embarcaciones creadas: {Embarcacion.total_embarcaciones}")



                