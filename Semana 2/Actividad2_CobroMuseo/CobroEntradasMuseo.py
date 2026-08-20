# Maria Estrella Arreola Yañez | Entrega: 21-08-26

# Precios base: Niños menores de 3 años (Gratis); Menores de edad ($30); Mayores de edad ($45).
# Descuentos: Adulto Mayor (12%); Profesor (%10); Estudiante (%10).

total_de_la_cuenta = 0

while True:
    inicio = input("¿Cuál es la edad del visitante? (Escribe 'Salir'): ")
    if inicio == "Salir":
        print("Saliendo...")
        break
    edad = int(inicio)

    if