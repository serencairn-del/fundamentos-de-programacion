# VERSIÓN PRUEBA DEL PROYECTO FINAL, EL CÓDIGO TERMINADO SERA TRASLADADO A UN CUADERNO DE JUPYTER Y EJECUTADO PARA UNA MEJOR
# LEGIBILIDAD PARA EL PROFESOR.

# IMPORTACIÓN DE LIBRERIAS ⬩➤

import time # Requerido para la pausa, prove funciones de control de tiempo
import pdb # Requerido para la depuración

# VARIABLES GLOBALES E INVENTARIO INCIAL ⬩➤

stk_chocolate = 21
stk_matcha = 18
stk_fresa = 15
preciopockys = 48

# DICCIONARIO PARA LAS OPCIONES DEL MENÚ ASOCIADA A LOS ARCHIVOS

Archivos_Sistema = {

    "1": "inventario_inicial.txt",
    "2": "ventas_diarias.txt",
    "3": "alertas_stock.txt",
    "4": "registro_caja.txt"
}

# FUNCIÓN PARA LA PANTALLA DE CARGA ⬩➤

def pantalla_carga():

    print("\n" + "✩₊˚.⋆☾𓃦☽⋆⁺₊✧" * 9)
    print()
    print("𖤐⬩➤INICIANDO SISTEMA DE GESTIÓN LOCAL POCKY YEM...")
    print()
    print("✩₊˚.⋆☾𓃦☽⋆⁺₊✧" * 9)


    #CICLO SIMPLE CON TEMPORIZADOR PARA SIMULAR LA CARGA DEL SISTEMA CON RETARDO CONTROLADO
    for i in range(1, 4):
        print(f"[𖤐𖤐𖤐] CARGANDO SISTEMA... [{i * 33}%]")
        time.sleep(1.5)

    print("\n[𖤐] SISTEMA INICIADO CORRECTAMENTE ^^")
    print("⬩➤" * 15 + "\n")

# ⬩➤

# Identificación del usuario con una función. ⬩➤



def solicitar_nombre_cajero():

    #INICIACIÓN DE VARIABLES LOCALES PARA EL CONTROL DE ESTE PROCESO

    nombre = ""
    nombre_valido = False

    # ESTRUCTURA WHILE-NOT QUE ASEGURA LA CAPTURA CORRECTA DE LOS DATOS CON UN FILTRO (.replace()isalpha() PARA VALIDAR
    # SOLO LETRAS OMITIENDO ESPACIOS CON UN RETORNO AL FLUJO PRINCIPAL DEL PROGRAMA)

    while not nombre_valido:
        nombre = input("Por favor, ingresar el nombre del cajero en turno ^^: ")
        if nombre != "" and nombre.replace(" ", "").isalpha():
            nombre_valido = True
        else:
            print("[⚠︎] ERROR. EL NOMBRE DEL CAJERO DEBE CONTENER SOLO LETRAS Y SIN ESPACIOS VACIOS. ")
            print("𖤐 INTENTE DE NUEVO SIN USAR NÚMEROS NI SIMBOLOS EXTRAÑOS ^^. \n")

    return nombre

# FUNCIÓN PARA PROCESAR LAS VENTAS ⬩➤


def procesar_venta():

    # SE DECLARAN VARIABLES GLOBALES COMPARTIDAS PARA LECTURA(ESCRITURA)
    global stk_chocolate, stk_matcha, stk_fresa, fecha, nombre

    print("\n✩₊˚.⋆☾⋆⁺₊✧| MÓDULO DE VENTAS POCKY YEM |✩₊˚.⋆☾⋆⁺₊✧")
    print(f"1. 𖤐 Pocky de Chocolate 𓂃 ོ𓂃 (Existencia: {stk_chocolate})")
    print(f"2. 𖤐 Pocky de Matcha 𓂃 ོ𓂃 (Existencia: {stk_matcha})")
    print(f"3. 𖤐 Pocky de Fresa 𓂃 ོ𓂃 (Existencia: {stk_fresa})")

    # BLOQUE TRY PARA EVITAR ENTRADAS ERRONEAS

    try:
        opcionmenu = int(input("𖤐 INGRESE EL SABOR REQUERIDO POR EL CLIENTE (1-3)ᨒ: "))
        if 1<= opcionmenu <=3:
            cantidad_c = int(input("𖤐 INGRESA CUÁNTAS CAJAS DE POCKY QUIERE EL CLIENTTE 𓂃🖊: "))

            if cantidad_c <= 0:
                print("[⚠︎] LA CANTIDAD DE CAJAS DEBE SER UN NÚMERO POSITIVO Y MAYOR A CERO. ")
                return

            # ASIGNACIÓN DE INDICE

            if opcionmenu == 1:
                stockdisponible = stk_chocolate
            elif opcionmenu == 2:
                stockdisponible = stk_matcha
            else:
                stockdisponible = stk_fresa

            # EVALUACIÓN DE LA TRANSACCIÓN

            if cantidad_c <= stockdisponible:
                precio_original = cantidad_c * preciopockys

                # DESCUENTO POR MAYOREO

                if cantidad_c > 6:
                    descuentoA = precio_original * 0.12
                else:
                    descuentoA = 0.0

                        #FORMULAS PARA HACER CALCULOS FINANCIEROS Y FISCALES

                subtotal_neto = precio_original -descuentoA
                impuestoIVA = subtotal_neto * 0.16
                totalpagoCIVA = subtotal_neto + impuestoIVA

                    # ALERTAS PARA LA SIMULACIÓN DEL CONTEO DE TIEMPO DE INACTIVIDAD

                alertas_generadas = "Ninguna"
                if opcionmenu == 1:
                    stk_chocolate -= cantidad_c
                    if stk_chocolate <= 6:
                        alertas_generadas = "⚠ ALERTA CHOCOLATE BAJO ⚠"
                        print("[¡⚠︎!] EL POCKY DE CHOCOLATE SE ESTÁ ACABANDO. PEDIR MÁS SUMINISTROS.")
                elif opcionmenu == 2:
                    stk_matcha -= cantidad_c
                    if stk_matcha <= 6:
                        alertas_generadas = "⚠ ALERTA MATCHA BAJO ⚠"
                        print("[¡⚠︎!] EL POCKY DE MATCHA SE ESTÁ ACABANDO. PEDIR MÁS SUMINISTROS.")
                elif opcionmenu == 3:
                    stk_fresa -= cantidad_c
                    if stk_fresa <= 6:
                        alertas_generadas = "⚠ ALERTA FRESA BAJO ⚠"
                        print("[¡⚠︎!] EL POCKY DE FRESA SE ESTÁ ACABANDO. PEDIR MÁS SUMINISTROS.")

                #FORMATO VISUAL PARA SIMULAR UN TICKET EN TERMINAL

                print("\n" + "๋࣭ ⭑⚝" * 8 + " TICKET DE VENTA " + "๋࣭ ⭑⚝" * 8)
                print(f" Importe original:   ${precio_original:.2f}")
                print(f" Descuento aplicado: -${descuentoA:.2f}")
                print(f" Subtotal Neto:      ${subtotal_neto:.2f}")
                print(f" IVA (16%):          ${impuestoIVA:.2f}")
                print(f" Total a Pagar:      ${totalpagoCIVA:.2f}")
                print("↟𖠰˚☀︎ᨒ↟𖠰"* 21)

                # BLOQUE DE CONTROL

                try:
                    fecha_txt = f"{fecha[0]}/{fecha[1]}/{fecha[2]}" # INDEXAMOS LOS DATOS DE LA TUPLA DE fecha GLOBAL

                    # Persistencia: Escritura en modo anexo ("a") con codificación estándar "utf-8" para soporte unicode
                    with open("ventas_diarias.txt", mode="a", encoding="utf-8") as file_ventas:
                        file_ventas.write(f"Fecha: {fecha_txt} | Cajero: {nombre} | Sabor: {opcionmenu} | Cajas: {cantidad_c} | Total: ${totalpagoCIVA:.2f}\n")

                    # Control de condiciones de resguardo para incidencias críticas de stock mínimo
                    if alertas_generadas != "Ninguna":
                        with open("alertas_stock.txt", mode="a", encoding="utf-8") as file_alertas:
                            file_alertas.write(f"|{fecha_txt}| {alertas_generadas} > Chocolate: {stk_chocolate}, Matcha: {stk_matcha}, Fresa: {stk_fresa}\n")
                    print("☾𖤓 VENTA REGISTRADA CORRECTAMENTE ☾𖤓")

                #captura cualquier error de este subsistema de archivos para prevenir roturas
                except Exception as error_archivo: 
                    print(f"⚠ ERROR AL INTENTAR ESCRIBIR LOS ARCHIVOS EN: {error_archivo}")
            else:
                print("⚠ EL ALMACEN NO CUENTA CON EXISTENCIAS SUFICIENTES ⚠")
        else:
            print("⚠ OPCIÓN DE SABOR INVALIDA EN EL PANEL DE VENTAS ⚠")

    except ValueError:
        print("⚠ ERROR, INGRESE ÚNICAMENTE NÚMEROS ENTEROS. ⚠")




print(" ⋆｡˚ ☁︎ ˚｡⋆｡˚☽˚｡⋆ IDENTIFICACIÓN DE PERSONAL ⋆｡˚ ☁︎ ˚｡⋆｡˚☽˚｡⋆")
nombre = solicitar_nombre_cajero() # invocamos a la función

 # Bienvenida con su contrucción para un despliegue en terminal presentable

mensaje_bienvenida = " 𖤐 BIENVENIDO AL SISTEMA DE CONTROL DE CAJA 𖨠──··· OPERADOR: " + nombre.upper() 
print("\n" + "๋࣭ ⭑⚝" * 15)
print()
print(mensaje_bienvenida)
print()
print("๋࣭ ⭑⚝" * 15)

pantalla_carga() # llamando a la función para la ejecución obligatoria para la pausa interactiva de carga

# CAPTURA DE FECHA  ⬩➤
fecha_valida = False  #variables para controlar el ciclo 
while not fecha_valida:
    try: 

        print("𖤐 💮💮💮 ESTABLECIENDO FECHA DE OPERACIÓN 💮💮💮 𖤐")
        dia_txt = input("Ingrese el día actual (DD): ")
        mes_txt = input("Ingrese el mes actual (MM): ")
        anio_txt = input("Ingrese el año actual (AAAA): ")

        # filtro para medir la longitud y restringir los caracteres de las cadenas
        if len(dia_txt) == 2 and len(mes_txt) == 2 and len(anio_txt) == 4:
            #conversion de la candena a enteros para hacer las evaluciones de rango
            dia = int(dia_txt)
            mes = int(mes_txt)
            anio = int(anio_txt)

            # evaluación de de rango usando el calendario gregoriano
            if 1 <= dia <=31 and 1 <= mes <=12 and anio > 0:

                # fecha provisional con el :02d para rellenar ceros a la izquierda
                fecha_provisional = f"{dia:02d}/{mes:02d}/{anio:02d}"
                print(f"REVISIÓN: La fecha ingresada es: {fecha_provisional}")

                # forma para validar la fecha y evitar errores operativos
                confirmacion = input("❀ ¿LA FECHA ES CORRECTA? (ESCRIBA SI O NO): ").strip().lower()
                if confirmacion == "si":
                    # empaquetamos y hacemos la tupla
                    fecha = dia, mes, anio
                    fecha_valida = True # camnio de estado para concluir la operación
                    print("[𖤐]Fecha confirmada y guardada en el sistema.\n")
                else:
                    print("\n[!] ENTENDIDO, REINICIANDO CAPTURA DE FECHA... ☼ᨒ\n")
            else: 
                print(" ⚠︎ ERROR: Los números ingresados están fuera del rango del calendario.")
                print("𖤐 Por favor, use días entre 01-31 y meses entre 01-12. \n")
        else:
            print("\n ⚠︎ ERROR: Longitud de dígitos incorrecta.")
            print("𖤐 Recuerde usar exactamente 2 dígitos para día (DD), 2 para mes (MM) y 4 para año (AAAA). \n")

    except ValueError:
        # captura de errores como letras o campos vacios en las conversiones int()
        print("\n ⚠︎ FORMATO INVÁLIDO. POR FAVOR INGRESE NÚMERO ENTEROS Y NO DEJE CAMPOS VACIOS. ⚠︎ ")
        print(" !𖤐 REINTENTANDO CONFIGURACIÓN DE FECHA... \n")

        # Sintaxis requerida desempaquetando y accediendo a los indices de la tupla
fecha_formateada = f"{fecha[0]}/{fecha[1]}/{fecha[2]}"
print(f"💮 Fecha de operación establecida: {fecha_formateada}💮")

# menu  ⬩➤
# menu en base a una matriz para acceder a las opciones

matriz_menu = [
    ["1", "⚝ Registrar una nueva venta"],
    ["2", "⚝ Ver archivos de texto disponibles | Lectura de historiales"],
    ["3", "⚝ Generar reporte manual del estado del almacen"],
    ["0", "⚝ Cerrar caja y salir del sistema"]
]

opcion_principal = "-1" # inicialización del control del bucle while
actividad_detectada = False # variable para simular y reiniciar el reloj del sistema


# ciclo principal
while opcion_principal != "0":
    print("\n✩₊˚.⋆☾⋆⁺₊✧|✩₊˚.⋆☾⋆⁺₊✧|✩₊˚.⋆☾⋆⁺₊✧|✩₊˚.⋆☾⋆⁺₊✧|✩₊˚.⋆☾⋆⁺₊✧|✩₊˚.⋆☾⋆⁺₊✧")
    print(f" 𖤐 MENÚ PRINCIPAL ⬩➤ LOCAL POCKY YEM ")
    print(f" 𖤐 CAJERO RESPONSABLE ⧽ {nombre.upper()}")
    print(f" 𖤐 FECHA DE TRABAJO ⧽ {fecha_formateada}")

    # for que recorre y despliega la matriz del menú
    for fila in matriz_menu:
        print(f" [{fila[0]}] ⬩➤ [{fila[1]}]")


    # CONTROL DE INACTIVIDAD | SIMULACIÓN  
    print("\n 𖤐 CONTROL DE INACTIVIDAD 𖤐")
    alerta_activa = True

    if actividad_detectada:
        # reseteando el reloj por operaciones efectuadas
        print("☪ ACTIVIDAD DETECTADA EN LA TERMINAL. CONTADOR DE TIEMPO REINICIADO ☪")
        actividad_detectada = False # apagando el reloj para la siguiente ronda del menú
    else:
        respuesta = "" # inicialización preventiva de la variable para evitar NameError por saltos de flujo

        # for para simular 10 minutos (reloj de inactividad)
        for minuto in range (1,12):
            #el umbral de tiempo es  el minuto 11
            if minuto == 11 and alerta_activa:
                print   ("\n 𖤐 ALERTA 𖤐  Han transcurrido 10 minutos de inactividad en la terminal.")
                respuestaV = False # variable de control para la validación del reloj
                respuesta = ""

                while not respuestaV:
                    try:
                        # captura de datos con strip y lowet para evitar un bug
                        respuesta = input("𖤐 ¿DESEA CONTINUAR LA SESIÓN ACTUAL? (ESCRIBA 'SI' O 'NO'): ").strip().lower()
                        if respuesta in ["si", "no"]:
                            respuestaV = True # entrada validada, se rompe el bucle interno
                        else:
                            print("⚠︎ OPCIÓN INVÁLIDA. POR FAVOR ESCRIBA 'SI' O 'NO' ⚠︎")

                    except Exception as z:
                        print(f"⚠︎ ERROR AL LEER LA RESPUESTA {z} INTENTE DE NUEVO")
                        respuesta = "no"
                        respuestaV = True

        # protección annte el abandono de la terminal por parte del usuario
        if respuesta == "no":
            print("\n 𖤐 𖤐𖤐 TERMINAL BLOQUEADA POR INACTIVIDAD")
            print(" 𖤐 PARA DESBLOQUEAR EL SISTEMA SE REQUIERE UNA NUEVA AUTENTICACIÓN. 𖤐")
            nombre = solicitar_nombre_cajero()

        alerta_activa = False # Desactivación de la alerta de la ronda actual


    # CAPTURA DE DATOS CON TRY PARA LA OPCIÓN PRINCIPAL DE LA OPERACIÓN

    try:
        opcion_principal = input("🏞 SELECCIONE EL NÚMERO DE OPERACIÓN QUE DESEA REALIZAR: ").strip()
    except Exception as x: 
        print(f"𖤐 HUBO UN PROBLEMA AL LEER {x} 𖤐")
        opcion_principal = "-1"

    # evaluación de las opciones seleccionadas en la matriz a través de la estructura if, elif, else con if dentro del flujo principal condicional

    if opcion_principal == "1":
        procesar_venta() # llamamos a la funcion que hace el proceso de ventas
        actividad_detectada = True #señal para resetear el reloj del menú

    elif opcion_principal == "2":
        #lectura de archivos desde el diccionario
        print("\n✩₊˚.⋆☾⋆⁺₊✧| CONSULTA DE ARCHIVOS DEL SISTEMA |✩₊˚.⋆☾⋆⁺₊✧")
        print("Archivos registrados disponibles:")
        for llave, nombre_archivo in Archivos_Sistema.items():
            print(f"[{llave}] ⬩➤ {nombre_archivo}")


        seleccionar = input("\n𖤐 Ingrese el número del archivo que desea leer: ").strip()
        # validación relacional, verifica si la opcion existe como llave válida en el diccionario
        if seleccionar in Archivos_Sistema:
            arhiv = Archivos_Sistema[seleccionar] # extracción del nombre del archivo
            print(f"\n ...DESPLEGANDO CONTENIDO DE {arhiv}")

            #control para lectura de archivos

            try: 
                with open(arhiv, mode="r", encoding="utf-8") as arhiv_lector:
                    contenido = arhiv_lector.read()
                    if contenido.strip() =="":
                        print("EL ARCHIVO ESTA ACTUALMENTE VACIO ⁀➴")
                    else:
                        print(contenido) # imprime en terminal el contenido de los archivos
                print("𖤐𖤐𖤐𖤐𖤐𖤐𖤐𖤐𖤐𖤐𖤐𖤐")
            except FileNotFoundError:
                print(f"ERROR 𖤐 EL ARCHIVO {arhiv} no existe en la caperta")
            except Exception as v: 
                print(f"ERROR INESPERADO AL LEER {v} ⁀➴")
        else:
            print("SLECCIÓN INVÁLIDA EN EL MENÚ")

        actividad_detectada = True

    elif opcion_principal == "3": 
        print("\n✩₊˚.⋆☾⋆⁺₊✧| GENERANDO REPORTE MANUAL DE ALMACÉN |✩₊˚.⋆☾⋆⁺₊✧")

        try:
            #  el modo "w" limpia los datos antiguos y escribe el estado actual de los inventarios
            with open("inventario_incial.txt", mode="w", encoding="utf-8") as arhiv_inv:
                arhiv_inv.write(f"REPORTE GENERADO EL {fecha_formateada} POR CAJERO: {nombre}\n")
                arhiv_inv.write(f"Existencias actuales en inventario: \n")
                arhiv_inv.write(f"Chocolate: {stk_chocolate} cajas\n")
                arhiv_inv.write(f"Matcha: {stk_matcha} cajas\n")
                arhiv_inv.write(f"Fresa: {stk_fresa} cajas\n")

            # El modo "a" añade los registros de venta al archivo sin alterar los renglones anteriores
            with open("registro_caja.txt", mode="a", encoding="utf-8") as arhiv_lg:
                arhiv_lg.write(f"{fecha_formateada} Reporte hecho por el cajero {nombre}\n")

            print("Reportes de inventario y registro de caja guardados con éxito. 𓂃 ִֶָ𐀔")

        except Exception as h: 
            print(f"ERROR AL ESCRIBIR EL REPORTE: {h}")
        
        actividad_detectada = True

    elif opcion_principal == "0":
        print("CERRANDO TERMINAL... ➤")

    else:
        print("OPCIÓN NO VÁLIDA")

print(f"𖤐 CAJA CERRADA DE FORMA SEGURA. ¡EXCELENTE TURNO, {nombre.upper()}! 𖤐") # CERRRAMOS EL SISTEMA
print("\n" + "✩₊˚.⋆☾𓃦☽⋆⁺₊✧" * 9)
