import requests

API_URL = "https://api.example.com/tickets"

def get_tickets():
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()

def upload_tickets(ticket_data):
    response = requests.post(API_URL, json=ticket_data)
    response.raise_for_status()
    return response.json()
