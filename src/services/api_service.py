import requests, urllib3

from services.auth_service import AuthenticationService
from services.cookie_manager import CookieManager
from config.singleton_config import SingletonConfig

##Disable warning about unverified HTTPS requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

API_URL = "https://maxis-service-prod-pdx.amazon.com/"

class APIService:
    def __init__(self):
        self.config = SingletonConfig()
        self.session = self.config.session
        self.authenticator = AuthenticationService()
        self.authenticator.authenticate()
        self.cookie_manager = CookieManager()
        self.cookies = self.setup_cookies()
        self._sim_endpoint = self._page_token = ''

    @staticmethod
    def prepare_endpoint(process_name, process_folders):
        process_id = (
            process_folders[process_name] if process_name != ''
            else '+OR+'.join(value for value in process_folders.values())
        )
        sim_status = 'Resolved'
        date_range = '[NOW-28DAYS TO NOW]'
        sort_order = 'lastUpdatedDate+desc'
        _sim_endpoint = f'issues?q=containingFolder:({process_id})+status:({sim_status})+createDate:({date_range})&sort={sort_order}'

    # src/services/service.py
    def process_data():
        # Example processing logic
        return "Processed Data"


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
