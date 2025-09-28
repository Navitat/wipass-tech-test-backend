from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
  "http://localhost:3000"
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

all_tickets = [
  {
    "client": "Hotel Example",
    "email": "cliente@hotel.com",
    "description": "No funciona el Wi-Fi en habitaciones",
    "priority": "P1"
  }
]

@app.get("/")
def index():
  return {"message": "Hello, World!"}

@app.get("/health")
def health_check():
  return {"ok": True}


@app.get("/tickets")
def get_tickets():
  return all_tickets


@app.post("/tickets")
def create_ticket(ticket: dict):
  new_ticket = {
    "client": ticket["client"],
    "email": ticket["email"],
    "description": ticket["description"],
    "priority": ticket["priority"]
  }

  all_tickets.append(new_ticket)

  return new_ticket