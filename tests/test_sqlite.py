"""Prueba de integración: registrar y consultar un ticket usando SQLite temporal."""

from database import crear_base_datos
from operaciones import registrar_ticket, listar_tickets


def test_registrar_ticket_sqlite(tmp_path, monkeypatch):
    # 1. Trabajar en la carpeta temporal que proporciona pytest.
    monkeypatch.chdir(tmp_path)

    # 2. Crear helpdesk.db y la tabla tickets en esa carpeta.
    crear_base_datos()

    # 3. Registrar un ticket válido utilizando operaciones.py.
    registrar_ticket(
        "Error de acceso",
        "No puedo iniciar sesión",
        "alta",
    )

    # 4. Recuperar los registros guardados en SQLite.
    registros = listar_tickets()

    # 5. Comprobar el archivo, la cantidad y los datos del ticket.
    assert (tmp_path / "helpdesk.db").is_file()
    assert len(registros) == 1
    assert registros[0][0] == 1           # id
    assert registros[0][1] == "Error de acceso"  # titulo
    assert registros[0][2] == "No puedo iniciar sesión"  # descripcion
    assert registros[0][3] == "alta"      # prioridad
    assert registros[0][4] == "abierto"   # estado por defecto
