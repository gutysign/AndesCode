titulo = "Problema con Outlook"
descripcion = "No puedo enviar correos"
prioridad = "alta"

ticket = {
    "titulo": titulo,
    "descripcion": descripcion,
    "prioridad": prioridad
}

tickets = []
tickets.append(ticket)


ticket2 = {
    "titulo": "Impresora sin conexión",
    "descripcion": "No puedo imprimir documentos",
    "prioridad": "media"
}

tickets.append(ticket2)

print("Tickets registrados:", tickets)
print("Cantidad de tickets:", len(tickets))