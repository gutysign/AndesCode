def crear_ticket(
    titulo: str,
    descripcion: str,
    prioridad: str,
    tickets: list[dict]
) -> dict:

    # Validar que el título no esté vacío
    if not titulo.strip():
        raise ValueError("El título no puede estar vacío")

    # Validar que la descripción no esté vacía
    if not descripcion.strip():
        raise ValueError("La descripción no puede estar vacía")

    # Validar la prioridad
    prioridades_permitidas = ["baja", "media", "alta"]

    if prioridad not in prioridades_permitidas:
        raise ValueError("La prioridad debe ser baja, media o alta")

    # Generar automáticamente el siguiente ID
    nuevo_id = max(
        (ticket["id"] for ticket in tickets),
        default=0
    ) + 1

    # Crear el diccionario del ticket
    ticket = {
        "id": nuevo_id,
        "titulo": titulo,
        "descripcion": descripcion,
        "prioridad": prioridad,
        "estado": "abierto"
    }

    # Agregar el ticket a la lista
    tickets.append(ticket)

    # Devolver el ticket creado
    return ticket