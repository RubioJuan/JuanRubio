def main():
    numeros = []
    
    while True:
        numero = int(input("Ingrese un número entero (ingrese un número negativo para finalizar): "))
        
        if numero < 0:
            break
        
        numeros.append(numero)

    if not numeros:
        print("No se ingresaron números.")
        return

    total_numeros = len(numeros)
    total_pares = sum(1 for num in numeros if num % 2 == 0)
    total_impares = total_numeros - total_pares
    promedio_pares = sum(num for num in numeros if num % 2 == 0) / total_pares if total_pares > 0 else 0
    promedio_impares = sum(num for num in numeros if num % 2 != 0) / total_impares if total_impares > 0 else 0
    menores_que_10 = sum(1 for num in numeros if num < 10)
    entre_20_y_50 = sum(1 for num in numeros if 20 <= num <= 50)
    mayores_que_100 = sum(1 for num in numeros if num > 100)

    print("\nReporte:")
    print(f"a. Total de números ingresados: {total_numeros}")
    print(f"b. Total de números pares ingresados: {total_pares}")
    print(f"c. Promedio de los números pares: {promedio_pares:.2f}")
    print(f"d. Promedio de los números impares: {promedio_impares:.2f}")
    print(f"e. Cuantos números son menores que 10: {menores_que_10}")
    print(f"f. Cuantos números están entre 20 y 50: {entre_20_y_50}")
    print(f"g. Cuantos números son mayores que 100: {mayores_que_100}")

if __name__ == "__main__":
    main()