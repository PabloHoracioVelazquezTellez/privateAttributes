class Venta:

    __id_venta = None
    __fecha = None
    __cliente = None
    __productos = []  # Lista de diccionarios para productos
    __total = 0


    # Getters para acceder a los atributos privados

    def get_id_venta(self):

        return self.__id_venta


    def get_fecha(self):

        return self.__fecha


    def get_cliente(self):

        return self.__cliente


    def get_productos(self):

        return self.__productos


    def get_total(self):

        return self.__total


    # Setters para modificar los atributos privados

    def set_id_venta(self, id_venta):

        self.__id_venta = id_venta


    def set_fecha(self, fecha):

        self.__fecha = fecha


    def set_cliente(self, cliente):

        self.__cliente = cliente

    def set_productos(self, producto):
        # Agregar el producto a la lista en lugar de reemplazar la lista completa
        self.__productos.append(producto)

    def set_total(self):
        # Inicializar el total en 0 antes de calcularlo
        self.__total = 0.0
        # Calcular el total sumando (cantidad * precio_unitario) de cada producto
        for producto in self.__productos:
            self.__total += producto['cantidad'] * producto['precio_unitario']

    def mostrar_detalle(self):
        print(f"ID Venta: {self.__id_venta}")
        print(f"Fecha: {self.__fecha}")
        print(f"Cliente: {self.__cliente}")
        print("Productos:")
        if not self.__productos:
            print("No hay productos en la lista.")
        else:
            for producto in self.__productos:
                print(f" - {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio Unitario: ${producto['precio_unitario']:.2f}")
        print(f"Total: ${self.__total:.2f}")