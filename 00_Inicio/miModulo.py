def pasar_a_mayusculas(ruta_archivo):
    #paso 1: abrir el archivo
    archivo = open(ruta_archivo,encoding='UTF-8')
    #paso 2: iterar sobre el archivo para acceder a cada linea
    for linea in archivo:
        print(linea.upper().strip())