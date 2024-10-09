import requests
from bs4 import BeautifulSoup
import argparse

def scrape_website(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all anchor tags
        links = soup.find_all('a')

        # Print out the title and href for each link
        for link in links:
            title = link.get_text(strip=True)
            href = link.get('href')
            print(f"Title: {title}, Link: {href}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error while requesting the URL: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(description='Web Scraper CLI')
    parser.add_argument('url', type=str, help='The URL of the website to scrape')
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Scrape the website
    scrape_website(args.url)

if __name__ == "__main__":
    main()
