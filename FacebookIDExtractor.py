import requests
import re

class FacebookIDExtractor:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers
        self.response_text = None

    def fetch_page(self):
        """Fetch the webpage content."""
        try:
            response = requests.get(self.url, headers=self.headers)
            response.raise_for_status()  # Raise an error for bad status codes
            self.response_text = response.text
            return True
        except requests.RequestException as e:
            print(f"Error fetching page: {e}")
            return False

    def extract_group_id(self):
        """Extract the group ID from the response text."""
        if not self.response_text:
            print("No response text available. Please fetch the page first.")
            return None
        match = re.search(r'"groupID":"(\d+)"', self.response_text)
        return match.group(1) if match else None

    def extract_page_id(self):
        """Extract the page ID from the meta tag in the response text."""
        if not self.response_text:
            print("No response text available. Please fetch the page first.")
            return None
        match = re.search(r'<meta property="al:android:url" content="fb://profile/(\d+)"', self.response_text)
        return match.group(1) if match else None

# Usage
url = "https://www.facebook.com/army2.net"
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    'dpr': "0.8",
    'viewport-width': "1098",
    'sec-ch-ua': "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    'sec-ch-ua-mobile': "?0",
    'sec-ch-ua-platform': "\"Windows\"",
    'sec-ch-ua-platform-version': "\"19.0.0\"",
    'sec-ch-ua-model': "\"\"",
    'sec-ch-ua-full-version-list': "\"Google Chrome\";v=\"137.0.7151.69\", \"Chromium\";v=\"137.0.7151.69\", \"Not/A)Brand\";v=\"24.0.0.0\"",
    'sec-ch-prefers-color-scheme': "dark",
    'upgrade-insecure-requests': "1",
    'sec-fetch-site': "none",
    'sec-fetch-mode': "navigate",
    'sec-fetch-user': "?1",
    'sec-fetch-dest': "document",
    'accept-language': "vi",
    'priority': "u=0, i"
}

# Initialize the extractor
extractor = FacebookIDExtractor(url, headers)

# Fetch the page
if extractor.fetch_page():
    # Extract and print group ID
    group_id = extractor.extract_group_id()
    if group_id:
        print(f"Group ID: {group_id}")
    else:
        print("Group ID not found.")

    # Extract and print page ID
    page_id = extractor.extract_page_id()
    if page_id:
        print(f"Page ID: {page_id}")
    else:
        print("Page ID not found.")