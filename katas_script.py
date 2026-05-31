
# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
# de cada letra en la cadena. Los espacios no deben ser considerados.


# código sin función para simplificar
cadena_texto = input("Inserte su texto: ").replace(" ", "")

frecuencia = {}

for i in cadena_texto:
    if i in frecuencia:
        frecuencia[i] += 1
    else:
        frecuencia[i] = 1

print(frecuencia)


# código con función

def contador_ch(cadena_texto):
    """
    Devuelve la frecuencia de cada letra de una cadena de texto

    Args:
        cadena_texto (str): input del texto

    Returns:
        dict: frecuencia de cada letra
    """    

    frecuencia = {}

    cadena_texto = cadena_texto.replace(" ", "")

    for i in cadena_texto:
        if i in frecuencia:
            frecuencia[i] += 1
        else:
            frecuencia[i] = 1

    return frecuencia


texto = input("Inserte su texto: ")
resultado = contador_ch(texto)

print(resultado)


# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

def sqr(num):
    """eleva al cuadrado

    Args:
        num (int): numero

    Returns:
        int: numero al cuadrado
    """    
    return num**2

a = [3,5,6,1,9]
doble_a = list(map(sqr, a))
doble_a


# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

# teniendo en cuenta que "palabra objetivo" es subcadena, en este ejemplo será la "a"

# creas función con dos parametros, se tiene que tener en cuenta mayúsculas, posibles comas, y pasar str a list (split)

pregunta = input("Escribe 5 palabras: ").lower().replace(",", "")
lista_palabras = pregunta.split()
target = "a"
            
def dime_palabras(a=lista_palabras, b=target):
    """identifica las palabras que tienen un target especifico, dado una lista de palabras

    Args:
        a str:  input con las 5 palabras --> lista_palabras.
        b str: substring, lo que tienen que contener las palabras

    Returns:
        _list: lista final de palabras que tienen el target
    """    
    lista_final = []
    for palabra in a:
        if b in palabra:
            lista_final.append(palabra)
    return lista_final

final_list = dime_palabras(a=lista_palabras, b=target)
print(final_list)


# como list comprehension
pregunta = input("Escribe 5 palabras: ")
lista_palabras = pregunta.lower().replace(",", "")
target = "a"

def dime_palabras(a=lista_palabras, b=target):
    return [palabra for palabra in a.split() if b in palabra]

final_list = dime_palabras(a=lista_palabras, b=target)
print(final_list)


# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

#map(funcion,iterable1, iterable2...)
a = [3, 5, 7, 4] 
b = [1, 3, 6, 2]

def difference(a, b):
    """calcula la diferencia

    Args:
        a (list): lista de numeros
        b (list): lista de numeros

    Returns:
        list: diferencia
    """    
    return a-b

resultado1 = map(difference, a, b)
print(list(resultado1))


# 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
# defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
# que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
# una tupla que contenga la media y el estado.


notas = [7, 9.3, 5, 3.4, 8.2, 4.7]
nota_aprobado = 5

def media(a = notas, b = nota_aprobado):
  """hace la media de una lista de notas y califica si es aprobado o suspenso segun el valor dado del segundo parametro

  Args:
      a (list): lista de notas.
      b (int): nota_aprobado.

  Returns:
      tuple: media y estado
  """  
  mean = sum(notas)/len(notas)
  if mean >= nota_aprobado:
    return mean, "aprobado"
  else:
    return mean, "suspenso"
  
result = tuple(media(a = notas, b = nota_aprobado))
result
        
# 6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(number):
    """calcula el factorial de un numero de manera recursiva

    Args:
        number (int): el numero dado

    Raises:
        ValueError: si es negativo

    Returns:
        int: factorial
    """    
    if number == 0:   #caso base
        return 1
    elif number > 0:
        return number * factorial(number - 1) #recursividad
    else: 
        raise ValueError("no se puede calcular factorial de número negativo")

ejemplo = factorial(3)
ejemplo
    
# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

#map(function,iterable)
# str(x), tuplaslist

#separa las tuplas y conviertes en str

tuplaslist = [("perro", "gato"), ("leon", "tigre")]

def convertidor_strings(tupla):
    """convierte tupla a str

    Args:
        tupla (tuple)

    Returns:
        str
    """    
    return str(tupla)

resultado_map = list(map(convertidor_strings, tuplaslist))
print(resultado_map)

# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
# o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
# indicando si la división fue exitosa o no.

try:
    a = int(input("Escribe un número"))
    b = int(input("Escribe otro número"))
    result = a/b
except ValueError:
    print("no has escrito un número")
    print("La división NO fue exitosa :(")
except ZeroDivisionError:
    print("no puedes dividir por 0")
    print("La división NO fue exitosa :(")
else:
    print(result)
    print("La división fue exitosa :)")

# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
# excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
# "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

lista_mascotas = ['perro', 'gato', 'buho', 'escalopendra', 'tigre', 'zorro', 'cocodrilo', 'oso', 'ardilla', 'mapache', 'primate', 'serpiente pitón']

prohibidos = ["mapache", "tigre", "serpiente pitón", "cocodrilo", "oso"]

def animales_permitidos(animal):
    """toma una lista de animales y la devuelve excluyendo mascotas prohibidas

    Args:
        animal (str): un animal de lista de animales

    Returns:
        str: un animal que no está en prohibidos
    """    
    return animal not in prohibidos

lista_filtrada = list(filter(animales_permitidos, lista_mascotas))

print(lista_filtrada)

# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente

numeros = input("Escribe los números separados por espacios: ")

lista_numeros = list(map(float, numeros.split()))

def promedio(num):
    """calcula el promedio

    Args:
        num (list): lista de numeros

    Raises:
        ValueError: lista vacia

    Returns:
        int: promedio
    """    
    if len(num) == 0:
        raise ValueError("La lista está vacía")
    
    return sum(num) / len(num)

try:
    media = promedio(lista_numeros)
    print("El promedio es:", media)
except ValueError as e:
    print(e)

# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

# resolví este ejercicio pensando en para qué crearía un programa que pidiese al usuario que introdujera la edad,
#  así que lo compliqué con algunos condicionales

class OutofrangeError(Exception):  #creacion de error personalizado
    pass

def edad(e):
    if e < 0 or e > 120:
        raise OutofrangeError("Edad fuera de rango")
    elif e >= 18:
        return "Puedes beber alcohol"
    else:
        return "Aún no puedes beber alcohol"

try:
    age = int(input("Escribe tu edad: "))
    permiso_beber = edad(age)
    print(permiso_beber)

except ValueError:
    print("No has escrito un número")

except OutofrangeError:
    print("Está fuerda de rango")
    
# Para que el programa anterior continúe preguntando al usuario la edad hasta que diga un valor correcto:

# versión 1 sin crear una clase específica de error

def edad(e):
    if e < 0 or e > 120:
        raise ValueError("Edad fuera de rango")
    elif e >= 18:
        return "Puedes beber"
    else:
        return "No puedes beber"

while True:
    try:
        age = int(input("Escribe tu edad: "))
        print(edad(age))
        break # si el usuario responde con un valor válido el loop deja de correr

    except ValueError as e:
        print(f"Error: {e}")

# Versión 2 de la parte del bucle, manejando control de flujo

while True:
    try:
        age = int(input("Escribe tu edad: "))
    except ValueError:
        print("No has escrito un número")
        continue

    try:
        print(edad(age))
        break
    except ValueError:
        print("Edad fuera de rango")


# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

sentence = input("Di una frase para saber la longitud de cada palabra")

def longitud_palabras(frase):
    """recibe una frase para listar la longitud de las palabras

    Args:
        frase (str): input

    Returns:
        list: lista con longitud de palabras
    """    
    palabras = frase.split()
    return list(map(len, palabras))
    
print(longitud_palabras(sentence))

# solución sin la función map. EL resultado puede devolver la longitud sólo, en forma de lista, o 
# la palabra y la longitud, mediante una tupla

sentence = input("Di una frase para saber la longitud de cada palabra")

def longitud_palabras(frase):
    palabras = frase.split()
    longitud = []

    for word in palabras:
        longitud.append((word, len(word))) # puede ser sólo len(word)
    
    return longitud
   
    
print(longitud_palabras(sentence))

# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()

caracteres = input("escribe un conjunto de caracteres").lower()

def solo_letras_min(caracteres):
    """transforma str en set de letras minusculas ordenadas

    Args:
        caracteres (str)

    Returns:
        set: letras minusculas
    """    
    letras_min = []
    for i in caracteres:
        if i.isalpha():
            letras_min.append(i)
    return sorted(set(letras_min))   

def combinar(lista_min):
    """del set anterior mapea en forma de tupla (x,x.upper)

    Args:
        lista_min (set)

    Returns:
        list: lista de tuplas
    """    
    return list(map(lambda x: (x, x.upper()), lista_min))

resultado = solo_letras_min(caracteres)
resultado_tuplas = combinar(resultado)

print(resultado_tuplas)
        
# pythonic answer

caracteres = input("escribe un conjunto de caracteres").lower()

resultado = [(c, c.upper()) for c in sorted(set(caracteres)) if c.isalpha()]

print(resultado)

# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()

palabras = input("Escribe una lista de palabras separadas por comas: ").lower().split(",")
letra = input("Escribe una letra para ver las palabras que comiencen por esa letra: ").lower()

def palabras_vuelta(palabra):
    """de una lista de palabras retorna palabras que empiezan con cierta letra

    Args:
        palabra (str): input con palabras

    Returns:
        str: dado el input de la letra especifica, devuelve esa palabra
    """    
    return palabra.strip().startswith(letra)

resultado_filter = list(filter(palabras_vuelta, palabras))

if resultado_filter:
    print(f"El resultado de la función filter es: {resultado_filter}")
else:
    print("No hay palabras que comiencen por esa letra.")
    
# 15. Crea una función lambda que sume 3 a cada número de una lista dada.

a = [2, 4, 7, 1, 34, 78, 9, 21]

def suma3(a):
    """suma 3 a cada numero de la lista

    Args:
        a (list): lista con numeros
    Print:
        lista mapeada
    """    
    suma = lambda x: x + 3
    resultado_lista = list(map(suma, a))
    print(f'el resultado de lamba es {resultado_lista}')

suma3(a)

# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()

#with one argument

a = input("Escribe una frase: ")
n = int(input("Escribe un número entero: "))

palabras = a.split()

def palabras_filtradas(palabra):
    """coge una palabra y la devuelve si la longitud es mayor a n

    Args:
        palabra (str)

    Returns:
        str: devuelve la palabra segun la n
    """    
    return len(palabra) > n

resultado_filter = list(filter(palabras_filtradas, palabras))

print(f'El resultado es {resultado_filter}')

# solución con dos argumentos como pide el ejercicio

def palabras_filtradas(texto, n):
    palabras = texto.split()
    return list(filter(lambda palabra: len(palabra) > n, palabras))

a = input("Escribe una frase: ")
n = int(input("Escribe un número entero: "))

resultado = palabras_filtradas(a, n)

print(resultado)

# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). Usa la función reduce()

from functools import reduce

# solución con lista de str

numeros = input("Dime números separados por un espacio:")
lista = numeros.split()
resultado = reduce(lambda x, y: x + y, lista)
print(resultado)

# solución con lista de digitos

numeros = input("Dime números separados por espacios: ")

lista = list(map(int, numeros.split()))

resultado = reduce(lambda x, y: x * 10 + y, lista)

print(resultado)

# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()

dic1 = [
    {'nombre': 'Marina', 'edad': 18, 'calificación': 78},
    {'nombre': 'Ramón', 'edad': 23, 'calificación': 84}, 
    {'nombre': 'Maria', 'edad': 32, 'calificación': 93},
    {'nombre': 'Jose', 'edad': 54, 'calificación': 99},
    {'nombre': 'Lourdes', 'edad': 56, 'calificación': 89},
    {'nombre': 'Toni', 'edad': 29, 'calificación': 44}
    ]

masde90 = filter(lambda student: student['calificación']>90, dic1)

for student in masde90:
    print(student['nombre'])

# 19. Crea una función lambda que filtre los números impares de una lista dada.

numbers = [2, 6, 5, 8, 7, 1, 4, 5, 9, 8, 5, 3, 2, 9, 1, 3]

def odds(x):
    return list(filter(lambda number: number%2 != 0, x))

odd_list = odds(numbers)
print(odd_list)

# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()

int_str = ['silla', 4, 'manzana', 54, 'brocoli', 'espejo', 9, 'leon', 83, 'zapato']


def elements(x):
    """de una lista de int y str transforma a lista de int

    Args:
        x (list): con palabras y numeros

    Returns:
        _list: sólo numeros
    """    
    return list(filter(lambda element: isinstance(element, int), x))

new_list = elements(int_str)
new_list

# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda

cubo = lambda x: x**3
print(cubo(2))

# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .

from functools import reduce
def producto(x, y):
    return x*y

numeros = [3, 6, 4, 7, 9, 2, 1, 5, 6, 7]

reduce_result = reduce(producto, numeros)
print(f'el resultado de la función es: {reduce_result}')

# 23. Concatena una lista de palabras.Usa la función reduce() .

def concatenar(a, b):
    return a.strip() + '' + b.strip()

palabras= ['árbol', 'planta', 'taza', 'cama', 'perchero', 'puerta']

result = reduce(concatenar, palabras)
result 

# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .

def resta(a, b):
    return a- b
num = [9, 6, 8, 4, 1, 2, 6]
result = reduce(resta, num)
result

# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contador(x):
    for i in range(len(x)):
        print(i + 1, x[i])

a = 'caracteres'

contador(a)

# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.

resto = lambda x, y: x % y 

print (resto(4, 2))

# 27. Crea una función que calcule el promedio de una lista de números.

numeros = [3, 5, 7, 2, 9, 7]

def promedio(num):
    return sum(num) / len(num)

media = promedio(numeros)
print("El promedio es:", media)

# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

lista = ['s', 5, 'g', 'y', 5, 's','patata', 56]


def duplicados(x):
    """dada una lista devuelve el primer duplicado

    Args:
        x (list)

    Returns:
        str o int: elemento duplicado
    """    
    lista_2 = []
    for i in x:
        if i in lista_2:
            return i
        lista_2.append(i)  #igualmente va metiendo los elementos en lista 2
    
duplicados(lista)
    
# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.

def enmascarador(x):
    a = str(x)
    return "#" * (len(a) - 4) + a[-4:]
    

variable = ['patata', 'brocoli', 'fresa']

print(enmascarador(variable))
    
# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

def reconocimiento_letras(x, y):
    if sorted(x.lower()) == sorted(y.lower()):
        print("anagramas")
    else:
        print("no anagramas")


palabra1 = input("Dime la primera palabra: ")
palabra2 = input("Dime la segunda palabra: ")

reconocimiento_letras(palabra1, palabra2)
                
# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción

def buscador_nombres():
    """crea una lista de nombres y permite buscar un nombre especifico

    Raises:
        Exception: cuando no se encuentra el nombre
    """    
    nombres = input("Ingresa una lista de nombres separados por comas: ").split(",")
    nueva_lista = []
    for nombre in nombres:
        nueva_lista.append(nombre.strip())
    nombres = nueva_lista
    nombre_buscar = input("¿Qué nombre quieres comprobar? ")
    if nombre_buscar in nombres:
        print("Fue encontrado")
    else:
        raise Exception("No fue encontrado")


buscador_nombres()

# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

empleados = [
    {'Nombre completo': 'Almudena Domínguez Márquez', 'Puesto': 'Analista de datos'},
    {'Nombre completo': 'José María Núñez Martínez', 'Puesto': 'Secretario'},
    {'Nombre completo': 'Isabel García Andreu', 'Puesto': 'Directora'},
    {'Nombre completo': 'Pedro Gil Abadía', 'Puesto': 'Auxiliar encargado de marketing'}
]

def empleado_puesto(y):
    """dado un diccionario con nombre y puesto de empleados, devuelve el puesto dado el nombre

    Args:
        y (dict): diccionario

    Returns:
        str: puesto
    """    
    x = input('¿Nombre completo? ')
    for empleado in y:
        if empleado['Nombre completo'] == x:
            print(empleado['Puesto'])
            return
    else:
        print('La persona no trabaja aquí')  # return es importante para que no itere sobre cada dict, y else tiene que estar a la altura del for


empleado_puesto(empleados)

# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

funcion = lambda x, y: x + y
l1 = [2, 6, 4, 8, 5, 1]
l2 = [6, 9, 5, 3, 6, 7]

list(map(funcion, l1, l2))

# 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.
# 
# Código a seguir:
# 1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
# 2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
# 3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
# 4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
# 5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
# 6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.
# 
# Caso de uso:
# 1. Crear un árbol.
# 2. Hacer crecer el tronco del árbol una unidad.
# 3. Añadir una nueva rama al árbol.
# 4. Hacer crecer todas las ramas del árbol una unidad.
# 5. Añadir dos nuevas ramas al árbol.
# 6. Retirar la rama situada en la posición 2.
# 7. Obtener información sobre el árbol.

class Arbol: # todo método tiene que ir dentro de la clase

    # 1. Inicializar árbol - atributos: tronco y ramas
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    # 2. Crecer tronco (importante no pasar longitud como parámetro, ya está el atributo de tronco)
    def crecer_tronco(self):
        self.tronco += 1

    # 3. Añadir nueva rama
    def nueva_rama(self):
        self.ramas.append(1)  # añades una a la lista cada vez que usas el metodo

    # 4. Crecer todas las ramas
    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas] # no hace falta longitud de rama como parámetro, se podría hacer como diccionario,
        #pero en este caso cada número es una rama que indica la longitud de la rama

    # 5. Quitar rama según posición
    def quitar_rama(self, posicion):
        if posicion < len(self.ramas):  
            self.ramas.pop(posicion) # pop para indice, remove para valor

    # 6. Mostrar información
    def info_arbol(self):
        print(f"Tronco: {self.tronco}")
        print(f"Número de ramas: {len(self.ramas)}")
        print(f"Longitudes ramas: {self.ramas}")


# CASO DE USO

# Crear un árbol.
arbol1 = Arbol()
# Hacer crecer el tronco del árbol una unidad.
arbol1.crecer_tronco()
# Añadir una nueva rama al árbol.
arbol1.nueva_rama()
# Hacer crecer todas las ramas del árbol una unidad.
arbol1.crecer_ramas()
#Añadir dos nuevas ramas al árbol.
arbol1.nueva_rama()
arbol1.nueva_rama()
# Retirar la rama situada en la posición 2.
arbol1.quitar_rama(2)
# Obtener información sobre el árbol.
arbol1.info_arbol()

# 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.
# 
# Código a seguir:
# 1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
# 2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no
# poder hacerse.
# 3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual.
# Lanzará un error en caso de no poder hacerse.
# 4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
# 
# Caso de uso:
# 1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
# 2. Agregar 20 unidades de saldo de "Bob".
# 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
# 4. Retirar 50 unidades de saldo a "Alicia".

class UsuarioBanco:

    def __init__(self, nombre, saldo, cuenta):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta = cuenta

    
    def retirar_dinero(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo = self.saldo - cantidad
        else:
            raise Exception("No se puede hacer")
    
    def transferir_dinero(self, usuario, transferencia):
            if self.cuenta == True and usuario.cuenta == True:
                if transferencia <= self.saldo:
                    usuario.saldo = usuario.saldo + transferencia
                    self.saldo = self.saldo - transferencia
                else:
                    raise Exception("No se puede hacer")
            else:
                raise Exception("No se puede hacer")
        

    def agregar_dinero(self, cantidad):
        self.saldo = cantidad + self.saldo

# caso de uso

# Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
alicia = UsuarioBanco('Alicia', 100, True)
bob = UsuarioBanco('Bob', 50, True)

#Agregar 20 unidades de saldo de "Bob".
bob.agregar_dinero(20)

#Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
bob.transferir_dinero(alicia, 80)

#Retirar 50 unidades de saldo a "Alicia".
alicia.retirar_dinero(50)

print(bob.saldo)
print(alicia.saldo)

# 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras , reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto .
# 
# Código a seguir:
# 1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene
# que devolver un diccionario.
# 2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene
# que devolver el texto con el remplazo de palabras.
# 3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra
# eliminada.
# 4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un
# número de argumentos variable según la opción indicada.
# 
# Caso de uso:
# Comprueba el funcionamiento completo de la función procesar_texto

def contar_palabras(x):
    a = x.split()
    counts = {}
    lowercase_a = [word.lower() for word in a]
    for word in lowercase_a:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return(counts)

        

def reemplazar_palabras(texto, vieja, nueva):
    return texto.replace(vieja, nueva)


def eliminar_palabra(texto, palabra):
    palabras = texto.split()
    resultado = []
    for p in palabras:
        if p != palabra:
            resultado.append(p)
    return " ".join(resultado)



def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, *args)
    elif opcion == "eliminar":
        return eliminar_palabra(texto, *args)
    else:
        raise Exception("Opción no válida")



texto = "no sé qué escribir porque escribir se me hace dificil"

print(procesar_texto(texto, "contar"))

print(procesar_texto(texto, "reemplazar", "escribir", "leer"))

print(procesar_texto(texto, "eliminar", "escribir"))

# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

from datetime import datetime

hora_str = input('Dime la hora')

try:
    hora = datetime.strptime(hora_str,'%H:%M')

    if 5 <= hora.hour < 13:
        print('es de día')
    elif 13 <= hora.hour < 20:
        print('es por la tarde')
    else:
        print('es de noche')

except ValueError:
    print('Escribe la hora en formato HH:MM')

# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. Las reglas de calificación son:
# - 0 - 69 insuficiente
# - 70 - 79 bien
# - 80 - 89 muy bien
# - 90 - 100 excelente

def grade(x):
        if 0 <= x <= 69:
            return ('insuficiente')
        elif 70 <= x <= 79:
            return ('bien')
        elif 80 <= x <= 89:
            return('muy bien')
        elif 90 <= x <= 100:
            return('excelente')
        else:
            raise Exception('Escribe una nota del 0 al 100')

print(grade(89))

# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).

import math

def calculo_area(cadena, datos):
    if cadena == 'rectangulo':
        base, altura = datos
        return base*altura
    elif cadena == 'circulo':
        (radio,) = datos
        return math.pi*radio**2
    elif cadena == 'triangulo':
        base, altura = datos
        return base*altura/2
    else:
        raise Exception('elige entre rectangulo, circulo o triangulo')
print(calculo_area('rectangulo', (18, 12)))
print(calculo_area('circulo', (3,)))
print(calculo_area('triangulo', (12, 15)))

# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:
# 
# - Solicita al usuario que ingrese el precio original de un artículo.
# -  Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
# - Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
# - Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€.
# - Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
# - Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python.

def precio_final():
    """calcula el precio final de un articulo teniendo en cuenta cupones de descuento

    Raises:
        Exception: Si el cupon es negativo
    """    
    precio_original = int(input('Ingresa el precio original del articulo'))
    cupon = input('¿Tienes cupon de descuento? Si/No')
    if cupon == 'Si':
        valor = int(input('Ingresa el valor del cupon'))
        if valor > 0:
            precio_descontado = precio_original - valor
            print(precio_descontado)
        else:
            raise Exception('ingresa un número válido')
    else:
        print(precio_original)

precio_final()
    



