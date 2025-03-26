import math

def menu():
    print("\n--- Calculadora Avanzada ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Raíz Cuadrada")
    print("7. Salir")

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División entre cero no permitida."
    return a / b

def potencia(a, b):
    return a ** b

def raiz_cuadrada(a):
    if a < 0:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo."
    return math.sqrt(a)

def main():
    while True:
        menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print(f"Resultado: {sumar(a, b)}")
        elif opcion == "2":
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print(f"Resultado: {restar(a, b)}")
        elif opcion == "3":
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print(f"Resultado: {multiplicar(a, b)}")
        elif opcion == "4":
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print(f"Resultado: {dividir(a, b)}")
        elif opcion == "5":
            a = float(input("Ingresa la base: "))
            b = float(input("Ingresa el exponente: "))
            print(f"Resultado: {potencia(a, b)}")
        elif opcion == "6":
            a = float(input("Ingresa el número: "))
            print(f"Resultado: {raiz_cuadrada(a)}")
        elif opcion == "7":
            print("¡Gracias por usar la calculadora! Hasta luego.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()