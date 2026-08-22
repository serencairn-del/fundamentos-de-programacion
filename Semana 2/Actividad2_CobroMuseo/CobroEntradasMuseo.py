# Maria Estrella Arreola Yañez | Entrega: 21-08-26

# Precios base: Niños menores de 3 años (Gratis); Menores de edad ($30); Mayores de edad ($45).
# Descuentos: Adulto Mayor (12%); Profesor (%10); Estudiante (%10).

total_de_la_cuenta = 0
contador_infantes = 0
contador_menores= 0
contador_adultos = 0
descuento = 0.10
descuento2 = 0.10
descuento3 = 0.12
num_visitantes=int(input("¿Cuántos desean boleto?: "))


while True:

    edad = int(input("¿Cuál es la edad del cliente? "))
    if edad < 3:
        precio_base = 0
        precio_final = precio_base
        contador_infantes = contador_infantes + 1
        print("Menor de tres años, boleto gratis")
    elif edad >=3 and edad <=17:
        precio_base = 30
        contador_menores = contador_menores + 1
        p_estudiante = input("El menor de edad es estudiante? (Sí/No)")
        if p_estudiante == "Sí": 
            precio_final = precio_base - (precio_base * descuento)
        else:
            precio_final = precio_base
    else:
        precio_base = 45
        contador_adultos = contador_adultos + 1
       

        print("Tipos de descuento: 1 - Adulto Mayor; 2 - Profesor, 3 - Estudiante; 4 - Ninguno")
        opc = input("Selecciona una opción: ")
        if opc == "1":
            precio_final = precio_base - (precio_base * descuento3)
        elif opc == "2":
            precio_final = precio_base - (precio_base * descuento2)
        elif opc == "3":
            precio_final = precio_base - (precio_base * descuento2)
        else:
            precio_final = precio_base

    total_de_la_cuenta = total_de_la_cuenta + precio_final
    print(f"El cobro de este boleto: $ {precio_final:.2f}\n")

    if contador_adultos + contador_menores + contador_infantes == num_visitantes:
        print("Registro finalizado conn éxito")
        break

print()
print("REPORTE DETALLADO DEL DÍA: ")
print(f"Los infantes son: {contador_infantes}")
print(f"Los menores son: {contador_menores}")
print(f"Los adultos son: {contador_adultos}")
print(f"Total de personas: {contador_infantes + contador_menores + contador_adultos}")
print(f"Tortal de la cuenta: ${total_de_la_cuenta:.2f}")


