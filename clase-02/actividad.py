nombre = input("Ingresá tu nombre: ")
edad =  input("Ingresá tu edad: ")
profesion = input("Ingresá tu profesión: ")
print(f"¡Bienvenidx {nombre}! Confirmamos que tenés {edad} y trabajás como {profesion}.")

for número in range(1,21):
    if número % 2 == 0:
        print(f"{número} es par")