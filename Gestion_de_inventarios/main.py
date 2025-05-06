from inventario import Inventario  # Importa la clase para gestionar el inventario.
from producto import Producto      # Importa la clase que representa un producto.


# interfaz del usuario
def menu():
    """Muestra las opciones disponibles para el usuario."""
    print("""
========= MENÚ =========
1. Añadir producto
2. Eliminar producto
3. Actualizar producto
4. Listar todos los productos
5. Filtrar por ID
6. Filtrar por nombre
0. Salir
========================
""")

def solicitar_datos_producto():
    """Pide al usuario la información para crear un nuevo producto."""
    identificador = input("ID: ")  # Obtiene el ID del producto.
    nombre = input("Nombre: ")      # Obtiene el nombre del producto.
    descripcion = input("Descripción: ")  # Obtiene la descripción del producto.
    precio = float(input("Precio: "))    # Obtiene y convierte el precio a un número decimal.
    cantidad = int(input("Cantidad disponible: "))  # Obtiene y convierte la cantidad a un número entero.
    return Producto(identificador, nombre, descripcion, precio, cantidad)  # Crea y devuelve un objeto Producto con los datos ingresados.

def main():
    """Función principal que controla el flujo de la aplicación."""
    inventario = Inventario()  # Crea una instancia de la clase Inventario para almacenar y gestionar los productos.

    while True:  # Inicia un bucle que se ejecuta hasta que el usuario decide salir.
        menu()  # Muestra el menú de opciones al usuario.
        opcion = input("Seleccione una opción: ")  # Lee la opción ingresada por el usuario.

        if opcion == "1":  # Si la opción es "1", el usuario quiere añadir un producto.
            producto = solicitar_datos_producto()  # Obtiene los detalles del nuevo producto llamando a la función correspondiente.
            inventario.agregar_producto(producto)  # Llama al método del inventario para añadir el producto creado.
        elif opcion == "2":  # Si la opción es "2", el usuario quiere eliminar un producto.
            identificador = input("ID del producto a eliminar: ")  # Pide el ID del producto que se va a eliminar.
            inventario.eliminar_producto(identificador)  # Llama al método del inventario para eliminar el producto con el ID especificado.
        elif opcion == "3":  # Si la opción es "3", el usuario quiere actualizar un producto.
            identificador = input("ID del producto a actualizar: ")  # Pide el ID del producto que se va a actualizar.
            nombre = input("Nuevo nombre (enter para omitir): ") or None  # Pide el nuevo nombre o usa None si no se ingresa nada.
            descripcion = input("Nueva descripción (enter para omitir): ") or None  # Pide la nueva descripción o usa None si no se ingresa nada.
            precio = input("Nuevo precio (enter para omitir): ")  # Pide el nuevo precio.
            cantidad = input("Nueva cantidad (enter para omitir): ")  # Pide la nueva cantidad.
            inventario.actualizar_producto(  # Llama al método del inventario para actualizar el producto.
                identificador,
                nombre=nombre,
                descripcion=descripcion,
                precio=float(precio) if precio else None,  # Convierte a float si hay valor, sino usa None.
                cantidad=int(cantidad) if cantidad else None   # Convierte a int si hay valor, sino usa None.
            )
        elif opcion == "4":  # Si la opción es "4", el usuario quiere listar todos los productos.
            inventario.listar_productos()  # Llama al método del inventario para mostrar la lista de productos.
        elif opcion == "5":  # Si la opción es "5", el usuario quiere filtrar productos por ID.
            identificador = input("ID a buscar: ")  # Pide el ID del producto a buscar.
            inventario.filtrar_por_id(identificador)  # Llama al método del inventario para buscar y mostrar el producto con ese ID.
        elif opcion == "6":  # Si la opción es "6", el usuario quiere filtrar productos por nombre.
            nombre = input("Nombre a buscar: ")  # Pide el nombre del producto a buscar.
            inventario.filtrar_por_nombre(nombre)  # Llama al método del inventario para buscar y mostrar los productos con ese nombre.
        elif opcion == "0":  # Si la opción es "0", el usuario quiere salir de la aplicación.
            print("¡Hasta pronto!")  # Muestra un mensaje de despedida.
            break  # Termina el bucle while, cerrando la aplicación.
        else:  # Si la opción ingresada no es válida.
            print("opción no válida.")  # Informa al usuario que la opción no es reconocida.

if __name__ == "__main__":
    """Asegura que la función main() se ejecute solo si el script se ejecuta directamente."""
    main()  # Llama a la función principal para iniciar la aplicación.