# pip install requests
import requests
# pip install beautifulsoup4
from bs4 import BeautifulSoup
import re

def ReP(url):
    response = requests.get(url)
    text = response.text

    soup = BeautifulSoup(text, 'html.parser')

    phone_pattern = r"\b(\d{3}[-.]?\d{3}[-.]?\d{4})\b"
    phones = re.findall(phone_pattern, text)

    return phones

def ReE(url):
    response = requests.get(url)
    text = response.text

    soup = BeautifulSoup(text, 'html.parser')

    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    emails = re.findall(email_pattern, text)

    return emails