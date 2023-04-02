class ManejadorProductos:
    def __init__(self):
        self.products = []

    def mostrar (self):
        return print(self.products)

    def agregar (self, product):
        self.products.append(product)
        return self.mostrar()
    

#Instancio la clase:
producto1 = ManejadorProductos()
leche = {"marca": "LaSerenisima", "precio": 500}
producto1.agregar(leche)