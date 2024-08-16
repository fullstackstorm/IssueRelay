import requests

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
