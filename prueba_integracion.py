"""HD-003.1: pruebas de integración de tickets, validaciones y SQLite.

Se utiliza un directorio temporal para proteger la base helpdesk.db real.
"""

import os
from tempfile import TemporaryDirectory

from tickets import crear_ticket
from operaciones import registrar_ticket, listar_tickets
from database import crear_base_datos


def ejecutar_pruebas():
    # PRUEBA 1: Un ticket válido se agrega a una lista de Python.
    tickets = []
    creado = crear_ticket(
        "Error de acceso",
        "No puedo iniciar sesión",
        "alta",
        tickets,
    )
    assert len(tickets) == 1
    assert creado == tickets[0]
    assert creado["id"] == 1
    print("PRUEBA 1 OK: ticket válido guardado en lista")

    # PRUEBA 2: Un título vacío produce ValueError y NO cambia la lista.
    antes = tickets.copy()
    try:
        crear_ticket("", "Error del sistema", "alta", tickets)
    except ValueError:
        pass  # Este error es el resultado esperado.
    else:
        raise AssertionError("Se aceptó un ticket con título vacío")

    assert tickets == antes
    print("PRUEBA 2 OK: título vacío rechazado; lista sin cambios")

    # PRUEBAS 3 Y 4: SQLite aislado en una carpeta temporal.
    carpeta_original = os.getcwd()
    with TemporaryDirectory() as carpeta_temporal:
        try:
            os.chdir(carpeta_temporal)
            crear_base_datos()

            # PRUEBA 3: Registrar un ticket válido y encontrarlo con SELECT.
            registrar_ticket(
                "Impresora sin conexión",
                "No puedo imprimir documentos",
                "media",
            )
            registros = listar_tickets()
            assert len(registros) == 1
            assert registros[0][1] == "Impresora sin conexión"
            assert registros[0][3] == "media"
            assert registros[0][4] == "abierto"
            print("PRUEBA 3 OK: ticket válido guardado y consultado en SQLite")

            # PRUEBA 4: Prioridad inválida; SQLite no debe cambiar.
            antes_sqlite = listar_tickets()
            try:
                registrar_ticket(
                    "Problema con correo",
                    "No puedo enviar mensajes",
                    "urgente",
                )
            except ValueError:
                pass  # Esperamos el rechazo antes del INSERT.
            else:
                raise AssertionError("Se aceptó la prioridad 'urgente'")

            assert listar_tickets() == antes_sqlite
            print("PRUEBA 4 OK: prioridad inválida rechazada; SQLite sin cambios")
        finally:
            # Es fundamental volver a la carpeta original antes de que
            # TemporaryDirectory elimine la carpeta y su base de prueba.
            os.chdir(carpeta_original)

    print("\nPRUEBAS DE INTEGRACIÓN SUPERADAS: 4 de 4")


if __name__ == "__main__":
    ejecutar_pruebas()
