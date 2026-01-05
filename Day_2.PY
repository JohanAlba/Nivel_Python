'''🎯 Reto 3: List Comprehensions
Crea una función que reciba una lista de números y retorne solo los números pares elevados al cuadrado.'''
# Ejemplo:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Debe retornar: [4, 16, 36, 64, 100]
def comprehensions (lista:list):
    pares = []
    for n in lista:
        if n % 2 == 0:
            pares.append(n**2) 
    return pares
print(comprehensions(numeros))
'-----extra-----'
def comprehensions(lista: list):
    return [n**2 for n in lista if n % 2 == 0]

print(comprehensions(numeros))
# [4, 16, 36, 64, 100]
'-----------------------------------------------------RETO 4-------------------------------------------------------------'
'''
🎯 Reto 4: Manipulación de strings
Crea una función que reciba una frase y retorne un diccionario con:

La frase invertida
Las vocales que contiene (sin repetir, en una lista)
El número de palabras'''

# Ejemplo:
frase = "Python es genial"
# Debe retornar: {
#     'invertida': 'laineg se nohtyP',
#     'vocales': ['o', 'e', 'i', 'a'],
#     'palabras': 3
# }
def manipulacion(palabra:str):
    
    invertida = palabra[::-1]
    
    palabras = len(palabra.split())
    
    vocales = set()
    for v in palabra.lower():
        if v in ['a','e','i','o','u']:
            vocales.add(v)
        
 

    
    return {'Invertida' : invertida,
            'Vocales' : vocales,
            'Palabra' : palabra}
print(manipulacion(frase))