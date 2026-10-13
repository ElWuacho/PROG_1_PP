from funciones1 import *

def programa():

    numero = 30
    legajo = [0] * numero
    nombres = [0] * numero
    genero = [0] * numero
    primer_parcial = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    segundo_parcial = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    promedios = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    print("Bievenido al programa de carga de datos la institucion educativa!!")

    bandera = False
    corriendo = True

    while corriendo:

        print("""Elija la opcion que desea hacer: 
             1- Realizar la carga de datos de los alumnos (Legajos, Nombres y Apellidos, Genero, Primera Nota y Segunda nota).
             2- Mostrar todos los datos de los alumnos.
             3- Calcular el promedio de todos los alumnos.
             4- Mostrar todos los datos de los alumnos y ordernarlos por promedio de manera descendiente.
             5- Mostrar el/los estudiante/s con mayor promedio.
             6- Buscar y mostrar todos los datos de un estudiante por legajo.
             7- Salir del programa.
        """)

        hi = input("Opcion a elegir (1-7): ")
        while hi == "" or not validar_opcion(hi):
            hi = input("Error en el valor ingresado, ingrese la opcion entre 1 a 7: ")

        opcion = int(hi)
        if opcion in [2,3,4,5,6] and not bandera:
            print("Error, recuerde que primero tiene que cargar datos para elegir las demas opciones.")

        else:
            match opcion:

                case 1:
                    agregar_elementos_lista(lista=legajo, var="legajo", tipo_validacion="numero")
                    validar_cadena(lista=legajo)
                    agregar_elementos_lista(lista=nombres, var="nombre y apellido", tipo_validacion="nombre")
                    agregar_elementos_lista(lista=genero, var="genero(F/M/X)", tipo_validacion="genero")
                    agregar_elementos_lista(lista=primer_parcial, var="primera nota del parcial", tipo_validacion="nota")
                    agregar_elementos_lista(lista=segundo_parcial, var="segunda nota del parcial", tipo_validacion="nota")
                    bandera = True
                case 2:
                    mostrar_todos_alumnos(legajo=legajo, nombre_apellido=nombres, genero=genero, primer_nota=primer_parcial, segunda_nota=segundo_parcial, promedio=promedios)
                case 3:
                    calcular_promedio(primer_n=primer_parcial, segunda_n=segundo_parcial, promedio=promedios)
                case 4:
                    ordenamiento_burbuja(legajo=legajo, nombre_apellido=nombres, genero=genero, primer_nota=primer_parcial, segunda_nota=segundo_parcial, promedio=promedios, orden="DES")
                    mostrar_todos_alumnos(legajo=legajo, nombre_apellido=nombres, genero=genero, primer_nota=primer_parcial, segunda_nota=segundo_parcial, promedio=promedios)
                case 5:
                    buscar_mayor_promedio(legajo=legajo, nombre_apellido=nombres, genero=genero, primer_nota=primer_parcial, segunda_nota=segundo_parcial, promedio=promedios)
                case 6:
                    buscar_por_legajo(legajo=legajo, nombre_apellido=nombres, genero=genero, primer_nota=primer_parcial, segunda_nota=segundo_parcial, promedio=promedios)
                case 7:
                    print("Saliendo del programa, gracias por pasarse!!!")
                    corriendo = False

