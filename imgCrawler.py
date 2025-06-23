# Script : imCrawler1.py
# Author : mxn

import requests, re, sys, argparse, shutil
from urllib.parse import urljoin
from rich.console import Console
from rich.progress import track
import time

console = Console()

width = shutil.get_terminal_size().columns

parser = argparse.ArgumentParser(description="Web crawler to parse images from a website.\nRun with python3 imgCrawler.py --domain <url>")
parser.add_argument('-d', '--domain', required=True, help='the domain to crawl in')
args = parser.parse_args()
domain = args.domain

title = "\t\t  ___                        ___                 _         \n" +\
        "\t\t |_ _|_ __  __ _ __ _ ___   / __|_ _ __ ___ __ _| |___ _ _ \n" +\
        "\t\t  | || '  \/ _` / _` / -_) | (__| '_/ _` \ V  V / / -_) '_|\n" +\
        "\t\t |___|_|_|_\__,_\__, \___|  \___|_| \__,_|\_/\_/|_\___|_|  \n" +\
        "\t\t                |___/                                      "

# This function will request a webpage and return the html text
def fetch_page(domain):
    try:
        response = requests.get(domain)

    except requests.exceptions.RequestException as e:
        sys.exit(e)

    return response.text

print("=" * width + "\n")
print(title)
print("\n" + "=" * width)
print(f"\nSearching for images from {domain}")

def get_images(html):
    image_pattern = r'<img[^>]+src=["\'](.*?)["\'][^>]*>'
    images = re.findall(image_pattern, html, re.I)
    images_found = []
    for image in images:
        this_image = image[1]
        images_found.append(image)
    for i in track(range(100), description="Processing..."):
        time.sleep(0.15)
    return images_found

html = fetch_page(domain)
images_found = get_images(html)

if not images_found:
    console.print("No image found", style="red")
    print(f"The html for {domain} has no <img> tag.")
else:    
    console.print("\nImages found:", style="green")
    print("\n".join(images_found))
