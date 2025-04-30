## 🔎 TypoFinder: Discover Common Typos in Popular GitHub Repositories

### 📌 Description

**TypoFinder** is a Python-powered tool that helps you identify common English and technical typos (e.g., `adress`, `recieve`, `seperate`) in the files of popular open-source GitHub repositories.

Perfect for:
- Finding small, easy-to-fix issues
- Opening valuable pull requests
- Building a contributor profile

It searches across GitHub using the public code search API and filters results based on star count and file language. It outputs a CSV file with direct links to typo-containing files.

---

## 🚀 Features

- 🔍 Finds typos in Markdown, Python, and other source files
- ⭐ Filters by repository popularity (e.g., stars > 100)
- 📂 Outputs results to a clean CSV file
- 🔐 Secure token handling via `.env`
- 🤖 Ready for automation and PR generation workflows

---

## 📦 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/YOUR_USERNAME/TypoFinder.git
cd TypoFinder
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Create a `.env` file** with your GitHub token:
```
GITHUB_TOKEN=ghp_your_actual_token_here
```

> You can generate a token at [https://github.com/settings/tokens](https://github.com/settings/tokens) (check `public_repo` scope at minimum).

4. **Run the script:**
```bash
python typo_finder.py
```

---

## ⚙️ Configuration

You can modify these values in `typo_finder.py`:

- `TYPOS`: List of words to search for
- `LANGUAGE`: Filter by language (e.g., "Markdown", "Python")
- `STARS`: Minimum stars filter (e.g., `>100`)
- `MAX_RESULTS`: Limit result size for performance

---

## 📄 Output

A file called `typo_results.csv` will be generated with the following columns:

- `typo` – The typo found
- `repo` – GitHub repo (owner/name)
- `file_name` – The file name containing the typo
- `path` – Direct GitHub link to the file
- `stars` – Repository star count (if available)

---

## 🙌 Contribution Opportunities

This tool is ideal if you're looking to:
- Make low-barrier open-source contributions
- Write typo-fix pull requests
- Get noticed in high-star projects

---
