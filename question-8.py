# Escribe un algoritmo, en pseudocódigo, javascript o python, que permita:  
# - Formar una cadena de la forma que indicaste en la pregunta anterior, con X cantidad de anillos. 
# - Obtener el costo de armar esta cadena de X piezas. (abrir = $20, cerrar = $35)

# Operaciones a utilizar. No definirlas, se sabe que la primera abre un anillo y la segunda une dos piezas.
# openRing(a)
# joinRings(a,b)
import sys

print('\n======================\nCONSTRUCTOR DE CADENAS\n======================\n')

def joinRing(a,b):
  print(f'Uniendo la pieza {a+1} y la {b+1}')

def openRing(a):
  print(f'\nAbriendo la pieza {a+1}')

def buildChain(pieces):
  openPrice = 20
  joinPrice = 35
  finalPrice = 0
  i = 1
  while i < pieces:
    if (i%2 ==1):
      openRing(i)
      finalPrice += openPrice
      joinRing(i, i-1)
      finalPrice += joinPrice
      # Existe una pieza al lado derecho, la presenta puede ser la final
      if ((i+1) < pieces):
        joinRing(i, i+1)
        finalPrice += joinPrice
    i += 1
  print(f'\nENHORABUENA!\nHa construido la cadena de {i} piezas, a un costo de ${finalPrice}')
  return finalPrice

print('Ingrese cuantas piezas desea unir. Si desea salir digite (s):')
opt = input()

if (opt == 's'):
  sys.exit()
  
buildChain(int(opt))
  
  
