dependencias = []
def registrar_dependencia():
    nombre_dependencia = input("Ingrese el nombre de la dependencia: ")
    dependencias.append({"nombre": nombre_dependencia, "consumo_electricidad": []})

def registrar_consumo_por_dependencia():
    if not dependencias:
        print("Primero debe registrar al menos una dependencia.")
        return

    print("Seleccione la dependencia para registrar el consumo:")
    for i, dependencia in enumerate(dependencias, 1):
        print(f"{i}. {dependencia['nombre']}")

    opcion_dependencia = int(input("Ingrese el número de la dependencia: "))
    dependencia_actual = dependencias[opcion_dependencia - 1]

    consumo_electricidad = float(input("Ingrese el consumo de electricidad en kWh: "))
    dependencia_actual["consumo_electricidad"].append(consumo_electricidad)

def ver_co2_producido():
    if not dependencias:
        print("Primero debe registrar al menos una dependencia.")
        return

    total_co2_producido = 0

    print("\nCO2 producido por cada dependencia:")
    for dependencia in dependencias:
        co2_producido = sum(dependencia["consumo_electricidad"]) * 0.6 
        total_co2_producido += co2_producido
        print(f"{dependencia['nombre']}: {co2_producido:.2f} kg CO2")

    print(f"\nTotal CO2 producido en la ciudad: {total_co2_producido:.2f} kg CO2")
def dependencia_mayor_co2():
    if not dependencias:
        print("Primero debe registrar al menos una dependencia.")
        return

    max_co2 = 0
    dependencia_max_co2 = ""

    for dependencia in dependencias:
        co2_producido = sum(dependencia["consumo_electricidad"]) * 0.6
        if co2_producido > max_co2:
            max_co2 = co2_producido
            dependencia_max_co2 = dependencia["nombre"]

    if dependencia_max_co2:
        print(f"\nLa dependencia que produce mayor CO2 es: {dependencia_max_co2} ({max_co2:.2f} kg CO2)")
    else:
        print("No hay suficiente información para determinar la dependencia con mayor producción de CO2.")
while True:
    print("\nMenú:")
    print("1. Registrar Dependencia")
    print("2. Registrar Consumo por Dependencia")
    print("3. Ver CO2 Producido")
    print("4. Dependencia que Produce Mayor CO2")
    print("5. Salir")
    opcion = int(input("Ingrese la opción deseada: "))
    if opcion == 1:
        registrar_dependencia()
    elif opcion == 2:
        registrar_consumo_por_dependencia()
    elif opcion == 3:
        ver_co2_producido()
    elif opcion == 4:
        dependencia_mayor_co2()
    elif opcion == 5:
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")
