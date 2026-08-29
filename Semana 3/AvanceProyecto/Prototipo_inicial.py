# Vamos a iniciar variables 0_0

stk_chocolate = 21
stk_matcha = 18
stk_fresa = 15

nombre_responsable = "Aoki Takano"

opcionmenu = 0
preciopockys = 48

#Primer bloque completado... 
#Aquí empieza el segundo bloque (el proceso)

while opcionmenu !=4:
    print("MENU DE LOCAL POCKY YEM")
    print(f"Cajero de turno: {nombre_responsable}")
    print(f"1. Pocky de Chocolate (Existencia: {stk_chocolate})")
    print(f"2 Pocjy de Matcha (Existencia: {stk_matcha})")
    print(f"3. Pcky de Fresa (Existencia: {stk_fresa})")
    print("4. Cerrar menu")

 
    opcionmenu = int(input("Ingrese el sabor requerido por el cliente: "))


    if 1 <= opcionmenu <=3:
        #1 <= opcionmenu <= 3 está abreviado; aqui se usa "and" (if opcionmenu <=1 and opcionmenu <=3:)
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
                    print("¡ALERTA! EL PoCKY DE CHOCOLATE SE ESTA ACABANDO. HAY QUE PEDIR MÁS SUMINISTROS.")
            elif opcionmenu == 2:
                stk_matcha = stk_matcha - cantidad_c
                if stk_matcha <= 6:
                    print("¡ALERTA! EL POCKY DE MATCHA SE ESTÁ ACABANDO. HAY QUE PEDIR MÁS SUMINISTROS.")
            elif opcionmenu == 3:
                stk_fresa = stk_fresa - cantidad_c
                if stk_fresa <=6:
                    print("¡ALERTA! EL POCKY DE FRESA SE ESTÁ ACABANDO. HAY QUE PEDIR MÁS SUMINSITROS.")

                    # CERRAMOS EL PROCESO Y VAMOS POR EL ÚLTIMO BLOQUE: MOSTRAR UN "REGISTRO" DE LO QUE SE HIZO 
                    # Y quiero que se vea decente... (no amontonado ;-;)

            print("\n     REGISTRO DE VENTA       ")
            print(f"Importe original:   ${precio_original:.2f}")
            print(f"El descuento aplicado (12%): -${descuentoA:.2f}")
            print(f"IVA:    ${impuestoIVA:.2f}")
            print(f"Total a Pagar:    ${totaldepagoCIVA:.2f}")
        else:
            print("EL ALMACEN NO CUENTA CON EXISTENCIAS SUFIECIENTES")

    elif opcionmenu == 4:
        print("Cerrando sistema...")
    else:
        print("Opción invalida en el sitema.")

print("Caja cerrada.")


    