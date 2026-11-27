"""Pruebas unitarias para las reglas de validación de tickets."""

import pytest

from validaciones import validar_datos_ticket


def test_ticket_con_datos_validos():
    resultado = validar_datos_ticket(
        "Error de acceso",
        "No puedo iniciar sesión",
        "alta",
    )
    assert resultado is None


def test_prioridad_invalida():
    with pytest.raises(ValueError):
        validar_datos_ticket(
            "Error de acceso",
            "No puedo iniciar sesión",
            "urgente",
        )


def test_titulo_vacio():
    with pytest.raises(ValueError):
        validar_datos_ticket(
            "",
            "Error del sistema",
            "alta",
        )


def test_descripcion_vacia():
    with pytest.raises(ValueError):
        validar_datos_ticket(
            "Error del sistema",
            "",
            "media",
        )


def test_titulo_con_espacios():
    with pytest.raises(ValueError):
        validar_datos_ticket(
            "   ",
            "El sistema no responde",
            "baja",
        )
