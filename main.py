from fastapi import FastAPI

api = FastAPI()

all_tickets = [
  {
    "client": "Hotel Example",
    "email": "cliente@hotel.com",
    "description": "No funciona el Wi-Fi en habitaciones",
    "priority": "P1"
  }
]

@api.get("/")
def index():
  return {"message": "Hello, World!"}

@api.get("/health")
def health_check():
  return {"ok": True}


@api.get("/tickets")
def get_tickets():
  return all_tickets


@api.post("/tickets")
def create_ticket(ticket: dict):
  new_ticket = {
    "client": ticket["client"],
    "email": ticket["email"],
    "description": ticket["description"],
    "priority": ticket["priority"]
  }

  all_tickets.append(new_ticket)

  return new_ticket