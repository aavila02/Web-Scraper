import requests
from bs4 import BeautifulSoup
import re

# Function to fetch the content of a webpage
def fetch_webpage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None

# Function to detect sensitive information using regular expressions
def detect_sensitive_data(content):
    # Regular expressions to find emails and API keys (simple patterns)
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    api_key_pattern = r'(?i)([\'\"]?api_key[\'\"]?[=:]\s?[\'\"][a-zA-Z0-9]{32,}[\'\"])'

    emails = re.findall(email_pattern, content)
    api_keys = re.findall(api_key_pattern, content)

    return emails, api_keys

# Function to scrape and analyze the webpage
def scrape_website(url):
    # Fetch the webpage content
    content = fetch_webpage(url)
    
    if content:
        # Parse the content using BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')
        
        # Extract text from the webpage for analysis
        text_content = soup.get_text()

        # Detect sensitive information
        emails, api_keys = detect_sensitive_data(text_content)

        # Display the findings
        if emails:
            print(f"Found {len(emails)} email(s):")
            for email in emails:
                print(f"- {email}")
        else:
            print("No emails found.")

        if api_keys:
            print(f"Found {len(api_keys)} potential API key(s):")
            for api_key in api_keys:
                print(f"- {api_key}")
        else:
            print("No API keys found.")
    else:
        print("Failed to retrieve webpage content.")

if __name__ == "__main__":
    # Example website to scrape
    url = input("Enter a URL to scrape for exposed data: ")
    scrape_website(url)

#test with
#https://norvig.com/big.txt