class ProductoAmazonico:
    total_productos =+ 1

#CONSTRUCTOR
    def __init__(self,nombre,categoria,precio,stock):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

#VALIDACIONES
        if self.precio < 0:
            raise ValueError ("El precio no es valido")
        if self.stock <= 0:
            raise ValueError ("el stock no es el adecuado")
        if self.categoria != "fruta" and self.categoria != "planta medicinal" and self.categoria != "artesania" and self.categoria != "alimento":
                raise ValueError ("La categoria no es valida")
        
#METODOS
    def vender(self,cantidad):
        if cantidad > self.stock:
            print("Error: No hay suficiente stock para realizar la venta.")
            return False
        else:
            self.stock -= cantidad
            return "se vendio con exito"
        
    def reabastecer(self, cantidad: int):
        self.stock += cantidad
    
    def valor_inventario(self) -> float:
        return self.precio * self.stock
    
    @classmethod
    def desde_cadena(cls, cadena: str):
        partes = cadena.replace("|", " ").split()
        return cls(partes[0], partes[1], float(partes[2]), int(partes[3]))
    
    #FORMATOS DE SALIDA

    def __str__(self):
        return f"{self.nombre} ({self.categoria}) S/ {self.precio:.2f} Stock: {self.stock} unidades"
    
    def __repr__(self):
        return f"ProductoAmazonico('{self.nombre}', '{self.categoria}', {self.precio}, {self.stock})"
             
    #TESTEO
    # --- PROGRAMA DE PRUEBA OBLIGATORIO ---
if __name__ == "__main__":

    # 1. Crear 5 productos usando constructor normal
    p1 = ProductoAmazonico("Aguaje", "fruta", 5, 100)
    p2 = ProductoAmazonico("Camu Camu", "fruta", 8, 50)
    p3 = ProductoAmazonico("Uña de Gato", "planta medicinal", 15, 20)
    p4 = ProductoAmazonico("Chonta", "alimento", 10, 15)
    p5 = ProductoAmazonico("Cerámica", "artesanía", 50, 5)

    print(p1.nombre)

    #CONSTRUCTOR ALTERNATIVO
    p6 = ProductoAmazonico.desde_cadena("SachaInchi alimento 25.0|40")
    
    productos = [p1, p2, p3, p4, p5, p6]

      # 3. Vender 20 unidades del primero 
    p1.vender(20)

    # 4. Intento de venta fallida (más del stock) 
    p5.vender(10)

    # 5. Reabastecer 
    p3.reabastecer(10)

    # 6. Imprimir todos los productos
    print("\n--- Inventario Actual ---")
    for p in productos:
        print(p)

    # 7. Imprimir total_productos de clase 
    print(f"\nTotal de productos registrados: {ProductoAmazonico.total_productos}")

    # 8. Valor de inventario total 
    total_valor = sum(p.valor_inventario() for p in productos)
    print(f"Valor total del inventario: S/ {total_valor:.2f}")

        



