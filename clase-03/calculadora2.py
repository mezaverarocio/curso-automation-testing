def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calculadora():
    print("Bienvenido a la calculadora")
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        opcion = input("Elija la operación (+, -, *, /): ")

        if opcion == "+":
            resultado = sumar(a, b)
        elif opcion == "-":
            resultado = restar(a, b)
        elif opcion == "*":
            resultado = multiplicar(a, b)
        elif opcion == "/":
            resultado = dividir(a, b)
        else:
            print("Opción inválida")
            return

        print(f"El resultado de la operación es: {resultado}")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    except ValueError:
        print("Error: Ingrese un valor numérico válido.")
    finally:
        print("Gracias por usar la calculadora.")

if __name__ == "__main__":
    calculadora()