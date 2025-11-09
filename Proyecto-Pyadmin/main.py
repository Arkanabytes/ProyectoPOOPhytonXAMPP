import os
import DAO.CRUDcliente
from DTO.tipo import Tipo_Usuario
from DTO.cliente import Cliente
from DTO.usuario import Usuario
from getpass import getpass

def menuprincipal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=======================================")
    print("=========== MENÚ PRINCIPAL ============")
    print("=======================================")
    print("     1.- (C) INGRESAR")
    print("     2.- (R) MOSTRAR")
    print("     3.- (U) MODIFICAR")
    print("     4.- (D) ELIMINAR")
    print("     5.- (E) SALIR")
    print("=======================================")

def menumostrar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=======================================")
    print("=========== MENÚ MOSTRAR ============")
    print("=======================================")
    print("     1.- MOSTRAR TODO")
    print("     2.- MOSTRAR UNO")
    print("     3.- MOSTRAR PARCIAL")
    print("     4.- VOLVER")
    print("=======================================")

def ingresardatos():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=======================================")
    print("======= INGRESAR DATOS CLIENTE ========")
    print("=======================================")
    run = input("INGRESE RUN: ")
    nombre = input("INGRESE NOMBRE: ")
    apellido = input("INGRESE APELLIDO: ")
    direccion = input("INGRESE DIRECCION: ")
    fono = input("INGRESE TELEFONO: ")
    correo = input("INGRESE CORREO: ")
    datos = DAO.CRUDCliente.mostrartipos()
    print("---------------------------------------")
    for dato in datos:
        print(" CODIGO : {} - {}".format(dato[0], dato[1]))
    print("---------------------------------------")
    tipo = int(input("Ingrese el codigo del Tipo de Cliente: "))
    monto = int(input("Ingrese MONTO CREDITO: "))
    c = Cliente(run, nombre, apellido, direccion, fono, correo, tipo, monto, deuda=0)
    DAO.CRUDCliente.agregar(c)

def mostrar():
    while True:
        menumostrar()
        try:
            op2 = int(input(" INGRESE OPCIÓN: "))
            if op2 == 1:
                mostrartodo()
                input("\n\nPRESIONE ENTER PARA CONTINUAR")
            elif op2 == 2:
                mostraruno()
            elif op2 == 3:
                mostrarparcial()
            elif op2 == 4:
                break
            else:
                print("Opción Fuera de Rango")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def mostrartodo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=======================================")
    print("====== MUESTRA DE TODOS LOS CLIENTES ======")
    print("=======================================")
    datos = DAO.CRUDCliente.mostrartodos()
    if datos:
        for dato in datos:
            print(" ID: {} - RUN: {} - NOMBRE: {} - APELLIDO: {} - TIPO: {}".format(
                dato[0], dato[1], dato[2], dato[3], dato[10]))
    print("=======================================")

def mostraruno():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=======================================")
    print("====== MUESTRA DE DATOS PARTICULAR ======")
    print("=======================================")
    try:
        op = int(input("\n Ingrese valor del ID del Cliente que desea Mostrar los Datos: "))
        datos = DAO.CRUDCliente.consultaparticular(op)
        if datos:
            print("\n=======================================")
            print("======= MUESTRA DE DATOS DEL CLIENTE =======")
            print("=======================================")
            print(f" ID        : {datos[0]}")
            print(f" RUN       : {datos[1]}")
            print(f" NOMBRE    : {datos[2]}")
            print(f" APELLIDO  : {datos[3]}")
            print(f" DIRECCION : {datos[4]}")
            print(f" FONO      : {datos[6]}")
            print(f" CORREO    : {datos[7]}")
            print(f" TIPO      : {datos[10]}")
            print(f" MONTO CREDITO: {datos[8]}")
            print(f" DEUDA     : {datos[9]}")
            print("=======================================")
        else:
            print("No se encontró un cliente con ese ID.")
        input("\n\n\n PRESIONE ENTER PARA CONTINUAR")
    except ValueError:
        print("ID inválido. Debe ser un número.")
        input("\n\nPRESIONE ENTER PARA CONTINUAR")

def mostrarparcial():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=======================================")
    print("====== MUESTRA PARCIALMENTE LOS CLIENTES ======")
    print("=======================================")
    try:
        cant = int(input("\nIngrese la Cantidad de Clientes a Mostrar: "))
        datos = DAO.CRUDCliente.consultaparcial(cant)
        if datos:
            for dato in datos:
                print(" ID: {} - RUN: {} - NOMBRE: {} - APELLIDO: {} - TIPO: {}".format(
                    dato[0], dato[1], dato[2], dato[3], dato[10]))
        print("=======================================")
        input("\n\n PRESIONE ENTER PARA CONTINUAR")
    except ValueError:
        print("Cantidad inválida. Debe ser un número.")
        input("\n\nPRESIONE ENTER PARA CONTINUAR")


def modificardatos():
    os.system('cls' if os.name == 'nt' else 'clear')
    listanuevos = []
    print("=======================================")
    print("======== MODULO MODIFICAR CLIENTE ========")
    print("=======================================")
    mostrartodo()
    try:
        mod = int(input("\n Ingrese valor de ID del cliente que desea Modificar: "))
        datos = DAO.CRUDCliente.consultaparticular(mod)
        if not datos:
            input("ID no encontrado. Presione ENTER para continuar.")
            return

        print(f" ID    : {datos[0]}")
        listanuevos.append(datos[0])
        print(f" RUN   : {datos[1]}")
        listanuevos.append(datos[1])

        # Se mantiene la lógica original de la PPT para modificar
        opm = input(f"DESEA MODIFICAR EL NOMBRE: {datos[2]} - [SI/NO] ")
        if opm.lower() == "si":
            nombrenuevo = input("INGRESE NOMBRE: ")
            listanuevos.append(nombrenuevo)
        else:
            listanuevos.append(datos[2])
        # ... y así para el resto de los campos ...
        listanuevos.append(datos[3]) # apellido
        listanuevos.append(datos[4]) # direccion
        listanuevos.append(datos[6]) # fono
        listanuevos.append(datos[7]) # correo
        listanuevos.append(datos[8]) # monto
        listanuevos.append(datos[9]) # deuda
        listanuevos.append(datos[10]) # tipo

        DAO.CRUDCliente.editar(listanuevos)
    except ValueError:
        print("ID inválido.")
        input()


def eliminardatos():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=======================================")
    print("======== MODULO ELIMINAR CLIENTE ========")
    print("=======================================")
    mostrartodo()
    try:
        elim = int(input("Ingrese valor de ID del Cliente que desea Eliminar: "))
        DAO.CRUDCliente.eliminar(elim)
    except ValueError:
        print("ID inválido.")
        input()


def menuUsuarios():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=======================================")
    print("=========== MENÚ USUARIOS =============")
    print("=======================================")
    print("     1.- INICIAR SESIÓN")
    print("     2.- REGISTRAR USUARIO")
    print("     3.- Salir")
    print("=======================================")


def ingresoUsuarios():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=======================================")
    print("========== INGRESO DE USUARIO =========")
    print("=======================================")
    username = input("INGRESE NOMBRE DE USUARIO: ")
    while True:
        clave1 = getpass("INGRESE PASSWORD         : ")
        clave2 = getpass("REPITA PASSWORD          : ")
        if clave1 == clave2:
            break
        else:
            print("Las contraseñas no coinciden. Intente de nuevo.")
    nombre = input("INGRESE NOMBRE           : ")
    apellidos = input("INGRESE APELLIDOS        : ")
    correo = input("INGRESE CORREO           : ")
    print("---------------------------------------")
    print("     1 para Administrador")
    print("     2 para Vendedor")
    print("---------------------------------------")
    try:
        tipo_num = int(input("     Ingrese Nº             : "))
        tipo_usuario = "Administrador" if tipo_num == 1 else "Vendedor"
        Usuario.registrar_usuario(username, clave1, nombre, apellidos, correo, tipo_usuario)
    except ValueError:
        print("Opción de tipo de usuario inválida.")
    print("=======================================")


# --- BUCLE PRINCIPAL ---
while True:
    menuUsuarios()
    try:
        opUsu = int(input(" INGRESE OPCIÓN: "))
        if opUsu == 1:
            user_input = input("Ingrese nombre de usuario: ")
            clave_input = getpass("Ingrese password: ")
            usuario_logueado = Usuario.login(user_input, clave_input)

            if not usuario_logueado:
                input("...Usuario o contraseña incorrectos. Presione ENTER.")
            else:
                print(f"Bienvenido {usuario_logueado.get_nombre().upper()} {usuario_logueado.get_apellidos().upper()}.")
                input("...Presiona ENTER para ingresar al Menú Principal.")

                while True:
                    menuprincipal()
                    try:
                        op = int(input(" INGRESE OPCIÓN: "))
                        if op == 1:
                            ingresardatos()
                        elif op == 2:
                            mostrar()
                        elif op == 3:
                            modificardatos()
                        elif op == 4:
                            eliminardatos()
                        elif op == 5:
                            op2 = input("¿DESEA SALIR DEL MENÚ PRINCIPAL? [SI/NO]: ")
                            if op2.lower() == "si":
                                break
                        else:
                            print("Opción Fuera de Rango")
                    except ValueError:
                        print("Opción inválida.")
        elif opUsu == 2:
            ingresoUsuarios()
            input("...Presione ENTER para continuar")
        elif opUsu == 3:
            opSalir = input("¿DESEA SALIR DEL SISTEMA? [SI/NO]: ")
            if opSalir.lower() == "si":
                exit()
        else:
            print("Opción fuera de rango.")

    except ValueError:
        print("Por favor, ingrese un número como opción.")
        input()