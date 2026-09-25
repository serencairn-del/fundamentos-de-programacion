# VERSIÓN PRUEBA DEL PROYECTO FINAL, EL CÓDIGO TERMINADO SERA TRASLADADO A UN CUADERNO DE JUPYTER Y EJECUTADO PARA UNA MEJOR
# LEGIBILIDAD PARA EL PROFESOR.

# IMPORTACIÓN DE LIBRERIAS ⬩➤

import time # Requerido para la pausa
import pdb # Requerido para la depuración

# VARIABLES GLOBALES E INVENTARIO INCIAL ⬩➤

stk_chocolate = 21
stk_matcha = 18
stk_fresa = 15
preciopockys = 48

# DICCIONARIO PARA LAS OPCIONES DEL MENÚ HACIA LOS ARCHIVOS

Archivos_Sistema = {

    "1": "inventario_inicial.txt",
    "2": "ventas_diarias.txt",
    "3": "alertas_stock.txt",
    "4": "registro_caja.txt"
}

# PANTALLA DE CARGA ⬩➤

def pantalla_carga():

    print("\n" + "✩₊˚.⋆☾𓃦☽⋆⁺₊✧" * 9)
    print()
    print("𖤐⬩➤INICIANDO SISTEMA DE GESTIÓN LOCAL POCKY YEM...")
    print()
    print("✩₊˚.⋆☾𓃦☽⋆⁺₊✧" * 9)

    for i in range(1, 4):
        print(f"𖤐 CARGANDO SISTEMA... [{i * 33}%]")
        time.sleep(1.5)

    print("\n[𖤐] SISTEMA INICIADO CORRECTAMENTE ^^")
    print("⬩➤" * 15 + "\n")

# SECUENCIA DEL PROGRAMA  ⬩➤

# Identificación del usuario con una función.
def solicitar_nombre_cajero():

    nombre = ""
    nombre_valido = False

    while not nombre_valido:
        nombre = input("Por favor, ingresar el nombre del cajero en turno ^^: ")
        if nombre != "" and nombre.replace(" ", "").isalpha():
            nombre_valido = True
        else:
            print("[𖤐] ERROR. EL NOMBRE DEL CAJERO DEBE CONTENER SOLO LETRAS Y SIN ESPACIOS VACIOS. ")
            print("𖤐 INTENTE DE NUEVO SIN USAR NÚMEROS NI SIMBOLOS EXTRAÑOS ^^. \n")

    return nombre

def procesar_venta():
    global stk_chocolate, stk_matcha, stk_fresa, fecha, nombre

    print("\n✩₊˚.⋆☾⋆⁺₊✧| MÓDULO DE VENTAS POCKY YEM |✩₊˚.⋆☾⋆⁺₊✧")
    print(f"1. 𖤐 Pocky de Chocolate (Existencia: {stk_chocolate})")
    print(f"2. 𖤐 Pocky de Matcha    (Existencia: {stk_matcha})")
    print(f"3. 𖤐 Pocky de Fresa     (Existencia: {stk_fresa})")

    try:
        opcionmenu = int(input("𖤐 INGRESE EL SABOR REQUERIDO POR EL CLIENTE (1-3): "))
        if 1<= opcionmenu <=3:
            cantidad_c = int(input("𖤐 INGRESA CUÁNTAS CAJAS DE POCKY QUIERE EL CLIENTTE: "))

            if cantidad_c <= 0:
                print("⚠︎ LA CANTIDAD DE CAJAS DEBE SER UN NÚMERO POSITIVO Y MAYOR A CERO. ")
                return

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

                subtotal_neto = precio_original -descuentoA
                impuestoIVA = subtotal_neto * 0.16
                totalpagoCIVA = subtotal_neto + impuestoIVA

                alertas_generadas = "Ninguna"
                if opcionmenu == 1:
                    stk_chocolate -= cantidad_c
                    if stk_chocolate <= 6:
                        alertas_generadas = "ALERTA CHOCOLATE BAJO"
                        print("¡ALERTA! EL POCKY DE CHOCOLATE SE ESTÁ ACABANDO. PEDIR MÁS SUMINISTROS.")
                elif opcionmenu == 2:
                    stk_matcha -= cantidad_c
                    if stk_matcha <= 6:
                        alertas_generadas = "ALERTA MATCHA BAJO"
                        print("¡ALERTA! EL POCKY DE MATCHA SE ESTÁ ACABANDO. PEDIR MÁS SUMINISTROS.")
                elif opcionmenu == 3:
                    stk_fresa -= cantidad_c
                    if stk_fresa <= 6:
                        alertas_generadas = "ALERTA FRESA BAJO"
                        print("¡ALERTA! EL POCKY DE FRESA SE ESTÁ ACABANDO. PEDIR MÁS SUMINISTROS.")

                print("\n" + "๋࣭ ⭑⚝" * 8 + " TICKET DE VENTA " + "๋࣭ ⭑⚝" * 8)
                print(f" Importe original:   ${precio_original:.2f}")
                print(f" Descuento aplicado: -${descuentoA:.2f}")
                print(f" Subtotal Neto:      ${subtotal_neto:.2f}")
                print(f" IVA (16%):          ${impuestoIVA:.2f}")
                print(f" Total a Pagar:      ${totalpagoCIVA:.2f}")
                print("๋࣭ ⭑⚝" * 21)

                try:
                    fecha_txt = f"{fecha[0]}/{fecha[1]}/{fecha[2]}"

                    with open("ventas_diarias.txt", mode="a") as file_ventas:
                        file_ventas.write(f"Fecha: {fecha_txt} | Cajero: {nombre} | Sabor: {opcionmenu} | Cajas: {cantidad_c} | Total: ${totalpagoCIVA:.2f}\n")

                    if alertas_generadas != "Ninguna":
                        with open("alertas_stock.txt", mode="a") as file_alertas:
                            file_alertas.write(f"|{fecha_txt}| {alertas_generadas} > Chocolate: {stk_chocolate}, Matcha: {stk_matcha}, Fresa: {stk_fresa}\n")
                    print("VENTA REGISTRADA CORRECTAMENTE.")

                except Exception as error_archivo:
                    print(f"ERROR AL INTENTAR ESCRIBIR LOS ARCHIVOS EN: {error_archivo}")
            else:
                print("EL ALMACEN NO CUENTA CON EXISTENCIAS SUFICIENTES")
        else:
            print("OPCIÓN DE SABOR INVALIDA EN EL PANEL DE VENTAS")

    except ValueError:
        print("ERROR, INGRESE ÚNICAMENTE NÚMEROS ENTEROS.")




print(" 𖤐 IDENTIFICACIÓN DE PERSONAL 𖤐")
nombre = solicitar_nombre_cajero()

 # Bienvenida ^^

mensaje_bienvenida = " 𖤐 BIENVENIDO AL SISTEMA DE CONTROL DE CAJA 𖨠──··· OPERADOR: " + nombre.upper() 
print("\n" + "๋࣭ ⭑⚝" * 15)
print()
print(mensaje_bienvenida)
print()
print("๋࣭ ⭑⚝" * 15)

pantalla_carga()

# CAPTURA DE FECHA  ⬩➤
fecha_valida = False
while not fecha_valida:
    try: 

        print("𖤐 💮💮💮 ESTABLECIENDO FECHA DE OPERACIÓN 💮💮💮 𖤐")
        dia = int(input("Ingrese el día actual (DD): "))

        mes = int(input("Ingrese el mes actual (MM): "))
        anio = int(input("Ingrese el año actual (AAAA): "))

        fecha = dia, mes, anio

        fecha_valida = True

    except ValueError:
        print("\n FORMATO INVÁLIDO. POR FAVOR INGRESE NÚMERO ENTEROS Y NO DEJE CAMPOS VACIOS. ")
        print(" !𖤐 REINTENTANDO CONFIGURACIÓN DE FECHA... \n")

        # Sintaxis requerida:
fecha_formateada = f"{fecha[0]}/{fecha[1]}/{fecha[2]}"
print(f"💮 Fecha de operación establecida: {fecha_formateada}💮")

matriz_menu = [
    ["1", "𖤐 Registrar una nueva venta"],
    ["2", "𖤐 Ver archivos de texto disponibles | Lectura de historiales"],
    ["3", "𖤐 Generar reporte manual del estado del almacen"],
    ["0", "𖤐 Cerrar caja y salir del sistema"]
]

opcion_principal = "-1"
actividad_detectada = False

while opcion_principal != "0":
    print("\n✩₊˚.⋆☾⋆⁺₊✧|✩₊˚.⋆☾⋆⁺₊✧|✩₊˚.⋆☾⋆⁺₊✧|✩₊˚.⋆☾⋆⁺₊✧|✩₊˚.⋆☾⋆⁺₊✧|✩₊˚.⋆☾⋆⁺₊✧")
    print(f" 𖤐 MENÚ PRINCIPAL ⬩➤ LOCAL POCKY YEM ")
    print(f" 𖤐 CAJERO RESPONSABLE ⧽ {nombre}")
    print(f" 𖤐 FECHA DE TRABAJO ⧽ {fecha_formateada}")

    for fila in matriz_menu:
        print(f" [{fila[0]}] ⬩➤ [{fila[1]}]")


    # CONTROL DE INACTIVIDAD | SIMULACIÓN 
    print("\n 𖤐 CONTROL DE INACTIVIDAD 𖤐")
    alerta_activa = True

    if actividad_detectada:
        print("ACTIVIDAD DETECTADA EN LA TERMINAL. CONTADOR DE TIEMPO REINICIADO")
        actividad_detectada = False
    else:
        respuesta = ""

        for minuto in range (1,12):
            if minuto == 11 and alerta_activa:
                print   ("\n 𖤐 ALERTA 𖤐  Han transcurrido 10 minutos de inactividad en la terminal.")
                respuestaV = False
                respuesta = ""

                while not respuestaV:
                    try:
                        respuesta = input("𖤐 ¿DESEA CONTINUAR LA SESIÓN ACTUAL? (ESCRIBA 'SI' O 'NO'): ")
                        if respuesta in ["si", "no"]:
                            respuestaV = True
                        else:
                            print("OPCIÓN INVÁLIDA. POR FAVOR ESCRIBA 'SI' O 'NO'")

                    except Exception as z:
                        print(f"ERROR AL LEER LA RESPUESTA {z} INTENTE DE NUEVO")
                        respuesta = "no"
                        respuestaV = True

        if respuesta == "no":
            print("\n 𖤐 TERMINAL BLOQUEADA POR INACTIVIDAD")
            print(" 𖤐 PARA DESBLOQUEAR EL SISTEMA SE REQUIERE UNA NUEVA AUTENTICACIÓN. ")
            nombre = solicitar_nombre_cajero()

        alerta_activa = False

    try:
        opcion_principal = input("SELECCIONE EL NÚMERO DE OPERACIÓN QUE DESEA REALIZAR: ").strip()
    except Exception as x: 
        print("𖤐 HUBO UN PROBLEMA AL LEER {x}")
        opcion_principal = -1


    if opcion_principal == "1":
        procesar_venta()
        actividad_detectada = True

    elif opcion_principal == "2":
        print("\n✩₊˚.⋆☾⋆⁺₊✧| CONSULTA DE ARCHIVOS DEL SISTEMA |✩₊˚.⋆☾⋆⁺₊✧")
        print("Archivos registrados disponibles:")
        for llave, nombre_archivo in Archivos_Sistema.items():
            print(f"[{llave}] ⬩➤ {nombre_archivo}")


        seleccionar = input("\n𖤐 Ingrese el número del archivo que desea leer: ").strip()

        if seleccionar in Archivos_Sistema:
            arhiv = Archivos_Sistema[seleccionar]
            print(f"\n DESPLEGANDO CONTENIDO DE {arhiv}")

            try: 
                with open(arhiv, mode="r") as arhiv_lector:
                    contenido = arhiv_lector.read()
                    if contenido.strip() =="":
                        print("EL ARCHIVO ESTA ACTUALMENTE VACIO")
                    else:
                        print(contenido)
                print("𖤐𖤐𖤐𖤐𖤐𖤐𖤐𖤐𖤐𖤐𖤐𖤐")
            except FileNotFoundError:
                print(f"ERROR 𖤐 EL ARCHIVO {arhiv} no existe en la caperta")
            except Exception as v: 
                print(f"ERROR IN ESPERADO AL LEER {v}")
        else:
            print("SLECCIÓN INVÁLIDA EN EL MENÚ")

        actividad_detectada = True

    elif opcion_principal == "3": 
        print("\n✩₊˚.⋆☾⋆⁺₊✧| GENERANDO REPORTE MANUAL DE ALMACÉN |✩₊˚.⋆☾⋆⁺₊✧")

        try:
            with open("inventario_incial.txt", mode="w") as arhiv_inv:
                arhiv_inv.write(f"REPORTE GENERADO EL {fecha_formateada} POR CAJERO: {nombre}\n")
                arhiv_inv.write(f"Existencias actuales en inventario: \n")
                arhiv_inv.write(f"Chocolate: {stk_chocolate} cajas\n")
                arhiv_inv.write(f"Matcha: {stk_matcha} cajas\n")
                arhiv_inv.write(f"Fresa: {stk_fresa} cajas\n")

            with open("registro_caja.txt", mode="a") as arhiv_lg:
                arhiv_lg.write(f"{fecha_formateada} Reporte hecho por el cajero {nombre}")

            print("Reportes de inventario y registro de caja guardados con éxito.")

        except Exception as h: 
            print(f"ERROR AL ESCRIBIR EL REPORTE: {h}")
        
        actividad_detectada = True

    elif opcion_principal == "0":
        print("CERRANDO TERMINAL...")

    else:
        print("OPCIÓN NO VÁLIDA")

print(f"CAJA CERRADA DE FORMA SEGURA. ¡EXCELENTE TURN, {nombre}!")


# OPCION 1 | PROCESAR VENTA ⬩➤