import unittest
import sqlite3
from app_sqlite import (
    crear_tabla,
    insertar_usuario,
    listar_usuarios,
    buscar_usuario_por_id,
    actualizar_edad,
    eliminar_usuario,
    conectar_bd
)

class TestAppSQLite(unittest.TestCase):

    def setUp(self):
        self.conexion = sqlite3.connect(":memory:")
        crear_tabla(self.conexion)

    def tearDown(self):
        self.conexion.close()

    def test_insertar_y_listar_usuario(self):
        insertar_usuario(self.conexion, 1, "Ana", 20)

        usuarios = listar_usuarios(self.conexion)

        self.assertEqual(len(usuarios), 1)
        self.assertEqual(usuarios[0], (1, "Ana", 20))

    def test_buscar_usuario_existente(self):
        insertar_usuario(self.conexion, 1, "Luis", 22)

        usuario = buscar_usuario_por_id(self.conexion, 1)

        self.assertEqual(usuario, (1, "Luis", 22))

    def test_buscar_usuario_inexistente(self):
        usuario = buscar_usuario_por_id(self.conexion, 99)

        self.assertIsNone(usuario)

    def test_actualizar_edad_usuario(self):
        insertar_usuario(self.conexion, 1, "María", 19)

        filas_afectadas = actualizar_edad(self.conexion, 1, 21)
        usuario = buscar_usuario_por_id(self.conexion, 1)

        self.assertEqual(filas_afectadas, 1)
        self.assertEqual(usuario, (1, "María", 21))

    def test_actualizar_usuario_inexistente(self):
        filas_afectadas = actualizar_edad(self.conexion, 50, 30)

        self.assertEqual(filas_afectadas, 0)

    def test_eliminar_usuario(self):
        insertar_usuario(self.conexion, 1, "Carlos", 25)

        filas_afectadas = eliminar_usuario(self.conexion, 1)
        usuario = buscar_usuario_por_id(self.conexion, 1)

        self.assertEqual(filas_afectadas, 1)
        self.assertIsNone(usuario)

    def test_eliminar_usuario_inexistente(self):
        filas_afectadas = eliminar_usuario(self.conexion, 99)

        self.assertEqual(filas_afectadas, 0)

    def test_insertar_usuario_con_edad_negativa(self):
        with self.assertRaises(ValueError):
            insertar_usuario(self.conexion, 1, "Lucía", -5)

    def test_actualizar_con_edad_negativa(self):
        insertar_usuario(self.conexion, 1, "Pedro", 18)

        with self.assertRaises(ValueError):
            actualizar_edad(self.conexion, 1, -10)

    #
    def test_conectar_bd(self):
        conn = conectar_bd(":memory:")
        self.assertIsNotNone(conn)
        conn.close()

if __name__ == "__main__":
    unittest.main()