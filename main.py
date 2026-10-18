from tickets import crear_ticket

tickets = []

nuevo = crear_ticket(
    "Error de acceso",
    "No puedo iniciar sesión",
    "alta",
    tickets
)

print("Ticket creado:", nuevo)
print("Total de tickets:", len(tickets))