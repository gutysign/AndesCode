"""Operaciones para guardar y consultar tickets en SQLite."""

import sqlite3


def registrar_ticket(titulo, descripcion, prioridad):
    """Guarda un ticket. SQLite asigna el ID y el estado 'abierto'."""
    conexion = sqlite3.connect("helpdesk.db")
    try:
        conexion.execute(
            """
            INSERT INTO tickets (titulo, descripcion, prioridad)
            VALUES (?, ?, ?)
            """,
            (titulo, descripcion, prioridad),
        )
        conexion.commit()
    finally:
        conexion.close()


def listar_tickets():
    """Devuelve todos los tickets como una lista de tuplas."""
    conexion = sqlite3.connect("helpdesk.db")
    try:
        cursor = conexion.execute(
            "SELECT id, titulo, descripcion, prioridad, estado "
            "FROM tickets ORDER BY id"
        )
        return cursor.fetchall()
    finally:
        conexion.close()
