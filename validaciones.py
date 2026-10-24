"""Validaciones compartidas para los tickets de HelpDesk."""


def validar_datos_ticket(
    titulo: str,
    descripcion: str,
    prioridad: str,
) -> None:
    """Comprueba que los campos obligatorios y la prioridad sean validos."""

    if not titulo.strip():
        raise ValueError("El título no puede estar vacío")

    if not descripcion.strip():
        raise ValueError("La descripción no puede estar vacía")

    prioridades_permitidas = ["baja", "media", "alta"]
    if prioridad not in prioridades_permitidas:
        raise ValueError("La prioridad debe ser baja, media o alta")
