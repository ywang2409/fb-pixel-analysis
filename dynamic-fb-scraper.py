import csv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
import re

def check_facebook_pixel_for_urls(csv_file):
    result = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            url = "https://" + row[1]
            try:
                res = check_facebook_pixel(url)
                result.append([row[1], res])
            except Exception as e:
                # print(f"Error occurred for URL: {url}")
                # print(f"Error message: {str(e)}")
                result.append([row[1], "Error"])

    with open('data/dynamic_res_1k.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(result)

def check_facebook_pixel(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run Chrome in headless mode
    driver = webdriver.Chrome(options=options)

    try:
        # Navigate to the Page
        driver.get(url)

        # set maximum time to load the web page in seconds
        driver.implicitly_wait(10)

        # Get the page source after interactions
        page_source = driver.page_source

        # Parse the page source with Beautiful Soup
        soup = BeautifulSoup(page_source, "html.parser")

        # Extract data using Beautiful Soup methods
        fbq_scripts = soup.find_all("script", type="text/javascript", 
                                    string=re.compile("fbevents.js"))

        # Print data extracted with Beautiful Soup
        if len(fbq_scripts) > 0:
            print(url, "has Facebook Pixel installed")

        if len(fbq_scripts) > 0:
            return "Found"
        else:
            return "Not Found"
    except Exception as e:
        # print(f"Error occurred for URL: {url}")
        # print(f"Error message: {str(e)}")
        return "Error"
    finally:
        driver.quit()


# Example usage
csv_file = 'data/top_1k.csv'
check_facebook_pixel_for_urls(csv_file)