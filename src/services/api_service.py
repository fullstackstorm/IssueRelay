import requests, urllib3

from services.cookie_manager import CookieManager

##Disable warning about unverified HTTPS requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

API_URL = "https://maxis-service-prod-pdx.amazon.com/"

class APIService:
    def __init__(self):
        self.cookie_manager = CookieManager()
        self.cookies = self.setup_cookies()

    def setup_cookies(self):
        """Set up cookies for the API handler."""
        self.cookie_manager.ensure_cookie_file_exists()
        cookies = self.cookie_manager.process_cookies()
        return cookies

    def __verify_cookies(self, cookie_file_path):
        """Verify that cookies are valid."""
        # Implement verification logic here
        pass

    def configure_cookies(self, cookie_file_path=None):
        """Configure cookies and set them for the API handler."""
        self.cookie_manager = CookieManager(cookie_file_path)
        self.cookies = self.setup_cookies()
        self.__verify_cookies(self.cookie_manager.cookie_file_path)
        
    def get_tickets():
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()

    def post_tickets(ticket_data):
        response = requests.post(API_URL, json=ticket_data)
        response.raise_for_status()
        return response.json()
