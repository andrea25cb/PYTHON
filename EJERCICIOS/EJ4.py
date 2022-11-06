
#append sirve para añadir elementos al final del array, como el push en javascript

def zoom (matriz):
    dim = len(matriz)*2 #numero de filas // zoom[0] devuelve num columnas *2 el doble
    zoom = [0] * dim #dimensiono a 0 todas las filas
   
    for i in range(dim):
        zoom[i] = [0] * len(matriz[0])*2 #num filas *2
   
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            for f in range(0,2):#matriz de 2x2
                for c in range (0,2):
                    zoom[i*2+f][j*2+c] = matriz[i][j]

    return zoom

def printMatriz (m):
    s=""
    for row in m: #por cada fila de la matriz
        for elem in row: #y por cada elemento de la fila
            s = s+ str(elem)+"  " #debo convertirlo a string para poder concatenar más numeros pasados a string
        s+="\n"
    return s #devuelvo el string
def enter_matriz(fila,col):#dimensiona una matriz con 0(el num de filas y col pero a 0) y le asigna valores desde el teclado con el input
    matriz = []
    for i in range(fila):
        a = [0]*col
        matriz.append(a)
    for i in range(fila):
        for c in range(col):
            matriz[i][c]= input("Elemento:")
    return matriz

a = [[1, 2,6], [3,4,5]]
z = zoom(a)
b = enter_matriz(3,2)
print(b)
print("matriz a")

print(printMatriz(a))
print ("Matriz z")
print(printMatriz(z))
z = zoom(z)
print(printMatriz(z))
z = zoom(z)
print(printMatriz(z))