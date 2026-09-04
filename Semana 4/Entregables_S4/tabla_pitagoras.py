# Maria Estrella Arreola Yañez

# Crear una lista vacia que contendra la matriz
# Hacer un ciclo for con otro ciclo for adentro para leer filas y columnas; hay que agregar esto a la lista vacia.

#Hay que definir una función almacene a la matriz e imprima solamente; luego recorrer a la matriz fila x fila 
#También número x número.
#Luego, mostrar los números (tabla) alineados por columnas y empezar cada fila en una nueva línea.
#Definir una fucnión que nos retorne el valor de la tabla, cada fila y cada columna accediendo a cada valor "restando"
# hay que tener en cuenta el defase (se empieza desde el cero aunque en pantalla aparazeca del 1 al 10)
# 

tbl = []

for r in range(1,11):
    fls = [] # 
    for c in range(1,11):
        fls.append(r * c)
    tbl.append(fls)

def tablaimp(tbl):
    for f  in tbl:
        for cd in f:
            print(cd, end="\t")
        print()

def consultaR(tbl, ren, col):
    rel = tbl[ren -1][col -1]
    return rel

tablaimp(tbl)

entrada1f = int(input("Ingresa el primer valor: "))
if entrada1f <1 or entrada1f >10:
    print("Ingresa solo valores entre 1 y 10")
    # Aquí nos falta algo....

entrada2c = int(input("Ingresa el seegundo valor: "))
if entrada2c <1 or entrada2c >10:
    print("Ingresa solo valores entre 1 y 10")
    # Aquí también.... 
    

respuesta = consultaR(tbl, entrada1f, entrada2c)

print(f"El producto de {entrada1f} x {entrada2c} es: {respuesta}")