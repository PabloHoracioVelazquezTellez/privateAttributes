from classVenta import Venta
venta= Venta()
venta.set_id_venta(1)
venta.set_fecha("15/10/24")
venta.set_cliente("Pablo")
for i in range(3):
    nombre = input("Producto: ")
    cantidad = int(input("Cantidad: "))
    precio_unitario = float(input("Precio Unitario: "))

    # Crear un diccionario para el producto y agregarlo a la lista
    producto = {
        'nombre': nombre,
        'cantidad': cantidad,
        'precio_unitario': precio_unitario
    }
    venta.set_productos(producto)
venta.set_total()

venta.mostrar_detalle()