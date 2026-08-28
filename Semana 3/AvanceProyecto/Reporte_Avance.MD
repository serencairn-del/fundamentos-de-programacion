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

* **Hay que insertar imagen... ¿cómo? ya veré xD**

---

## 6. Prototipo del código fuente (Python):

* ***Pendiente, también... ¬¬**
    
