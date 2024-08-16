import os
import requests
from config.singleton_config import SingletonConfig

API_URL = "https://api.example.com"

class AuthenticationService:
    def __init__(self) -> None:
        self.config = SingletonConfig()
        self.session = self.config.session

    def authenticate(self):
        """Ensure the cookie file exists or generate it if necessary."""
        if not os.path.exists(self.cookie_file_path):
            print('MIDWAY AUTHENTICATION\nInput will not display; press enter when done.')
            os.system('cmd /c "mwinit -s"')  # Run MWInit to generate the cookie file

    def login(self, username, password):
        """Authenticate a user and return session cookies."""
        login_url = f"{API_URL}/login"
        response = self.session.post(login_url, data={'username': username, 'password': password})
        response.raise_for_status()
        # You can manage cookies or tokens here
        return response.json()  # Return user data or authentication token if needed

    def logout(self):
        """Log out the user and clear session."""
        logout_url = f"{API_URL}/logout"
        response = self.session.post(logout_url)
        response.raise_for_status()
        self.session.cookies.clear()  # Clear cookies if using session-based authentication

    def get_auth_token(self):
        """Retrieve the current authentication token if applicable."""
        # This is a placeholder; implement token retrieval as needed
        return self.session.headers.get('Authorization')
