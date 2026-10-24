"""Prueba sencilla de la lección HD-002.2.

Requiere que database.py, operaciones.py y esta prueba estén en la misma carpeta.
Cada ejecución agrega dos tickets nuevos a helpdesk.db.
"""

from database import crear_base_datos
from operaciones import registrar_ticket, listar_tickets

crear_base_datos()

registrar_ticket("Error de acceso", "No puedo iniciar sesión", "alta")
registrar_ticket("Impresora sin conexión", "No puedo imprimir documentos", "media")

print("Tickets guardados:")
for ticket in listar_tickets():
    print(ticket)

print("Total de tickets:", len(listar_tickets()))
