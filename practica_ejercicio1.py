class ProductoAmazonico:
    total_productos = 0
    
    def __init__(self,nombre:str,categoria:str,precio:float,stock:int):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock= stock
        self.id_valor:float
        ProductoAmazonico.total_productos += 1

#VALIDACIONES
        if not (self.precio > 0):
            raise ValueError ("El precio no es valido")
        
        if not (self.stock > 0):
            raise ValueError ("El valor en stock no es un valor permitido")

        if self.categoria != "fruta" and self.categoria != "planta medicinal" and self.categoria != "artesania" and self.categoria != "alimento" :
            raise ValueError  ("La categoria no es valida") 

#METODOS
    
    def vender (self,cantidad:int):
        if  cantidad > self.stock :
            raise TypeError ("la cantidad pedida supera al stock")
        else:
            self.stock -= cantidad
            print(f"{cantidad} Vendidos Exitosamente")
            return 
    
    def reabastecer (self,cantidad:int):
        if cantidad <= 0 :
            raise ValueError("el valor no es valido")
        else:
            self.stock += cantidad
            print (f"Se abastecio correctamente {cantidad} unidades")
            print (f"Ahora se tiene {self.stock} unidades")
            return True
        
    def valor_inventario(self) -> float:
        return self.precio * self.stock

#METODO DE CLASE
    @classmethod
    def desdecadena(cls,cadena:str):
        partes = cadena.replace("|"," ").split()
        return cls(partes[0],partes[1],float(partes[2]),int(partes[3]))
    
    #FORMATOS DE SALIDA
    
    def __str__(self):
        return f"{self.nombre}({self.categoria}) - S/.{self.precio} - Stock:{self.stock} Unidades"
    def __repr__(self):
        return f"ProductoAmazonico({self.nombre!r},{self.categoria!r},{self.precio},{self.stock})"

#PROGRAMA DE PRUEBA
if __name__ == "__main__":
    product1 = ProductoAmazonico("Aguaje","fruta",23.90,25)
    product2 = ProductoAmazonico("Camu Camu","fruta",34.60,18)
    product3 = ProductoAmazonico("Uña de Gato","planta medicinal",43.50,50)
    product4 = ProductoAmazonico("Chonta","alimento",19.99,60)
    product5 = ProductoAmazonico("collar iwakari","artesania",10,8)
    
    productoclase = ProductoAmazonico.desdecadena("Platano|fruta|28.40|11")

    productos = [product1,product2,product3,product4,product5,productoclase]
    #20 Unidades vendidas
    product1.vender(20)

    #Mas del stock
    # product5.vender(9)

    #Reabasteciendo un producto
    product1.reabastecer(30)

    #Todos los productos con print
    print("\n---------INVENTARIO--------")
    for p in productos:
        print (p)


    #Total Productos
    print(f"\nel total de productos es: {ProductoAmazonico.total_productos}")

    #valor inventario final
    total_valor = sum(p.valor_inventario() for p in productos)
    print(f"Valor total del inventario S/. {total_valor:.2f}")






    