#importamos las librerías necesarias
import numpy
import random

#sacamos las  notas aleatorias
notas = random.sample(range(0, 100), 15)
print(notas)

#calculamos la media
media = sum(notas)/15

#imprimimos la nota media
print(f"La nota media es de {media}")

#ordenamos las notas en orden ascendente para calcular la mediana
notas_ordenadas = sorted(notas)
#print(notas_ordenadas)

#imprimimos la mediana (valor de indice 7)
print(notas_ordenadas[7])

#calculamos la cantidad de valores por encima de la media
#creamos un contador
contador = 0
for nota in notas:
    if nota > media:
        contador += 1
        continue
    else:
        continue

#imprimimos la cantidad de valores por encima de la media
print(f"La cantidad de notas por encima de la media es de {contador}")

#calculamos la desviacion tipica S = ((sum(x-media)^2)/n-1)^1/2
for nota in notas:
    desviacion_tipica_num = sum(((nota)-(media))**2)
    desviacion_tipica = (desviacion_tipica_num/14)**(1/2)