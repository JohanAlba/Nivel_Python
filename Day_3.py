'''Crea una clase Estudiante con:
Atributos:

nombre (string)
edad (int)
notas (lista de números)

Métodos:

agregar_nota(nota): Agrega una nota a la lista
promedio(): Retorna el promedio de las notas
aprobado(): Retorna True si el promedio es >= 6, sino False
'''
# Ejemplo de uso:

class Estudiante:
    def __init__(self,nombre:str,edad:int,notas:list):
        self.nombre = nombre
        self.edad = edad
        self.notas = notas

    def agregar_nota(self,nota:int):

        self.notas.append(nota)
        return self.notas
    
    def Promedio(self):
        return sum(self.notas)/len(self.notas)
        
    def aprobado(self):
        if self.Promedio ()>=6:
            return True
        else:
            return False


estudiante = Estudiante("Juan", 20, [7, 8, 5])
estudiante.agregar_nota(9)
print(estudiante.Promedio())  # 7.25
print(estudiante.aprobado())  # True
'------------------------------------------------RETO 5----------------------------------------------'
'''
🎯 Reto 6: Manejo de excepciones
Crea una función dividir(a, b) que:

Divida a entre b
Maneje el error si b es cero (captura ZeroDivisionError)
Maneje el error si los parámetros no son números (captura TypeError)
Retorne el resultado o un mensaje de error apropiado'''
def dividir (a,b):
    try :
        total = a/b
        
    except ZeroDivisionError:
            
            return'b es = 0 '
    except TypeError:

        return 'No son numero'
    return total
# Ejemplos de uso:
print(dividir(10, 2))    # 5.0
print(dividir(10, 0))    # "Error: No se puede dividir entre cero"
print(dividir(10, "a"))  # "Error: Los parámetros deben ser números" 
    