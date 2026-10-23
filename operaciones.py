"""Operaciones CRUD básicas para la base de datos HelpDesk (SQLite)."""

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


def actualizar_estado_ticket(ticket_id: int, nuevo_estado: str) -> int:
    """Actualiza el estado del ticket indicado; devuelve filas afectadas (0 o 1)."""
    if nuevo_estado not in ("abierto", "cerrado"):
        raise ValueError("El estado debe ser 'abierto' o 'cerrado'")

    conexion = sqlite3.connect("helpdesk.db")
    try:
        cursor = conexion.execute(
            "UPDATE tickets SET estado = ? WHERE id = ?",
            (nuevo_estado, ticket_id),
        )
        conexion.commit()
        return cursor.rowcount
    finally:
        conexion.close()


def eliminar_ticket(ticket_id: int) -> int:
    """Elimina únicamente el ticket indicado; devuelve filas afectadas (0 o 1)."""
    conexion = sqlite3.connect("helpdesk.db")
    try:
        cursor = conexion.execute(
            "DELETE FROM tickets WHERE id = ?",
            (ticket_id,),
        )
        conexion.commit()
        return cursor.rowcount
    finally:
        conexion.close()
