""" variables """
# python sencible a minuscula y mayusculas
# las variables no pueden empezar por un digito
# print('Nombre del alumno: ', input('Ingresa tu nombre: ')) # 
# print(f'Nive de python: {input('Ingrase su nivel')}')

nombre = input('Nombre: ')
nivel = input('Ingrese su nivel: ')
print('Nombre del alumno: ', nombre)
print(f'Nive de python: {nivel}')

print(f'Hola {nombre} eres un {nivel}') # f-string
print('comenzaremos por la clase 1')


# print('hola mundo')  # el print es para imprimir en pantalla

# Fundamentos de Programación en Python

# Funciones
# Las funciones son bloques de código reutilizables que realizan una tarea específica.
# Ejemplo:
# def saludo(nombre):
#     return f'Hola, {nombre}'

# Listas
# Las listas son colecciones ordenadas y mutables de elementos.
# se pueden combinar, las listas respetan el orden, se pueden modificar
# Ejemplo:
mi_lista2 = [1, 2, 3, 'hola', True, [1, 2, 3]]
mi_lista = [1, 2, 3, 4, 5]

# Tuplas
# Las tuplas son colecciones ordenadas e inmutables de elementos. (no se pueden modificar) se ejecutan mas rapido
# Ejemplo:
mi_tupla = (1, 2, 3)

# Diccionarios
# Los diccionarios son colecciones desordenadas de pares clave-valor. la clave es unica no se puede repetir no modificar el valos se puede modificar
# Ejemplo:
mi_diccionario = {'nombre': 'Juan', 'edad': 30}

# Conjuntos
# Los conjuntos son colecciones desordenadas de elementos únicos.
# Ejemplo:
mi_conjunto = {1, 2, 3, 4, 5}

# tipos de datos en Python
# print(type(5)) # int
# print(type('hola')) # el print es para imprimir en pantalla
# print(type(True)) # boolean
# print(type(3.14)) # float


""" Entrade y salida de usuario """
# print("hola mundo, soy un programador", "como estan locas", sep=' - ')

# print('hola', input('como te llamas?'), 'bienvenido')

# print('''Diario de un viajero espacio
      
#       Fecha 2024-8-23
#       El baño se tapo en fue un mierde total por un dia completo, ya que la comida le cayo mal
#       todo el equipo.
      
#       Le tome una fota a la tierra y quedo increible desde el espaico exterior.''')




