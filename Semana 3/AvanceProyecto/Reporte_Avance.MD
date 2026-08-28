# AVANCE DE PROYECTO (FASE 1):

**MARIA ESTRELLA ARREOLA YAÑEZ**

**Importante:** La organización es ficticia.

---

**Organización:** Local Pocky YEM
**Área de impacto:** Gestión de inventario de sabores y área de cajas.
**Responsable:** Aoki Takano (cajero del local)

---

## 1. Análisis técnico y definición del problema:

### Descripción del problema:
El local tiene perdidas financieras y desabasto constante de los sabores populares de su tienda debido a que las ventas y el inventario se hacen manualmente en el cierre diario. Esto hace que haya ineficiencia en las existencias fisicas de pockys y mal conteo del dinero ganado cada día.

### Reglas del negocio: 
1. El sistema tiene que operar mostrando un menu con los tres sabores estandar que maneja el local (Chocolate, Matcha, Fresa) y tener una opción de salida vidente.
2. Cada transacción debe calcular un subtotal neto (es el resultado de restar los decuentos al precio original), evaluar si la compra excede las 6 cajas de cualquier sabor para así aplicar un 12% de descuento y cobrar el 16% de IVA.
3. Cada venta hecha debe restar las unidades del stock especifico de ese sabor. Además si el restante de ese stock es inferior/igual a 6 unidades, el sistema tiene que mandar una alerta preventiva.

---

## 2. Listado de requerimientos obligatorios:

* **R1:** Desplegar un menú donde se muestre los tres sabores que maneja el local.
    * *Variable:* pendiente
* **R2:** Pedir al cajero la cantidad exacta de cajas que se desean adquirir.
    * *Variable:* pendiente
* **R3:** El sistema tiene que validar la existencia fisica del sabor en el stock actual antes de proceder a la venta.
    * *Variable:* pendiente
* **R4:** Calcular el subtotal neto haciendo los descuentos si excede las 6 unidades (cajas).
    * *Variable:* pendiente
* **R5:** Desglosar/mostrar? el cobro final incluyendo el IVA (16%); es importante primero realizar el descuento porque sino le cobraremos de más al cliente xD.
    * *Variable:* pendiente
* **R6:** Hay que registrar el nombre del cajero responsable de la terminal.
    * *Variable:* pendiente

---

## 3. Estructuras de control:

* **Estructura de ciclos:** Hay que simular una caja... así que el programa se tiene que mantenere en ejecución y poner una opción de salir. ('While')
* **Estructura de desición:** Se tiene "leer" a los stocks por sabor, hacer descuentos por mayoreo y mostrar alarmas cuando haya poco inventario... posiblemente un ('if-elif-else')

---

## 4. Diseño de algoritmo (Pseudocódigo en Psent):

* **Código Psent:** Pendiente.

---

## 5. Diseño de algoritmo (Diagrama de flujo sacado de Psent):

Algoritmo LocalPockyYEM
	Definir stk_chocolate, stk_matcha, stk_fresa, cantidad c, opcionmenu Como Entero
	Definir preciopockys, precio_original, descuentoA, impuestoIVA, totalpagoCIVA Como Real
    Definir nombre_responsable Como Cadena
    Definir stockdisponible Como Entero
	// Inicialización de Variables
    stk_chocolate <- 21
    stk_fresa <- 18
    stk_matcha <- 15
    preciopockys <- 48.0
    nombre_responsable <- "Aoki Takano"
    opcionmenu <- 0
    
    // Ciclo de Operación 
    Mientras opcionmenu <> 4 Hacer
        Escribir "MENU DE LOCAL POCKY YEM"
        Escribir "Cajero de turno: ", nombre_responsable
        Escribir "1. Pocky Chocolate (Stock: ", stk_chocolate, ")"
        Escribir "2. Pocky Matcha (Stock: ", stk_matcha, ")"
        Escribir "3. Pocky Fresa (Stock: ", stk_fresa, ")"
        Escribir "4. Cerrar menú"
        Escribir "Seleccione una opcion del menu:"
        Leer opcionmenu
        
        Si opcionmenu >= 1 Y opcionmenu <= 3 Entonces
            Escribir "Ingresa cuántas cajas de Pocky quiere el cliente:"
            Leer cantidad_c
            
            Si cantidad_c <= 0 Entonces
                Escribir "Error: La cantidad de cajas debe ser un número positivo y mayor a cero."
            Sino
                // Asignación de Stock 
                Segun opcionmenu Hacer
                    1: stockdisponible <- stk_chocolate
                    2: stockdisponible <- stk_matcha
                    3: stockdisponible <- stk_fresa
                FinSegun
                
                // Modelo de Entrada-Proceso-Salida
                Si cantidad_c <= stockdisponible Entonces
                    precio_original <- cantidad_c * preciopockys
                    
                    // Condicional de Descuento 
                    Si cantidad_c > 6 Entonces
                        descuentoA <- precio_original * 0.12
                    Sino
                        descuentoA <- 0.0
                    FinSi
                    
                    impuestoIVA <- (precio_original - descuentoA) * 0.16
                    totalpagoCIVA <- (precio_original - descuentoA) + impuestoIVA
                    stockdisponible <- stockdisponible - cantidad_c
                    
                    // Actualización física de inventarios y alertas
                    Segun opcionmenu Hacer
                        1:
                            stk_chocolate <- stockdisponible
                            Si stk_chocolate <= 6 Entonces
                                Escribir "¡ALERTA! EL POCKY DE CHOCOLATE SE ESTA ACABANDO. HAY QUE PEDIR MÁS SUMINISTROS."
                            FinSi
                        2:
                            stk_mactha <- stockdisponible
                            Si stk_mactha <= 6 Entonces
                                Escribir "¡ALERTA! EL POCKY DE MATCHA SE ESTÁ ACABANDO. HAY QUE PEDIR MÁS SUMINISTROS."
                            FinSi
                        3:
                            stK_fresa <- stockdisponible
                            Si stk_fresa <= 6 Entonces
                                Escribir "¡ALERTA! EL POCKY DE FRESA SE ESTÁ ACABANDO. HAY QUE PEDIR MÁS SUMINSITROS."
                            FinSi
                    FinSegun
                    
                    // Salida del resumen de venta
                    Escribir "--- REGISTRO DE VENTA ---"
                    Escribir "Importe original:  $", precio_original
                    Escribir "El descuento aplicado (12%): $", descuentoA
                    Escribir "IVA: $", impuestoIVA
                    Escribir "Total a Pagar:  $", totalpagoCIVA
                    Escribir "------------------------"
                Sino
                    Escribir "EL ALMACEN NO CUENTA CON EXISTENCIAS SUFICIENTES"
                FinSi
            FinSi
        Sino
            Si opcionmenu = 4 Entonces
                Escribir "Cerrando sistema"
            FinSi
        FinSi
        Escribir "Opción invalida en el sistema."
    FinMientras
    Escribir "CAJA CERRADA"
	
FinAlgoritmo

---

## 6. Prototipo del código fuente (Python):

* ***Pendiente, también... ¬¬**
    
