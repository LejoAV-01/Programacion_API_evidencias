from producto import Producto

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.identificador in self.productos:
            print("Ya existe un producto con ese ID.")
        else:
            self.productos[producto.identificador] = producto
            print("Producto añadido exitosamente.")

    def eliminar_producto(self, identificador):
        if identificador in self.productos:
            del self.productos[identificador]
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, identificador, **kwargs):
        producto = self.productos.get(identificador)
        if producto:
            producto.actualizar(**kwargs)
            print(" Producto actualizado.")
        else:
            print("Producto no encontrado.")

    def listar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        for producto in self.productos.values():
            print(producto)

    def filtrar_por_id(self, identificador):
        producto = self.productos.get(identificador)
        if producto:
            print(producto)
        else:
            print("Producto no encontrado.")

    def filtrar_por_nombre(self, nombre):
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        if encontrados:
            for p in encontrados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")
