import re

# List of common phishing keywords (for demonstration purposes)
phishing_keywords = ["login", "verify", "account", "update", "secure", "bank", "password", "signin", "confirm","0"]

# Function to check if a URL contains phishing keywords
def contains_phishing_keywords(url):
    for keyword in phishing_keywords:
        if keyword in url.lower():
            return True
    return False

# Function to check if a URL contains suspicious patterns
def contains_suspicious_patterns(url):
    # Check for presence of IP address in URL
    ip_pattern = re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b')
    if ip_pattern.search(url):
        return True

    # Check for multiple subdomains 
    subdomain_pattern = re.compile(r'(\w+\.){3,}')
    if subdomain_pattern.search(url):
        return True

    return False

# Main function to scan a list of URLs for phishing
def scan_for_phishing(urls):
    for url in urls:
        if contains_phishing_keywords(url):
            print(f"Potential phishing URL detected: {url}")
        elif contains_suspicious_patterns(url):
            print(f"Suspicious URL detected: {url}")
        else:
            print(f"URL seems safe: {url}")

# Example usage
urls_to_scan = [

  "http://google.com"

]


scan_for_phishing(urls_to_scan)