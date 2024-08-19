# src/controllers/controller.py
from src.services.service import process_data

def handle_button_click():
    # Example logic for button click
    result = process_data()
    print(f"Button clicked, result: {result}")
