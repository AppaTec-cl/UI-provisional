from os import system
from test import *
import random

class inter:
    def __init__(self):
        self.dao = DAO()

    def menu(self):
        system("cls")
        print("    MENU PRINCIPAL")
        print("    --------------")
        print("    1. Ver Usuario")
        print("    2. Ver Contrato")
        print("    3. Ver Historial de Contrato")
        print("    4. Ver Usuarios")
        print("    5. Ver Contratos")
        print("    6. Ver Historial de Contratos")
        print("    7. Registrar Usuario")
        print("    8. Salir")
        print("")

    def verUsuario(self):
        system("cls")
        id = int(input("Ingrese el id del usuario: "))
        self.dao.verUsuario(id)

    def verContrato(self):
        system("cls")
        id = int(input("Ingrese el id del contrato: "))
        self.dao.verContrato(id)

    def verHistorialContrato(self):
        system("cls")
        id = int(input("Ingrese el id del contrato: "))
        self.dao.verHistorialContrato(id)

    def verUsuarios(self):
        system("cls")
        self.dao.verUsuarios()

    def verContratos(self):
        system("cls")
        self.dao.verContratos()

    def verHistorialContratos(self):
        system("cls")
        self.dao.verHistorialContratos()

    def registrarUsuario(self):
        system("cls")
        rut = input("Ingrese su rut: ")
        nombre = input("Ingrese su nombre: ")
        apellido_p = input("Ingrese su apellido paterno: ")
        apellido_m = input("Ingrese su apellido materno: ")
        email = input("Ingrese su correo electrónico: ")
        password = input("Ingrese su contraseña: ")
        rol = input("Ingrese su rol: ")
        estado = True
        while estado:
            id = random.randint(11111, 99999)
            pasa = self.dao.verificar_id(id)
            if pasa == False:
                estado = False
        print("El", id, "fue:", self.dao.agregarUsuario(id, rut, nombre, apellido_p, apellido_m, email, password, rol))

    def CargarIu(self):
        while True:
            self.menu()
            opcion = input("Ingrese una opcion: ")
            if opcion == "1":
                self.verUsuario()
            elif opcion == "2":
                self.verContrato()
            elif opcion == "3":
                self.verHistorialContrato()
            elif opcion == "4":
                self.verUsuarios()
            elif opcion == "5":
                self.verContratos()
            elif opcion == "6":
                self.verHistorialContratos()
            elif opcion == "7":
                self.registrarUsuario()
            else:
                break
            input("Presione una tecla para continuar...")

ui = inter()
ui.CargarIu()