from http.cookiejar import MozillaCookieJar
import os
import pathlib
import tempfile
import requests
from config.singleton_config import SingletonConfig

class CookieManager:
    def __init__(self, cookie_file_path=None):
        self.config = SingletonConfig()
        self.session = self.config.session
        self.__verify_cookies(cookie_file_path)
        if cookie_file_path is None:
            self.cookie_file_path = os.path.join(pathlib.Path.home(), '.midway', 'cookie')
        else:
            self.cookie_file_path = cookie_file_path

    def create_cookie_jar(self):
        """Process the cookie file and return a MozillaCookieJar object."""
        with tempfile.NamedTemporaryFile('w', delete=False) as temp_file:
            with open(self.cookie_file_path, 'r') as source_file:
                for line in source_file:
                    # Remove the '#HttpOnly_' prefix if present
                    temp_file.write(line[10:] if line.startswith('#HttpOnly_') else line)
                    temp_file.flush()

            cookies = MozillaCookieJar(temp_file.name)
            cookies.load()

        os.remove(temp_file.name)
        self.session.cookies = cookies
        self.__verify_cookies(self.cookie_file_path)
    
    def __verify_cookies(self, cookie_file_path=None):
        try:
            response = self.session.get('https://midway-auth.amazon.com/api/session-status')
            status = response.json()
            if not status['authenticated']: raise Exception
        except Exception:
            if cookie_file_path: os.remove(cookie_file_path)
            self.create_cookie_jar()

    def get_cookies(session: requests.Session) -> requests.cookies.RequestsCookieJar:
        """Retrieve cookies from the session."""
        return session.cookies

    def set_cookies(session: requests.Session, cookies: dict):
        """Set cookies in the session."""
        for key, value in cookies.items():
            session.cookies.set(key, value)

    def clear_cookies(session: requests.Session):
        """Clear cookies from the session."""
        session.cookies.clear()
