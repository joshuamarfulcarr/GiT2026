# ============================================================
#  Wikipedia Data Scraper — Beginner Starter Project
#  Tools used: requests, BeautifulSoup
#
#  SETUP (run once in your terminal):
#    pip install requests beautifulsoup4
# ============================================================

import requests
from bs4 import BeautifulSoup
import csv
import json
import os


# ------------------------------------------------------------
# PART 1: Fetch a Wikipedia page
# ------------------------------------------------------------

def get_page(url):
    """
    Downloads a Wikipedia page and returns a BeautifulSoup object
    (a parsed, searchable version of the HTML).
    """
    # Add a User-Agent so Wikipedia knows we're a regular browser-like request
    headers = {"User-Agent": "Mozilla/5.0 (WikiScraper/1.0)"}

    response = requests.get(url, headers=headers)

    # Check if the request succeeded (status 200 = OK)
    if response.status_code != 200:
        print(f"Error: Could not fetch page (status {response.status_code})")
        return None

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


# ------------------------------------------------------------
# PART 2: Extract the article title and intro paragraph
# ------------------------------------------------------------

def get_title_and_intro(soup):
    """
    Extracts the page title and first paragraph of the article.
    """
    # The main title is inside an <h1> tag with id="firstHeading"
    title = soup.find("h1", id="firstHeading").text

    # The article body is inside a <div> with class "mw-parser-output"
    body = soup.find("div", class_="mw-parser-output")

    # Get the first non-empty <p> tag (skip empty ones Wikipedia sometimes adds)
    intro = ""
    for p in body.find_all("p"):
        if p.text.strip():          # .strip() removes whitespace
            intro = p.text.strip()
            break

    return title, intro


# ------------------------------------------------------------
# PART 3: Extract all section headings
# ------------------------------------------------------------

def get_headings(soup):
    """
    Returns a list of all section headings (h2 and h3) on the page.
    """
    headings = []

    # Wikipedia uses <h2> for main sections, <h3> for sub-sections
    for tag in soup.find_all(["h2", "h3"]):
        text = tag.text.replace("[edit]", "").strip()  # Remove the "[edit]" buttons
        if text not in ("Contents", "See also", "References",
                        "External links", "Notes", "Bibliography"):
            headings.append({"level": tag.name, "heading": text})

    return headings


# ------------------------------------------------------------
# PART 4: Extract a table (e.g. an infobox or data table)
# ------------------------------------------------------------

def get_first_table(soup):
    """
    Finds the first standard Wikipedia table and returns its
    data as a list of rows (each row is a list of cell values).
    """
    table = soup.find("table", class_="wikitable")

    if not table:
        print("No wikitable found on this page.")
        return []

    rows = []
    for tr in table.find_all("tr"):
        cells = [td.text.strip() for td in tr.find_all(["th", "td"])]
        if cells:
            rows.append(cells)

    return rows


# ------------------------------------------------------------
# PART 5: Save results to CSV and JSON
# ------------------------------------------------------------

def save_to_csv(rows, filename="table_data.csv"):
    """
    Saves a list of rows to a CSV file.
    """
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print(f"Table saved to {filename}")


def save_to_json(data, filename="page_data.json"):
    """
    Saves any Python dictionary or list to a JSON file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Data saved to {filename}")


# ------------------------------------------------------------
# MAIN — Put it all together
# ------------------------------------------------------------

def scrape_wikipedia(url):
    print(f"\nScraping: {url}\n")

    # Step 1: Fetch the page
    soup = get_page(url)
    if not soup:
        return

    # Step 2: Get title and intro
    title, intro = get_title_and_intro(soup)
    print(f"Title:  {title}")
    print(f"Intro:  {intro[:200]}...")   # Print first 200 characters

    # Step 3: Get headings
    headings = get_headings(soup)
    print(f"\nFound {len(headings)} section headings:")
    for h in headings:
        indent = "    " if h["level"] == "h3" else ""
        print(f"  {indent}[{h['level']}] {h['heading']}")

    # Step 4: Get first table
    print("\nLooking for a table...")
    table_rows = get_first_table(soup)
    if table_rows:
        print(f"Found a table with {len(table_rows)} rows. First 3 rows:")
        for row in table_rows[:3]:
            print(" |", " | ".join(row[:4]))   # Print first 4 columns

    # Step 5: Save everything
    result = {
        "url": url,
        "title": title,
        "intro": intro,
        "headings": headings,
    }
    save_to_json(result, "page_data.json")

    if table_rows:
        save_to_csv(table_rows, "table_data.csv")


# ------------------------------------------------------------
# CHANGE THIS URL to any Wikipedia article you want to scrape!
# ------------------------------------------------------------

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    scrape_wikipedia(url)

    output_dir = r"C:\Users\JCs\Desktop"
    for filename in ["page_data.json", "table_data.csv"]:
        if os.path.exists(filename):
            os.replace(filename, os.path.join(output_dir, filename))
            print(f"Moved {filename} to {output_dir}")
    