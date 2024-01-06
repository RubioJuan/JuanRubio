# Registro de 20 estudiantes 
class Estudiante:
    def __init__(self, nombre, edad, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.altura = altura

    def calcular_imc(self):
        altura_cuadrado = self.altura ** 2
        imc = self.peso / altura_cuadrado
        return imc

    def determinar_categoria_imc(self):
        imc = self.calcular_imc()
        if 18.5 <= imc < 24.9:
            return "Peso Ideal"
        elif 25 <= imc < 29.9:
            return "Sobrepeso"
        elif 30 <= imc < 34.9:
            return "Obesidad Grado I"
        elif 35 <= imc < 39.9:
            return "Obesidad Grado II"
        elif imc >= 40:
            return "Obesidad Grado III"
        else:
            return "Bajo peso"

def main():
    estudiantes = []

    for _ in range(20):
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))
        peso = float(input("Ingrese el peso del estudiante en kilogramos: "))
        altura = float(input("Ingrese la altura del estudiante en metros: "))

        estudiante = Estudiante(nombre, edad, peso, altura)
        estudiantes.append(estudiante)

    # Reporte
    peso_ideal_count = 0
    obesidad_grado_i_count = 0
    obesidad_grado_ii_count = 0
    obesidad_grado_iii_count = 0
    sobrepeso_count = 0

    for estudiante in estudiantes:
        categoria_imc = estudiante.determinar_categoria_imc()
        
        if categoria_imc == "Peso Ideal":
            peso_ideal_count += 1
        elif categoria_imc == "Sobrepeso":
            sobrepeso_count += 1
        elif categoria_imc == "Obesidad Grado I":
            obesidad_grado_i_count += 1
        elif categoria_imc == "Obesidad Grado II":
            obesidad_grado_ii_count += 1
        elif categoria_imc == "Obesidad Grado III":
            obesidad_grado_iii_count += 1

    print("\nReporte:")
    print(f"a. Cuantos estudiantes se encuentran en el peso ideal: {peso_ideal_count}")
    print(f"b. Cuantos estudiantes se encuentran en obesidad grado I: {obesidad_grado_i_count}")
    print(f"c. Cuantos estudiantes se encuentran en obesidad grado II: {obesidad_grado_ii_count}")
    print(f"d. Cuantos estudiantes se encuentran en obesidad grado III: {obesidad_grado_iii_count}")
    print(f"e. Cuantos estudiantes se encuentran en sobrepeso: {sobrepeso_count}")

if __name__ == "__main__":
    main()