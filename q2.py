import requests
from bs4 import BeautifulSoup

url = "https://example.com/tesla-revenue"  # Replace with the actual URL
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Example: Extracting revenue table
revenue_table = soup.find("table")
print(revenue_table)
