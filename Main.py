# Ejemplo:
numeros = [5, 2, 8, 1, 9, 3]
# Debe retornar: {'suma': 28, 'promedio': 4.67, 'mayor': 9, 'menor': 1}
suma =sum(numeros)
promedio = suma/6
mayor =max(numeros)
menor=min(numeros)
print (f'Suma:{suma}, Promedio:{promedio:.2f}, Mayor:{mayor}, Menor:{menor}')
'----------------------------------------feed back--------------------------------------------------'
'1. El pedido era retornar un diccionario, no imprimir:'

def analizar_numeros(numeros):
    suma = sum(numeros)
    promedio = round(suma / len(numeros), 2)  # Usa len() en vez de hardcodear el 6
    mayor = max(numeros)
    menor = min(numeros)
    
    return {
        'suma': suma,
        'promedio': promedio,
        'mayor': mayor,
        'menor': menor
    }
# Uso:
resultado = analizar_numeros([5, 2, 8, 1, 9, 3])
print(resultado)
'------------------------------------------Ejercicio 2----------------------------------------------'
'Crea una función que reciba una cadena de texto y retorne un diccionario con la frecuencia de cada palabra (sin importar mayúsculas/minúsculas).'
# Ejemplo:
palabras = "Hola mundo hola Python python es genial"
# Debe retornar: {'hola': 2, 'mundo': 1, 'python': 2, 'es': 1, 'genial': 1}
def contador(texto: str):
    frecuencia = {}
    texto = texto.lower()           # ✓ Guarda el resultado
    lista_palabras = texto.split()  # ✓ Guarda el resultado y usa otro nombre

    for palabra in lista_palabras:  # ✓ Itera sobre la LISTA
        if palabra in frecuencia:
            frecuencia[palabra] += 1  # ✓ Operador correcto
        else:
            frecuencia[palabra] = 1   # ✓ Asigna al diccionario correctamente
    
    return frecuencia

print(contador(palabras))

    
    
    












