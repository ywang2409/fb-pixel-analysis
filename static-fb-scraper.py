import requests
import csv

def check_facebook_pixel(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get(url, headers=headers, timeout=5, allow_redirects=True)
        if response.status_code == 200:
            html_content = response.text
            if 'www.facebook.com/tr' in html_content or \
                'fbq' in html_content or \
                'fbevents.js' in html_content or \
                'connect.facebook.net' in html_content:
                return "Found"
            else:
                return "Not Found"
        return "Error"
    except requests.exceptions.RequestException:
        return "Error"


def check_facebook_pixel_for_urls(csv_file):
    result = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            url = 'https://' + row[1]
            status = check_facebook_pixel(url)
            result.append([row[1], status])

    with open('data/static_res_1k.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(result)


# Example usage
csv_file = 'data/top_1k.csv'
check_facebook_pixel_for_urls(csv_file)
