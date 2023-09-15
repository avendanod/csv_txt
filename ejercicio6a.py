
# USANDO LA LIBRERíA sys EL DATO DE ENTRADA COMO PARÁMETRO
import sys
import os

# EL DATOS DE ENTRADA ES UN PATH DE UN ARCHIVO
fileDir = sys.argv[1]

# SPLIT SEPARA LA CADENA EN 2 PARTE: DIRECCIÓN Y NOMBRE DEL ARCHIVO Y LOS GUARDA EN UNA "TUPLA"
tuplaDir = os.path.split(fileDir)

# ALMACENA LOS ELEMENTOS DE LA TUPLA LLAMADA tuplaDir EN 2 VARIABLES
dirArchivo = tuplaDir[0]
nomArchivo = tuplaDir[1]  

# RESULTADO
print("TUPLA: "+str(tuplaDir))
print("Tipo: "+str(type(tuplaDir)))
print("elemento 0: ", str(dirArchivo))
print("elemento 1: ", str(nomArchivo))