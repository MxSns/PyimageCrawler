```
············································································
: ███████████             █████                                            :
:░░███░░░░░███           ░░███                                             :
: ░███    ░███ █████ ████ ░███  █████████████    ██████    ███████  ██████ :
: ░██████████ ░░███ ░███  ░███ ░░███░░███░░███  ░░░░░███  ███░░███ ███░░███:
: ░███░░░░░░   ░███ ░███  ░███  ░███ ░███ ░███   ███████ ░███ ░███░███████ :
: ░███         ░███ ░███  ░███  ░███ ░███ ░███  ███░░███ ░███ ░███░███░░░  :
: █████        ░░███████  █████ █████░███ █████░░████████░░███████░░██████ :
:░░░░░          ░░░░░███ ░░░░░ ░░░░░ ░░░ ░░░░░  ░░░░░░░░  ░░░░░███ ░░░░░░  :
:               ███ ░███                                  ███ ░███         :
:              ░░██████                                  ░░██████          :
:               ░░░░░░                                    ░░░░░░           :
:   █████████                                      ████                    :
:  ███░░░░░███                                    ░░███                    :
: ███     ░░░  ████████   ██████   █████ ███ █████ ░███   ██████  ████████ :
:░███         ░░███░░███ ░░░░░███ ░░███ ░███░░███  ░███  ███░░███░░███░░███:
:░███          ░███ ░░░   ███████  ░███ ░███ ░███  ░███ ░███████  ░███ ░░░ :
:░░███     ███ ░███      ███░░███  ░░███████████   ░███ ░███░░░   ░███     :
: ░░█████████  █████    ░░████████  ░░████░████    █████░░██████  █████    :
:  ░░░░░░░░░  ░░░░░      ░░░░░░░░    ░░░░ ░░░░    ░░░░░  ░░░░░░  ░░░░░     :
············································································
```

# PyImageCrawler

A simple Python script to extract image URLs from a specified website

## Description

This tool is a web crawler that fetches the HTML of a given domain and uses regular expressions

## Features

- Accepts a domain as a command-line argument.
- Extracts image URLs from the HTML content.
- Error handling for failed requests.

## Installation

- Clone the repository :

https://github.com/MxSns/PyimageCrawler.git

- Install the required dependencies

pip install -r requirements.txt

## Usage

python3 imgCrawler.py -d https://example.com

	-d or --domain: The website to crawl (required)

## Example output

Image URLs:
https://example.com/image1.jpg
https://example.com/image2.png

## Requirements

Python3.x
requests library
