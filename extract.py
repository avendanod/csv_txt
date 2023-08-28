
#! ESTE ES UN EJERCICIO DE EJEMPLO OBSERVAR EL COMPORTAMIENTO
#! DE PYTHON TRABAJANDO COMO SCRIPTS.

#* ---------------------------------------------------------------------------------------------------

######     #    #     # ### ######        #    #     # ####### #     # ######     #    #     # ####### 
#     #   # #   #     #  #  #     #      # #   #     # #       ##    # #     #   # #   ##    # #     # 
#     #  #   #  #     #  #  #     #     #   #  #     # #       # #   # #     #  #   #  # #   # #     # 
#     # #     # #     #  #  #     #    #     # #     # #####   #  #  # #     # #     # #  #  # #     # 
#     # #######  #   #   #  #     #    #######  #   #  #       #   # # #     # ####### #   # # #     # 
#     # #     #   # #    #  #     #    #     #   # #   #       #    ## #     # #     # #    ## #     # 
######  #     #    #    ### ######     #     #    #    ####### #     # ######  #     # #     # ####### 
                                                                                               
#* ---------------------------------------------------------------------------------------------------

#! https://github.com/avendanod
#! https://tensify.net
#! avendanod@gmail.com

#! TOMA EL CONTENIDO DE UN ARCHIVO .CSV ENTREGADO POR EL USUARIO COMO UN PARÁMETRO Y DEVUELVE 
#! UN ARCHIVO TIPO TEXTO (.TXT) CON EL MISMO NOMBRE Y PATH DEL ARCHIVO ORIGINA

#$ IMPORTA LIBRERÍAS
import sys                                                          #-> sys PERMITE USAR FUNCIONES DEL INTERPRETER DE PYTHON
import csv                                                          #-> csv PERMITE INTERACTUAR CON ARCHIVOS TIPO CSV (Textos de Excel)
import os                                                           #-> csv PERMITE FUNCIONES DEL SISTEMA OPERATIVO

#$ TOMA EL ARCHIVO INDICADO
fileName = sys.argv[1]
print("-----------")
print("ARCHIVO ORIGEN: "+fileName)

#$ ORGANIZA EL NOMBRE EL ARCHIVO DESTINO
fileString = os.path.split(fileName)                                #-> SEPARA LA VARIABLE filename EN 2 PARTES dirArchivo y nomArchivo
dirArchivo = fileString[0]
nomArchivo = fileString[1].replace(".csv","")                       #-> EN LA VARIABLE nomArchivo, REEMPLAZA EL TEXTO ".CVS" POR "VACÍO"

#$ MUESTRA LA DIRECCIÓN Y EL ARCHIVO QUE INGRESÓ COMO PARÁMETRO
print("-----------")
print("DIRECCIÓN:   "+dirArchivo)
print("NOM ARCHIVO: "+nomArchivo)

#$ CREA EL NOMBRE DEL ARCHIVO DESTINO (con dirección)
nombreArchivoTexto = dirArchivo+"/"+"RESULTADO_"+nomArchivo+".txt"  #-> CONCATENA/ENCADENA LA VARIABLE dirArchivo + uUN slash + nomArchivo + UN TEXTO CON ".TXT"

#$ PREPARA EN LA MEMORIA UN ARCHIVO DE TEXTO TIPO "W"->ESCRITURA
tfile = open(nombreArchivoTexto, "w")                               #-> ESTA INSTRUCCIÓN CREAR UN ARCHIVO CON EL NOMBRE Y LA DIRECCIÓN INDICADO EN LA INSTRUCCIÓN ANTERIOR (y TIPO W ESCRITURA)

#$ MUESTRA UNA LÍNEA DE SEPARACIÓN
print("-----------")

#$ INICIA CICLO DE LECTURA DEL ARCHIVO CSV
with open(fileName, 'r') as file:                                   #-> AQUÍ INICIA UN BUCLE QUE SE EJECUTA LA CANTIDAD DE LINEAS QUE TRA EL ARCHIVO ORIGINAL fileName

  #. SEPARA POR "CARÁCTER SEPARADOR" en este caso ","
  csvreader = csv.reader(file, delimiter=',')                       #-> ESTA INSTRUCCIÓN LEE EL ARCHIVO ORIGINAL file, LINEA POR LINEA Y SEPARA POR EL DELIMITADOR ","
  for row in csvreader:                                             #-> PARA CADA FILA EN LA FILA LEÍDA DEL ARCHIVO ORIGEN

    #. ELIMINA EL STRING 'HDD ' y lo REEMPLAZA por VACÍO
    texto = row[3].replace("HDD ","")                               #-> DE CADA FILA TOMA LA POSICIÓN "3" y LE REEMPLAZA "HDD " POR "VACÍO" Y LA PONE EN LA VARIABLE texto
    
    #. MUESTRA LA VARIABLE
    print(texto)

    #. AGREGA EL CONTENIDO DE LA VARIABLE JUNTO A UN
    #. "RETORNO DE CARRO" como una linea en el archivo
    #. ".TXT" CREADO
    tfile.write(texto+"\n")                                         #-> EL CONTENIDO DE  LA VARIABLE texto LO AGREGA AL ARCHIVO DE TEXTO CREADO CON open() ANTES DEL CICLO

#$ MUESTRA EL MENSAJE AL CREAR FÍSICAMENTE EL ARCHIVO DE TEXTO
print("-----------")
print("ARCHIVO FINAL: "+nombreArchivoTexto)
tfile.close()                                                       #-> CIERRA EL ARCHIVO DE TEXTO Y LO CREA FÍSICAMENTE EN EL DISCO DURO

#$ MUESTRA EL MENSAJE AL FINALIZAR EL PROCESO
print("-----------")
print("ARCHIVO "+nomArchivo+".txt HA SIDO CREADO")