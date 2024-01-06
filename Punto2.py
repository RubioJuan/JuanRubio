Nombre = input("Ingrese el nombre del estudiante: ")
Edad = int(input("Ingrese la edad del estudiante: "))
Peso = float(input("Ingrese el peso del estudiante del estudiante: "))
Altura = float(input("Ingrese la altura del estudiante: "))
Altura_2 = (Altura * Altura)
IMC = (Peso / Altura_2)
if IMC <= 24.9:
    categoriaimc = "NORMAL"
    print("Su categoria es normal") 
elif IMC <= 29.9:
    print("Su categoria es de sobre peso")    
elif IMC <= 34.9:
    print("Su categoria es de obesidad 1")    
elif IMC <= 39.9:
    print("Su categoria es de obesidad 2")
elif IMC > 40:
    print("Su categoria obesidad 3")        
else: 
    print("Error, no entra en ninguna categoria")    