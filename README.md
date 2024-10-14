# Web Scraping for Data Security

A Python-based web scraper that gathers publicly available information about websites and detects potentially exposed sensitive data, such as emails or API keys. This project showcases how automation can be used to identify publicly exposed sensitive information, which could pose a security risk.

## Features
- Scrapes and parses website content using `requests` and `BeautifulSoup`.
- Detects sensitive data patterns like:
  - Emails
  - API Keys
- Generates reports with the detected information.
- Customizable regex patterns for different data types (e.g., phone numbers, credit cards).

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/web-scraping-data-security.git
    cd web-scraping-data-security
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the scraper:
    ```bash
    python scraper.py
    ```

## Future Enhancements
- Integrate with **Have I Been Pwned** API to check if scraped emails are part of known breaches.
- Add multi-page scraping for large websites.
