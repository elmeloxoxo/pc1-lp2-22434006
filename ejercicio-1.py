class productosAmazonicos:
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
             
      
        
f1= productosAmazonicos("Aguaje","fruta",12,4)
print(f1.stock)
f1.vender()



