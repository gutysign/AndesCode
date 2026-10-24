"""Prueba UPDATE y DELETE sin modificar el archivo helpdesk.db del usuario."""

import os
from tempfile import TemporaryDirectory

from database import crear_base_datos
from operaciones import (
    actualizar_estado_ticket,
    eliminar_ticket,
    listar_tickets,
    registrar_ticket,
)


def ejecutar_pruebas():
    carpeta_original = os.getcwd()

    # Trabajamos en una carpeta temporal, con una base de datos nueva.
    with TemporaryDirectory() as carpeta_temporal:
        try:
            os.chdir(carpeta_temporal)
            crear_base_datos()

            registrar_ticket("Error de acceso", "No puedo iniciar sesión", "alta")
            registrar_ticket("Impresora sin conexión", "No puedo imprimir", "media")

            iniciales = listar_tickets()
            assert [fila[0] for fila in iniciales] == [1, 2]
            assert [fila[4] for fila in iniciales] == ["abierto", "abierto"]
            print("Tickets iniciales:", iniciales)

            actualizados = actualizar_estado_ticket(1, "cerrado")
            assert actualizados == 1
            assert listar_tickets()[0][4] == "cerrado"
            assert listar_tickets()[1][4] == "abierto"
            print("Filas actualizadas (ID 1):", actualizados)

            no_encontrados = actualizar_estado_ticket(999, "cerrado")
            assert no_encontrados == 0
            print("Filas actualizadas (ID 999):", no_encontrados)

            try:
                actualizar_estado_ticket(1, "urgente")
            except ValueError:
                print("Estado inválido: rechazado correctamente")
            else:
                raise AssertionError("Se aceptó un estado no permitido")

            eliminados = eliminar_ticket(2)
            assert eliminados == 1
            assert eliminar_ticket(999) == 0
            print("Filas eliminadas (ID 2):", eliminados)

            finales = listar_tickets()
            assert len(finales) == 1
            assert finales[0][0] == 1 and finales[0][4] == "cerrado"
            print("Tickets restantes:", finales)
            print("PRUEBAS SUPERADAS: UPDATE y DELETE funcionan correctamente")
        finally:
            os.chdir(carpeta_original)


if __name__ == "__main__":
    ejecutar_pruebas()
