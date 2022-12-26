import requests
from bs4 import BeautifulSoup


# Fetch the HTML content of the website
response = requests.get('http://127.0.0.1:5000/display')

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the text from the HTML content
text = soup.get_text()

# Print the text
print(text)