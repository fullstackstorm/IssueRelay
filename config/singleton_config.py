import json
import requests

class SingletonConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        # Load configuration from config.json
        with open('config.json', 'r') as file:
            self.config = json.load(file)
        
        # Initialize a single session
        self.session = requests.Session()
        # Example: Set session headers or other settings from config
        '''self.session.headers.update({
            'Authorization': f"Bearer {self.config.get('apiKey')}"
        })'''
