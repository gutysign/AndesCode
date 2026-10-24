"""Creación de tickets en memoria para el proyecto HelpDesk."""

from validaciones import validar_datos_ticket


def crear_ticket(
    titulo: str,
    descripcion: str,
    prioridad: str,
    tickets: list[dict],
) -> dict:
    # 1. Validar los datos antes de crear el ticket.
    validar_datos_ticket(titulo, descripcion, prioridad)

    # 2. Generar el siguiente ID a partir del mayor ID existente.
    nuevo_id = max((ticket["id"] for ticket in tickets), default=0) + 1

    # 3. Construir el ticket.
    ticket = {
        "id": nuevo_id,
        "titulo": titulo,
        "descripcion": descripcion,
        "prioridad": prioridad,
        "estado": "abierto",
    }

    # 4. Guardar el ticket en la lista y devolverlo.
    tickets.append(ticket)
    return ticket
