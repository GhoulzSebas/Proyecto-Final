# Sebastián Pérez C.I: 31.748.129
# Sjglys Xavier Luis C.I: 31.877.913



patrones = []

contraseñas = []

subcadena = ""

def abrir_archivos(archivos, lista):
    #leer archivo
    with open(archivos, "r", encoding="utf8") as archivos:
        for data in archivos :
            contraseña = data.rstrip()
            #pasar contraseña o patrón obvio a un arreglo
            lista += [contraseña]
        
    

abrir_archivos("patronesobvios.txt",patrones)
abrir_archivos("contraseña.txt",contraseñas)

def calcular_puntos_de_seguridad(patterns, passwords):
    
    minusculas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    mayusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    numeros = ["0","1","2","3","4","5","6","7","8","9"]
    puntos_de_seguridad = 0
    puntos_de_seguridad_arr = []
    #iterar sobre el arreglo con las contraseñas
    for i in passwords:
        puntos_de_seguridad = 0
        ciclo_minusculas = 0
        ciclo_mayusculas = 0
        ciclo_numeros = 0
        ciclo_caracteres_especiales = 0
        #iterar cada caracter de la contraseña para verificar si es una letra mayúscula, minúsculas, un numero, o un caracter especial
        for k in i:
            #Verificar la existencia de minúsculas en la contraseña
            if k in minusculas:
                if ciclo_minusculas == 0:
                    
                    puntos_de_seguridad += 1
                    ciclo_minusculas = 1
                    continue
                else: 
                    continue
            #Verificar la existencia de mayúsculas en la contraseña
            elif k in mayusculas:
                if ciclo_mayusculas == 0:
                    puntos_de_seguridad += 1
                    ciclo_mayusculas = 1
                    continue
                else:
                    continue
            
            #Verificar la existencia de números en la contraseña
            elif k in numeros:
                if ciclo_numeros == 0:
                    puntos_de_seguridad += 1
                    ciclo_numeros = 1
                    continue
            #Verificar la existencia de caracteres especiales en la contraseña
            else:
                if ciclo_caracteres_especiales == 0:
                    puntos_de_seguridad += 3
                    ciclo_caracteres_especiales = 1
                    continue
                else:
                    puntos_de_seguridad += 2
                    continue
        
        #verificar si existen patrones obvios en la contraseña 
        for patron_obvio in patterns:
            for caracter in range(len(i)):
                subcadena = ""
                for j in range(caracter,len(i)):
                    subcadena += i[j]
                    if subcadena == patron_obvio:
                        puntos_de_seguridad -= 5
        

        puntos_de_seguridad_arr += [puntos_de_seguridad + len(i)]

    return puntos_de_seguridad_arr

puntos_de_seguridad_arreglo = calcular_puntos_de_seguridad(patrones,contraseñas)

print(puntos_de_seguridad_arreglo)

def clasificar_contraseñas(puntos_de_seguridad_array):
    clasificacion_contraseñas = []
    for puntos in puntos_de_seguridad_array:
        if puntos <= 15 :
            clasificacion_contraseñas += ["Debil"]
        elif puntos > 15 and puntos <= 20 :
            clasificacion_contraseñas += ["Moderada"]
        elif puntos > 20 and puntos <= 35:
            clasificacion_contraseñas += ["Buena"]
        elif puntos > 35 and puntos <= 100:
            clasificacion_contraseñas += ["Excelente"]
        elif puntos > 100 :
            clasificacion_contraseñas += ["Impenetrable"]
    
    return clasificacion_contraseñas

clasificacion_contraseñas = clasificar_contraseñas(puntos_de_seguridad_arreglo)

print(clasificacion_contraseñas)

def ordenamiento_burbuja(contraseñas_archivo,puntos_de_seguridad_ar,categoria_de_contraseñas):
    for i in range(len(puntos_de_seguridad_ar)):
        for j in range(len(puntos_de_seguridad_ar) -1 -i):
            if puntos_de_seguridad_ar[j] < puntos_de_seguridad_ar[j + 1]:

                aux = puntos_de_seguridad_ar[j]
                puntos_de_seguridad_ar[j] = puntos_de_seguridad_ar[j + 1]
                puntos_de_seguridad_ar[j + 1] = aux

                aux = contraseñas_archivo[j]
                contraseñas_archivo[j] = contraseñas_archivo[j + 1]
                contraseñas_archivo[j + 1] = aux

                aux = categoria_de_contraseñas[j]
                categoria_de_contraseñas[j] = categoria_de_contraseñas[j + 1]
                categoria_de_contraseñas[j + 1] = aux

ordenamiento_burbuja(contraseñas,puntos_de_seguridad_arreglo,clasificacion_contraseñas)

print(contraseñas)
print(puntos_de_seguridad_arreglo)
print(clasificacion_contraseñas)

def exportar_archivo(passwords,cattegories,points):
    #crear nuevo archivo y escribir las contraseñas, categoría a la que pertenecen y los puntos de seguridad respectivamente
    with open("contraseñas_ordenadas.txt","w") as archivo_final:
        archivo_final.write("          Contraseña          |          Categoría          |          Puntos de seguridad \n")
        for posicion in range(len(passwords)):
            archivo_final.write(f"{passwords[posicion]}  | {cattegories[posicion]}  |  {points[posicion]} \n"  )
    
exportar_archivo(contraseñas,clasificacion_contraseñas,puntos_de_seguridad_arreglo)

             
