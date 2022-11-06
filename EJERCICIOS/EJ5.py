cesta = {}
continuar = True

while continuar: #mientras pulse y
    item = input('Introduce un artículo: ')
    precio = float(input('Introduce el precio de ' + item + ': '))
    cesta[item] = precio
    continuar = input('¿Quieres añadir más artículos? (y/n)? ') == "y"
coste = 0
print('LISTA DE LA COMPRA:')
print ('----------------------')
for item, precio in cesta.items():
    print(item, '\t', precio)
    coste += precio
print ('________________________')
print('COSTE TOTAL: ', coste)
