class Producto:
    def __init__(self, codigo, nombre, valor_compra, valor_venta, stock_minimo, stock_maximo, proveedor):
        self.codigo = codigo
        self.nombre = nombre
        self.valor_compra = valor_compra
        self.valor_venta = valor_venta
        self.stock_minimo = stock_minimo
        self.stock_maximo = stock_maximo
        self.proveedor = proveedor
        self.stock_actual = 0
    def actualizar_stock(self, cantidad):
        self.stock_actual += cantidad
    def calcular_ganancia_potencial(self):
        return (self.valor_venta - self.valor_compra) * self.stock_actual
productos = []
def registrar_producto():
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    valor_compra = float(input("Ingrese el valor de compra del producto: "))
    valor_venta = float(input("Ingrese el valor de venta del producto: "))
    stock_minimo = int(input("Ingrese el stock mínimo permitido: "))
    stock_maximo = int(input("Ingrese el stock máximo permitido: "))
    proveedor = input("Ingrese el nombre del proveedor del producto: ")
    nuevo_producto = Producto(codigo, nombre, valor_compra, valor_venta, stock_minimo, stock_maximo, proveedor)
    productos.append(nuevo_producto)
    print("Producto registrado con éxito.")
def visualizar_productos():
    print("\nLista de Productos:")
    for producto in productos:
        print(f"\nCódigo: {producto.codigo}")
        print(f"Nombre: {producto.nombre}")
        print(f"Valor de Compra: ${producto.valor_compra:.2f}")
        print(f"Valor de Venta: ${producto.valor_venta:.2f}")
        print(f"Stock Mínimo: {producto.stock_minimo}")
        print(f"Stock Máximo: {producto.stock_maximo}")
        print(f"Proveedor: {producto.proveedor}")
        print(f"Stock Actual: {producto.stock_actual}")
def actualizar_stock():
    codigo_producto = input("Ingrese el código del producto: ")
    cantidad = int(input("Ingrese la cantidad a agregar o restar al stock (positivo para agregar, negativo para restar): "))
    for producto in productos:
        if producto.codigo == codigo_producto:
            producto.actualizar_stock(cantidad)
            print("Stock actualizado con éxito.")
            return
    print("No se encontró un producto con ese código.")
def informe_productos_criticos():
    print("\nProductos Críticos:")
    for producto in productos:
        if producto.stock_actual < producto.stock_minimo:
            print(f"\nCódigo: {producto.codigo}")
            print(f"Nombre: {producto.nombre}")
            print(f"Stock Mínimo: {producto.stock_minimo}")
            print(f"Stock Actual: {producto.stock_actual}")
def calcular_ganancia_potencial_total():
    total_ganancia_potencial = sum(producto.calcular_ganancia_potencial() for producto in productos)
    print(f"\nGanancia Potencial Total: ${total_ganancia_potencial:.2f}")
while True:
    print("\nMenú Principal:")
    print("1. Registrar Producto")
    print("2. Visualizar Productos")
    print("3. Actualizar Stock")
    print("4. Informe de Productos Críticos")
    print("5. Calcular Ganancia Potencial Total")
    print("6. Salir")
    opcion = int(input("Ingrese la opción deseada: "))
    if opcion == 1:
        registrar_producto()
    elif opcion == 2:
        visualizar_productos()
    elif opcion == 3:
        actualizar_stock()
    elif opcion == 4:
        informe_productos_criticos()
    elif opcion == 5:
        calcular_ganancia_potencial_total()
    elif opcion == 6:
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")
