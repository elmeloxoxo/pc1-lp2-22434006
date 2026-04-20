class Motor:

    def __init__(self, marca: str, potencia_hp: int):
        self.marca = marca
        self.potencia_hp = potencia_hp

    def __str__(self):
      
        return f"{self.marca} {self.potencia_hp}HP"


class Embarcacion:

    total_embarcaciones = 0

    def __init__(self, nombre: str, tipo: str, capacidad_pasajeros: int, ruta: str, marca_motor: str, potencia_motor: int):
        self.nombre = nombre
        self.tipo = tipo
        self.capacidad_pasajeros = capacidad_pasajeros
        self.ruta = ruta
        self.motor = Motor(marca_motor, potencia_motor)
        Embarcacion.total_embarcaciones += 1

    def es_grande(self):
        
        return self.capacidad_pasajeros > 100

    def descripcion(self):
        
        return f"[{self.tipo}] {self.nombre} - Capacidad: {self.capacidad_pasajeros} - Ruta: {self.ruta} - Motor: {self.motor}"

    def __str__(self):
     
        return f"[{self.tipo}] {self.nombre} {self.ruta} (Motor: {self.motor})"

    def __eq__(self, otro):
       
        if not isinstance(otro, Embarcacion):
            return False
        return self.nombre.lower() == otro.nombre.lower()


class Puerto:

    def __init__(self, nombre: str, ciudad: str):
        self.nombre = nombre
        self.ciudad = ciudad
        self.embarcaciones = [] # Inicialmente vacía

    def registrar(self, embarcacion: Embarcacion):
   
        if embarcacion in self.embarcaciones: # Utiliza __eq__ automáticamente
            print(f"Error: La embarcación con nombre '{embarcacion.nombre}' ya está registrada.")
        else:
            self.embarcaciones.append(embarcacion)

    def buscar_por_ruta(self, ruta_busqueda: str):
        resultados = [e for e in self.embarcaciones if ruta_busqueda.lower() in e.ruta.lower()]
        return resultados

    def listar_grandes(self):
        return [e for e in self.embarcaciones if e.es_grande()]

    def reporte(self):
        print(f"\n--- REPORTE DEL PUERTO: {self.nombre} ({self.ciudad}) ---")
        print(f"Total embarcaciones registradas: {len(self.embarcaciones)}")
        print(f"Embarcaciones grandes: {len(self.listar_grandes())}")
        print("Lista completa:")
        for e in self.embarcaciones:
            print(f" - {e}")


# Programa de prueba obligatorio
if __name__ == "__main__":
    # 1. Crear el puerto
    mi_puerto = Puerto("Puerto Masusa", "Iquitos")

    # 2. Crear y registrar 4 embarcaciones con datos realistas
    e1 = Embarcacion("Flecha del Amazonas", "Deslizador", 30, "Iquitos a Nauta", "Yamaha", 200)
    e2 = Embarcacion("Gran Transatlántico", "Motonave", 350, "Iquitos a Yurimaguas", "Caterpillar", 1200)
    e3 = Embarcacion("Expreso de Selva", "Lancha", 80, "Iquitos a Santa Rosa", "Volvo", 450)
    e4 = Embarcacion("Río Itaya", "Peque-peque", 12, "Iquitos a Tamshiyacu", "Honda", 13)

    for nave in [e1, e2, e3, e4]:
        mi_puerto.registrar(nave)

    # 3. Intentar registro repetido
    e_repetida = Embarcacion("Flecha del Amazonas", "Lancha", 45, "Pucallpa", "Suzuki", 150)
    mi_puerto.registrar(e_repetida)

    # 4. Buscar por la ruta "Iquitos"