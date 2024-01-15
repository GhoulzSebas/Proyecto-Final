

patrones = []

contraseñas = []

subcadena = ""

def abrir_archivos(archivos, lista):

    with open(archivos, "r", encoding="utf8") as archivos:
        for data in archivos :
            contraseña = data.rstrip()
            lista += [contraseña]
        
    

abrir_archivos("patronesobvios.txt",patrones)
abrir_archivos("contraseña.txt",contraseñas)

def calcular_puntos_de_seguridad(patterns, passwords):
    
    minusculas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    mayusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    numeros = ["0","1","2","3","4","5","6","7","8","9"]
    puntos_de_seguridad = 0
    puntos_de_seguridad_arr = []
    
    for i in passwords:
        puntos_de_seguridad = 0
        ciclo_minusculas = 0
        ciclo_mayusculas = 0
        ciclo_numeros = 0
        ciclo_caracteres_especiales = 0
        
        for k in i:
            if k in minusculas:
                if ciclo_minusculas == 0:
                    
                    puntos_de_seguridad += 1
                    ciclo_minusculas = 1
                    continue
                else: 
                    continue
            elif k in mayusculas:
                if ciclo_mayusculas == 0:
                    puntos_de_seguridad += 1
                    ciclo_mayusculas = 1
                    continue
                else:
                    continue

            elif k in numeros:
                if ciclo_numeros == 0:
                    puntos_de_seguridad += 1
                    ciclo_numeros = 1
                    continue
            else:
                if ciclo_caracteres_especiales == 0:
                    puntos_de_seguridad += 3
                    ciclo_caracteres_especiales = 1
                    continue
                else:
                    puntos_de_seguridad += 2
                    continue
    
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
    with open("ejemplo.txt","a") as archivo_final:
        archivo_final.write("          Contraseña          |          Categoría          |          Puntos de seguridad \n")
        for posicion in range(len(passwords)):
            archivo_final.write(f"{passwords[posicion]}  | {cattegories[posicion]}  |  {points[posicion]}, \n"  )
    
exportar_archivo(contraseñas,clasificacion_contraseñas,puntos_de_seguridad_arreglo)

             
