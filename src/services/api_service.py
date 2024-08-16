import http.cookiejar as cookie_jar, json, os, pathlib, requests, tempfile, time, urllib3

##Disable warning about unverified HTTPS requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

API_URL = "https://maxis-service-prod-pdx.amazon.com/"

def get_tickets():
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()

def post_tickets(ticket_data):
    response = requests.post(API_URL, json=ticket_data)
    response.raise_for_status()
    return response.json()
