def agregar_elementos_lista(lista_legajo: list, lista_nombre_apellido: list, lista_genero: list, lista_primer_nota: list, lista_segunda_nota: list):
    """ Esta funcion agrega los valores ingresados por el cliente a las listas ya creadas en el sistema
        valida cada dato ingresado mediante el parametro de tipo de validacion correspondiente y en caso
        de que haya un valor mal ingresado, corrobora que ingrese nuevamente dicho dato. En el caso que
        este todo ok, lo guardamos.

    Args:
        lista (list): La lista a la cual agregaremos los datos.
        var (str): El nombre de la lista.
        tipo_validacion (str): El tipo de validacion que necesitamos usar para las listas.
    """

    for i in range(len(lista_legajo)):
        print(f"Ingrese los datos del alumno N°{i + 1}")
        bandera = True

        while bandera:
            legajo = input("Ingrese el numero de legajo: ")

            if not validar_numero(legajo):
                print("Valor no admitido.")
            else:
                bandera2 = True

                for j in range(i):
                    if lista_legajo[j] == legajo:
                        bandera2 = False
                        break

                if not bandera2:
                    print("El numero de legajo ya existe.")
                else:
                    bandera = False
                

        lista_legajo[i] = legajo

        nombre_apellido = input("Ingrese el nombre y apellido: ")
        while not validar_nombre(nombre_apellido):
            print("Valor no admitido.")
            nombre_apellido = input("Ingrese el nombre y apellido: ")

        lista_nombre_apellido[i] = nombre_apellido

        genero = input("Ingrese el genero del alumno: ")
        while not validar_genero(genero):
            print("Valor no admitido.")
            genero = input("Ingrese el genero del alumno: ")

        lista_genero[i] = genero

        primer_n = input("Ingrese la primera nota: ")
        while not validar_numero_1_al_10(primer_n):
            print("Valor no admitido.")
            primer_n = input("Ingrese la primera nota: ")

        lista_primer_nota[i] = primer_n

        segunda_n = input("Ingrese la segunda nota: ")

        while not validar_numero_1_al_10(segunda_n):
            print("Valor no admitido.")
            segunda_n = input("Ingrese la segunda nota: ")

        lista_segunda_nota[i] = segunda_n

def validar_numero (valor: str)-> bool:
    """Esta funcion valida si es un numero entero o no.

    Args:
        valor (str): El dato que validaremos en la funcion.

    Returns:
        bool: Devuelve un valor booleano.
    """
    retorno = True
    if (valor == ""):
        retorno = False

    for i in valor:
        valor1 = ord(i)
    
        if not (valor1 >= 48 and valor1 <= 57):
            retorno = False
            break
    return retorno

def validar_nombre (valor: str)-> bool:
    """Esta funcion valida si el dato ingresado es alfabetico o no.

    Args:
        valor (str): El dato que validaremos a continuacion de tipo str.

    Returns:
        bool: El valor booleano que retornara.
    """
    retorno = True
    if (len(valor)) == 0:
        retorno = False

    else:
        for i in valor:
            valor1 = ord(i)
            if not ((65 <= valor1 <= 90) or (97 <= valor1 <= 122) or valor1 == 32):
                retorno = False
                break

    return retorno

def validar_cadena(lista: list)-> bool:
    """Esta funcion valida la cadena completa en el caso que sean mas de 2 digitos.

    Args:
        lista (list): La lista que recorrera para validar posteriormente.

    Returns:
        bool: Retornara un valor booleano.
    """
    retorno = True
    for i in range(len(lista)):
        hola = validar_numero(lista[i])
        if (hola == False):
            retorno = False
            break
    return retorno

def validar_genero (valor: str)-> bool:
    """Esta funcion validara si el valor ingresado es correspondiente a las letras del genero (F/M/X)

    Args:
        valor (str): El dato ingresado por el cliente a validar.

    Returns:
        bool: Retornera un valor booleano.
    """

    retorno = True
    if (valor == ""):
        retorno = False
    
    for i in valor:
        valor1 = ord(i)
        
        if not (valor1 == 70 or valor1 == 77 or valor1 == 88):
            retorno = False
            break
    return retorno

def validar_numero_1_al_10 (valor: str)-> bool:
    """Esta funcion validara si el dato ingresado es un numero que va entre el 1 al 10, llamando a 
       otra funcion para validar primero si es numerico.

    Args:
        valor (str): El dato ingresado por el cliente del tipo str que validaremos.

    Returns:
        bool: Retornera un valor del tipo booleano.
    """
    retorno = True
    if not (validar_numero(valor)):
        retorno = False

    else:
        variable = int(valor)
        if not (1 <= variable <= 10):
            retorno = False
    return retorno

def validar_opcion(valor: str)-> bool:
    """Esta funcion validara si el dato ingresado esta dentro del parametro seleccionado (1 al 7)

    Args:
        valor (str): El valor ingresado por el cliente que validaremos a continuacion.

    Returns:
        bool: Retornara un valor del tipo booleano.
    """

    retorno = True
    if not (validar_numero(valor)):
        retorno = False
    
    else:
        variable = int(valor)
        if not (1 <= variable <= 7):
            retorno = False
    return retorno

def mostrar_todos_alumnos(legajo: list, nombre_apellido: list, genero: list, primer_nota: list, segunda_nota: list, promedio: list):
    """Esta funcion recorrera y mostrara todos los datos de las listas que haya en su parametro, como legajo, nombre y
       apellido, genero, primer nota, segunda nota y promedios.

    Args:
        legajo (list): Lista de legajos
        nombre_apellido (list): Lista de Nombres y Apellidos
        genero (list): Lista de generos
        primer_nota (list): Lista de las primeras notas
        segunda_nota (list): Lista de las segundas notas
        promedio (list): Lista de los promedios
    """
    print("Legajo\tNombre y Apellido\tGenero\tPrimer Nota\tSegunda Nota\tPromedio")
    for i in range(len(legajo)):
        mostrar_alumno(legajo=legajo[i], nombre_apellido=nombre_apellido[i], genero=genero[i], primer_nota=primer_nota[i], segunda_nota=segunda_nota[i], promedio=promedio[i])

def mostrar_alumno(legajo: list, nombre_apellido: list, genero: list, primer_nota: list, segunda_nota: list, promedio: list):
    """Esta funcion imprimira los datos de un alumno en particular.

    Args:
        legajo (list): Lista de legajos
        nombre_apellido (list): Lista de Nombres y Apellidos
        genero (list): Lista de generos
        primer_nota (list): Lista de las primeras notas
        segunda_nota (list): Lista de las segundas notas
        promedio (list): Lista de los promedios
    """
    print(f"{legajo}\t{nombre_apellido}\t\t{genero}\t{primer_nota}\t\t{segunda_nota}\t\t{promedio:.2f}")

def calcular_promedio(primer_n: list, segunda_n: list, promedio: list):
    """Esta funcion toma como parametros 2 listas de la primer y segunda nota y hace el promedio.

    Args:
        primer_nota (list): Lista de las primeras notas
        segunda_nota (list): Lista de las segundas notas
        promedio (list): Lista de los promedios
    """
    suma = 0
    for i in range(len(primer_n)):
        num1 = float(primer_n[i])
        num2 = float(segunda_n[i])
        suma = round((num1 + num2) / 2, 2)
        promedio[i] = suma

def ordenamiento_burbuja(legajo: list, nombre_apellido: list, genero: list, primer_nota: list, segunda_nota: list, promedio: list, orden: str):
    """Esta funcion ordena dos listas de forma "bubble sort" y se elije si es de forma ASC o DES

    Args:
        listado (list): Lista de tipo int legajos
        listado1 (list): Lista de tipo str nombres
        orden (str): Valor tipo str que sera ASC o DES
    """
    n = len(legajo)

    for i in range(n-1):
        for j in range(i+1, n):
            if (promedio[j] < promedio[i]) and orden == "ASC":
                aux_legajo = legajo[i]
                legajo[i] = legajo[j]
                legajo[j] = aux_legajo

                aux_nombres = nombre_apellido[i]
                nombre_apellido[i] = nombre_apellido[j]
                nombre_apellido[j] = aux_nombres

                aux_genero = genero[i]
                genero[i] = genero[j]
                genero[j] = aux_genero

                aux_primern = primer_nota[i]
                primer_nota[i] = primer_nota[j]
                primer_nota[j] = aux_primern

                aux_segundan = segunda_nota[i]
                segunda_nota[i] = segunda_nota[j]
                segunda_nota[j] = aux_segundan

                aux_promedio = promedio[i]
                promedio[i] = promedio[j]
                promedio[j] = aux_promedio

            elif (promedio[j] > promedio[i]) and orden == "DES":
                aux_legajo = legajo[i]
                legajo[i] = legajo[j]
                legajo[j] = aux_legajo
                
                aux_nombres = nombre_apellido[i]
                nombre_apellido[i] = nombre_apellido[j]
                nombre_apellido[j] = aux_nombres
                
                aux_genero = genero[i]
                genero[i] = genero[j]
                genero[j] = aux_genero
                
                aux_primern = primer_nota[i]
                primer_nota[i] = primer_nota[j]
                primer_nota[j] = aux_primern
                
                aux_segundan = segunda_nota[i]
                segunda_nota[i] = segunda_nota[j]
                segunda_nota[j] = aux_segundan
                
                aux_promedio = promedio[i]
                promedio[i] = promedio[j]
                promedio[j] = aux_promedio

def buscar_mayor_promedio(legajo: list, nombre_apellido: list, genero: list, primer_nota: list, segunda_nota: list, promedio: list):
    """Esta funcion usa los datos de la lista legajos y compara entre para buscar el mayor promedio y luego
       lo imprime mediante la funcion mostrar alumno.

    Args:
        legajo (list): Lista de legajos
        nombre_apellido (list): Lista de Nombres y Apellidos
        genero (list): Lista de generos
        primer_nota (list): Lista de las primeras notas
        segunda_nota (list): Lista de las segundas notas
        promedio (list): Lista de los promedios
    """
    var = promedio[0]

    for i in range(len(promedio)):
        if promedio[i] > var:
            var = promedio[i]
    print("Legajo\tNombre y Apellido\tGenero\tPrimer Nota\tSegunda Nota\tPromedio")
    for j in range(len(legajo)):
        if promedio[j] == var:
            mostrar_alumno(legajo=legajo[j], nombre_apellido=nombre_apellido[j], genero=genero[j], primer_nota=primer_nota[j], segunda_nota=segunda_nota[j], promedio=promedio[j])

def buscar_por_legajo(legajo: list, nombre_apellido: list, genero: list, primer_nota: list, segunda_nota: list, promedio: list):
    """Esta funcion permite al cliente ingresar un valor, que se validara, para luego buscar ese numero
       en la lista de legajos, si la encuentra, lo imprimira junto con los datos del alumno el particular,
       en el caso que no encuentre, se le imprimira un mensaje que no existe ese numero de legajo.

    Args:
        legajo (list): Lista de legajos
        nombre_apellido (list): Lista de Nombres y Apellidos
        genero (list): Lista de generos
        primer_nota (list): Lista de las primeras notas
        segunda_nota (list): Lista de las segundas notas
        promedio (list): Lista de los promedios
    """
    numero = input("Ingrese el numero de legajo a buscar: ")

    while not validar_numero(numero):
        print("El valor que ingreso es incorrecto.")
        numero = input("Ingrese el numero de legajo a buscar: ")

    num_val = int(numero)
    flag = False

    for j in range(len(legajo)):
        if (int(legajo[j])) == num_val:
            print("Legajo\tNombre y Apellido\tGenero\tPrimer Nota\tSegunda Nota\tPromedio")
            mostrar_alumno(legajo=legajo[j], nombre_apellido=nombre_apellido[j], genero=genero[j], primer_nota=primer_nota[j], segunda_nota=segunda_nota[j], promedio=promedio[j])
            flag = True
            break
    if (flag == False):
        print("Valor no encontrado en la base de datos.")