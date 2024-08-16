import tkinter as tk
from tkinter import ttk
from src.controllers.ticket_controller import TicketController

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Ticket Manager")
        self.controller = TicketController()

        # Example layout
        self.label = ttk.Label(root, text="Welcome to Ticket Manager")
        self.label.pack(padx=10, pady=10)

        self.button = ttk.Button(root, text="Load Tickets", command=self.load_tickets)
        self.button.pack(padx=10, pady=10)

    def load_tickets(self):
        tickets = self.controller.load_tickets()
        # Code to update the UI with ticket data
