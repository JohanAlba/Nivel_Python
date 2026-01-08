'''
🎯 Reto 7: Lectura y escritura de archivos
Crea una función contar_palabras_archivo(nombre_archivo) que:

Lea un archivo de texto
Cuente cuántas palabras tiene en total
Maneje el error si el archivo no existe
Retorne el número de palabras o un mensaje de error

Luego crea otra función escribir_resultado(nombre_archivo, contenido) que:

Escriba el contenido en un archivo
Maneje posibles errores '''
# Ejemplo de uso:

# 1. Primero crea un archivo de prueba
escribir_resultado = "Andre me maltrata y me patelea pero yo asi la amo"

# 2. Luego cuenta las palabras
#print(contar_palabras_archivo("prueba.txt"))  # 5

# 3. Si el archivo no existe:
#print(contar_palabras_archivo("noexiste.txt"))  # "Error: Archivo no encontrado"
def crear_Archivo(texto:str):
    with open("PRUEBA.txt", 'w') as archivo:
        archivo.write(texto)
    return archivo
#rear_Archivo(escribir_resultado)

def leer_archivo(archivo:str):
    try :
        with open(archivo,"r") as archivo:
            contenido = archivo.read()
        contar = contenido.split()
        return f"El archivo tiene :{len(contar)} palabras"
    except FileNotFoundError:
        return "Archivo no encontrado "

archivo = 'PRUEBA.txt'
print(leer_archivo(archivo))