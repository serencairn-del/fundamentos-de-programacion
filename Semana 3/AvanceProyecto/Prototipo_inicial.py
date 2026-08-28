# Vamos a iniciar variables 0_0

stk_chocolate = 21
stk_matcha = 18
stk_fresa = 15

nombre_responsable = "Aoki Takano"

opcionmenu = 0
preciopockys = 48

#Primer bloque completado... 
#Aquí empieza el segundo bloque (el proceso)

while opcionmenu:
    print("MENU DE LOCAL POCKY YEM")
    print(f"Cajero de turno: {nombre_responsable}")
    print(f"1. Pocky de Chocolate")
    print(f"2 Pocjy de Matcha")
    print(f"3. Pcky de Fresa")
    print("4. Cerrar menu")

    try:
        opcionmenu = int(input("Seleccione el sabor o salir(1 a 4): "))

    if 1 <= opcionmenu >=3:
        try:
            cantidad_c = int(input("Ingresa cuántas cajas de Pocky quiere el cliente: "))

            if cantidad_c <= 0:
                print("Error: La cantidad de cajas debe ser un número positivo y mayor a cero.")
                continue

            if opcionmenu == 1:
                stockdisponible = stk_chocolate
            elif opcionmenu == 2: 
                stockdisponible = stk_matcha
            else:
                stockdisponible = stk_fresa

            if cantidad_c <= stockdisponible:
                precio_original = cantidad_c * preciopockys

                if cantidad_c > 6:
                    descuentoA = precio_original * 0.12
                else:
                    descuentoA = 0.0

                impuestoIVA = (precio_original - descuentoA) * 0.16
                totaldepagoCIVA = (precio_original - descuentoA) + impuestoIVA

                if opcionmenu == 1:
                    stk_chocolate = stk_chocolate - cantidad_c
                    if stk_chocolate <= 6:
                        print("¡ALERTA! EL PCKY DE CHOCOLATE SE ESTA ACABANDO. HAY QUE RE-ORDENAR.")
                    elif opcionmenu == 2:
                        stk_matcha = stk_matcha - cantidad_c
                        if stk_matcha <= 6:
                            print("¡ALERTA! EL POCKY DE MATCHA SE ESTÁ ACABDO. HAY QUE PEDIR MÁS SUMINISTROS.")
                    elif opcionmenu == 3:
                        stk_fresa = stk_fresa - cantidad_c
                        if stk_fresa <=6:
                            print("¡ALERTA! EL POCKY DE FRESA SE ESTÁ ACABANDO. HAY QUE PEDIR MÁS SUMINSITROS.")

                    # CERRAMOS EL PROCESO Y VAMOS POR EL ÚLTIMO BLOQUE: MOSTRAR UN "REGISTRO" DE LO QUE SE HIZO 
                    # Y quiero que se vea decente... (no amontonado ;-;)

                    print("     REGISTRO DE VENTA       ")
                    print(f"Importe original:   ${precio_original}")
                    print(f"El descuento aplicado (12%):    -$")
                    print(f"IVA:    ${impuestoIVA}")
                    print(f"Total final:    ${totaldepagoCIVA}")
                else:
                    print("EL ALMACEN NO CUENTA CON EXISTENCIAS SUFIECINTES")
            elif opcionmenu == 4:
                print("Cerrando sistema...")
            else:
                print("")


    