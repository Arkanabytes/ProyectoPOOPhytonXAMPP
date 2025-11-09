from DAO.conexion import Conexion
import bcrypt
from dotenv import load_dotenv
import os

load_dotenv()

# Parámetros de conexión
host = os.getenv("host")
user = os.getenv("user")
passwordS = os.getenv("password")
db = os.getenv("db")

class Usuario:
    def __init__(self, username, password_hash, nombre, apellidos, email, tipo_usuario):
        self.__username = username
        self.__password_hash = password_hash
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__email = email
        self.__tipo_usuario = tipo_usuario

    # Getters
    def get_username(self):
        return self.__username

    def get_password_hash(self):
        return self.__password_hash

    def get_nombre(self):
        return self.__nombre

    def get_apellidos(self):
        return self.__apellidos

    def get_email(self):
        return self.__email

    def get_tipo_usuario(self):
        return self.__tipo_usuario

    @staticmethod
    def login(username, password):
        con = Conexion(host, user, passwordS, db)
        usuario_data = con.obtenerUsuario(username)
        if usuario_data and len(usuario_data) == 1:
            usuario_data = usuario_data[0]
            hashed_password = usuario_data[2].encode('utf-8')
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                return Usuario(
                    username=usuario_data[1],
                    password_hash=usuario_data[2],
                    nombre=usuario_data[3],
                    apellidos=usuario_data[4],
                    email=usuario_data[5],
                    tipo_usuario=usuario_data[6]
                )
        return None

    @staticmethod
    def registrar_usuario(username, password, nombre, apellidos, email, tipo_usuario):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        nuevo_usuario = Usuario(username, hashed_password, nombre, apellidos, email, tipo_usuario)

        con = Conexion(host, user, passwordS, db)
        exito = con.agregarUsuario(
            username=nuevo_usuario.get_username(),
            password_hash=nuevo_usuario.get_password_hash().decode('utf-8'),
            nombre=nuevo_usuario.get_nombre(),
            apellidos=nuevo_usuario.get_apellidos(),
            email=nuevo_usuario.get_email(),
            tipo_usuario=nuevo_usuario.get_tipo_usuario()
        )

        if exito:
            print("¡Usuario registrado exitosamente!")
            return nuevo_usuario
        else:
            print("Error al registrar el usuario.")
            return None