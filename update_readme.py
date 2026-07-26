#!/usr/bin/env python3
import os
from collections import defaultdict

# ── Settings ───────────────────────────────────────────────────────────────────

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))

# Platform folder name → display name + URL
PLATFORMS = {
    "leetcode":    ("LeetCode",    "https://leetcode.com"),
    "algoleague":  ("AlgoLeague",  "https://algoleague.com"),
    "neetcode":    ("NeetCode",    "https://neetcode.io"),
    "hackerrank":  ("HackerRank",  "https://hackerrank.com"),
    "competitive": ("Competitive", ""),
}

# Only track these three languages, in this column order
LANGUAGES = ["C", "C++", "Python"]

EXT_MAP = {
    ".c":   "C",
    ".cpp": "C++",
    ".py":  "Python",
}

IGNORE_DIRS  = {".git", "__pycache__", ".idea", ".vscode", "node_modules"}
IGNORE_FILES = {"generate_readme.py", "README.md", ".gitignore"}

# ── Scanning ───────────────────────────────────────────────────────────────────

def scan():
    """
    Returns:
        platform_stats : { platform_key: { lang_name: count } }
        lang_totals    : { lang_name: count }
    """
    platform_stats = defaultdict(lambda: defaultdict(int))
    lang_totals    = defaultdict(int)

    for entry in sorted(os.listdir(REPO_ROOT)):
        if entry in IGNORE_DIRS or entry in IGNORE_FILES:
            continue
        platform_dir = os.path.join(REPO_ROOT, entry)
        if not os.path.isdir(platform_dir):
            continue

        platform_key = entry.lower()

        for root, dirs, files in os.walk(platform_dir):
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
            for fname in files:
                ext = os.path.splitext(fname)[1].lower()
                if ext not in EXT_MAP:
                    continue
                lang = EXT_MAP[ext]
                platform_stats[platform_key][lang] += 1
                lang_totals[lang] += 1

    return platform_stats, lang_totals

# ── Markdown generation ────────────────────────────────────────────────────────

def build_platform_table(platform_stats, lang_totals) -> str:
    header = "| Platform | " + " | ".join(LANGUAGES) + " | Total |"
    sep    = "|----------|" + "|".join([":-------:"] * len(LANGUAGES)) + "|:-----:|"

    rows = []
    for pkey, (name, url) in PLATFORMS.items():
        link  = f"[{name}]({url})" if url else name
        cells = [str(platform_stats[pkey].get(lang, 0)) for lang in LANGUAGES]
        total = sum(platform_stats[pkey].values())
        rows.append(f"| {link} | " + " | ".join(cells) + f" | **{total}** |")

    totals = [str(lang_totals.get(lang, 0)) for lang in LANGUAGES]
    grand  = sum(lang_totals.values())
    rows.append(f"| **Total** | " + " | ".join(totals) + f" | **{grand}** |")

    return "\n".join([header, sep] + rows)


def build_lang_breakdown(lang_totals) -> str:
    total = sum(lang_totals.values())
    if total == 0:
        return "_No solutions added yet._"
    lines = []
    for lang in sorted(LANGUAGES, key=lambda l: -lang_totals.get(l, 0)):
        count = lang_totals.get(lang, 0)
        pct   = count / total * 100 if total else 0
        filled = int(pct / 5)
        bar   = "█" * filled + "░" * (20 - filled)
        lines.append(f"| **{lang}** | `{bar}` | {count} ({pct:.0f}%) |")
    return "| Language | Distribution | Count |\n|----------|-------------|-------|\n" + "\n".join(lines)


def build_readme(platform_stats, lang_totals) -> str:
    total          = sum(lang_totals.values())
    platform_table = build_platform_table(platform_stats, lang_totals)
    lang_breakdown = build_lang_breakdown(lang_totals)

    return f"""# Algorithms

> A collection of algorithm and data structure problems I've solved across various platforms.

![Total Solutions](https://img.shields.io/badge/Total%20Solutions-{total}-blue?style=flat-square)

---

## Solutions by Platform

{platform_table}

---

## Language Breakdown

{lang_breakdown}

---
"""

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    platform_stats, lang_totals = scan()
    readme_content = build_readme(platform_stats, lang_totals)

    out_path = os.path.join(REPO_ROOT, "README.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(readme_content)

    total = sum(lang_totals.values())
    print(f"README.md updated — {total} solutions across {len(platform_stats)} platforms.")

if __name__ == "__main__":
    main()