import os
import requests
import csv
import time
from dotenv import load_dotenv
load_dotenv()

# 🔑 Replace with your GitHub Personal Access Token to avoid rate limits
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

if not GITHUB_TOKEN:
    raise ValueError("❌ GitHub token not found in .env file!")

# 🔍 Typo terms to search
TYPOS = ["adress", "recieve", "seperate", "enviroment", "dependancy", "intial", "occured", "retun", "funtion"]

# 📂 Target languages or file types
LANGUAGE = "Markdown"  # or "Python", or None
STARS = ">100"  # minimum stars to filter
MAX_RESULTS = 50  # GitHub limits to 1000 per search query

HEADERS = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"token {GITHUB_TOKEN}"
}

def search_typo(typo, language=None):
    print(f"🔍 Searching for typo: {typo}")
    results = []
    query = f'"{typo}" stars:{STARS}'
    if language:
        query += f" language:{language}"

    page = 1
    while True:
        url = f"https://api.github.com/search/code?q={query}&per_page=50&page={page}"
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            print(f"⚠️ Error: {response.status_code}, {response.json()}")
            break

        data = response.json()
        for item in data.get("items", []):
            results.append({
                "typo": typo,
                "repo": item["repository"]["full_name"],
                "file_name": item["name"],
                "path": item["html_url"],
                "stars": item["repository"].get("stargazers_count", "N/A")
            })

        if "next" not in response.links or len(results) >= MAX_RESULTS:
            break
        page += 1
        time.sleep(1)  # be polite with rate limits

    return results

def write_csv(all_results, filename="typo_results.csv"):
    keys = ["typo", "repo", "file_name", "path", "stars"]

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(all_results)
    print(f"✅ Results written to {filename}")

def main():
    all_results = []
    for typo in TYPOS:
        results = search_typo(typo)
        all_results.extend(results)

    write_csv(all_results)

if __name__ == "__main__":
    main()
