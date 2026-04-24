import sqlite3


def conectar_bd(nombre_bd="usuarios.db"):
    return sqlite3.connect(nombre_bd)

def crear_tabla(conexion):
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL
        )
    """)
    conexion.commit()

def insertar_usuario(conexion, id_usuario, nombre, edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")

    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO usuarios (id, nombre, edad) VALUES (?, ?, ?)",
        (id_usuario, nombre, edad)
    )
    conexion.commit()

def listar_usuarios(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, edad FROM usuarios")
    return cursor.fetchall()

def buscar_usuario_por_id(conexion, id_usuario):
    cursor = conexion.cursor()
    cursor.execute(
        "SELECT id, nombre, edad FROM usuarios WHERE id = ?",
        (id_usuario,)
    )
    return cursor.fetchone()

def actualizar_edad(conexion, id_usuario, nueva_edad):
    if nueva_edad < 0:
        raise ValueError("La edad no puede ser negativa")

    cursor = conexion.cursor()
    cursor.execute(
        "UPDATE usuarios SET edad = ? WHERE id = ?",
        (nueva_edad, id_usuario)
    )
    conexion.commit()
    return cursor.rowcount

def eliminar_usuario(conexion, id_usuario):
    cursor = conexion.cursor()
    cursor.execute(
        "DELETE FROM usuarios WHERE id = ?",
        (id_usuario,)
    )
    conexion.commit()
    return cursor.rowcount