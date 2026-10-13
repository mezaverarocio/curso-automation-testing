primer_numero = float(input("Dame un primer número: "))
segundo_numero = float(input("Dame un segundo número: "))
operacion = input("Ingrese símbolo de la operación a realizar +, -, *, /: ")

if operacion == "+":
    print(primer_numero + segundo_numero)
elif operacion == "-":
    print(primer_numero - segundo_numero)
elif operacion == "*":
    print(primer_numero * segundo_numero)
elif operacion == "/":
    print(primer_numero / segundo_numero)
else:
    print("Operación no válida")