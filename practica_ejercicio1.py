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
        self.id_valor = self.precio * self.stock
        print(f"el valor en el inventario es {self.id_valor}")
        return

#METODO DE CLASE
    @classmethod
    def desdecadena(cls,cadena:str):
        partes = cadena.replace("|"," ").split()
        return cls(partes[0],partes[1],float(partes[2]),int(partes[3]))


productoclase = ProductoAmazonico.desdecadena("Platano|fruta|28.40|11")

print(productoclase.stock)


prd1=ProductoAmazonico ("Coca","planta medicinal",3.80,6)
prd1.reabastecer(20)
prd1.vender(18)
print(prd1.stock)
#prd1.valor_inventario()








# prd2=ProductoAmazonico("Tapioca","energizante",22.30 ,20)
# print(prd2.nombre)

# print(ProductoAmazonico.total_productos)
    



    