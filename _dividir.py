

import sys
import csv
import os

fileName = sys.argv[1]
print("-----------")
print("ARCHIVO ORIGEN: "+fileName)

fileString = os.path.split(fileName)
dirArchivo = fileString[0]
nomArchivo = fileString[1].replace(".csv","")

print("-----------")
print("DIRECCIÓN:   "+dirArchivo)
print("NOM ARCHIVO: "+nomArchivo)

nombreArchivoTexto = dirArchivo+"/"+"RESULTADO_"+nomArchivo+".txt"

tfile = open(nombreArchivoTexto, "w")

print("----------- INICIO DE PROCESO -----------------")

with open(fileName, 'r') as file:

  csvreader = csv.reader(file, delimiter=',')
  for row in csvreader:
    texto = row[3].replace("HDD ","")
    print(texto)
    tfile.write(texto+"\n")

print("----------- PROCESO FINALIZADO ------------------")
print("ARCHIVO "+nomArchivo+".txt HA SIDO CREADO EN LA CARPETA ORIGINAL")
tfile.close()
