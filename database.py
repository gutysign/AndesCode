import sqlite3


def crear_base_datos():
    # 1. Abrir o crear la base de datos
    conexion = sqlite3.connect("helpdesk.db")

    # 2. Crear la tabla de tickets si no existe
    conexion.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            prioridad TEXT NOT NULL,
            estado TEXT NOT NULL DEFAULT 'abierto'
        );
    """)

    # 3. Guardar los cambios
    conexion.commit()

    # 4. Cerrar la conexión
    conexion.close()


if __name__ == "__main__":
    crear_base_datos()
    print("Base de datos helpdesk.db y tabla tickets listas.")
