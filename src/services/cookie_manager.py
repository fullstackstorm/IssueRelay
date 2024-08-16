from http.cookiejar import MozillaCookieJar
import os
import pathlib
import tempfile
import requests

class CookieManager:
    def __init__(self, cookie_file_path=None):
        if cookie_file_path is None:
            self.cookie_file_path = os.path.join(pathlib.Path.home(), '.midway', 'cookie')
        else:
            self.cookie_file_path = cookie_file_path

    def ensure_cookie_file_exists(self):
        """Ensure the cookie file exists or generate it if necessary."""
        if not os.path.exists(self.cookie_file_path):
            print('MIDWAY AUTHENTICATION\nInput will not display; press enter when done.')
            os.system('cmd /c "mwinit -s"')  # Run MWInit to generate the cookie file

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
        return cookies

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
