#!/usr/bin/env python3
"""Update the project status from the GitHub API.

Generates/updates:
- README.md: block between <!-- AUTO:STATUS:START --> and <!-- AUTO:STATUS:END -->
- STATUS.md: full table
- data/status.json: machine-readable data

Usage:
    python tools/update_status.py
    python tools/update_status.py --render-only   # no API calls; use data/status.json

GitHub Actions runs this every hour with GITHUB_TOKEN, which provides a larger API quota.
No external dependencies: standard library only.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
STATUS = ROOT / "STATUS.md"
DATA = ROOT / "data" / "status.json"

SEARCHES = [
    ("gta 6", "gta 6"),
    ("gta6", "gta6"),
    ("leonida", "leonida"),
    ('"grand theft auto vi"', '"grand theft auto vi"'),
    ("topic:gta6", "topic:gta6"),
    ("topic:xbox-series-x", "topic:xbox-series-x"),
    ("topic:reverse-engineer-anything", "topic:reverse-engineer-anything"),
]

REPOS = [
    "xcl-dev/xcl",
    "Marvisak/VIctory",
    "ubiquitarianism/leonida",
    "R0Y00/Xbox2Windows",
    "LooperSalty/AnyXboxX",
    "OnlyMoisties/GTA6-BootTest",
    "californiaAlmonds/OpenScarlett",
    "Ahmet-Dedeler/awesome-gta6-reverse-engineering",
]

TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
HEADERS = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "GTA6-PCPORT-INFO-status-bot",
    "X-GitHub-Api-Version": "2022-11-28",
}
if TOKEN:
    HEADERS["Authorization"] = f"Bearer {TOKEN}"


def get_json(url: str) -> dict:
    request = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def search_count(query: str) -> int:
    params = urllib.parse.urlencode({"q": query, "per_page": 1})
    return int(get_json(f"https://api.github.com/search/repositories?{params}")["total_count"])


def repo_info(full_name: str) -> dict:
    data = get_json(f"https://api.github.com/repos/{full_name}")
    return {
        "full_name": data.get("full_name", full_name),
        "html_url": data.get("html_url"),
        "stars": data.get("stargazers_count"),
        "forks": data.get("forks_count"),
        "open_issues": data.get("open_issues_count"),
        "pushed_at": data.get("pushed_at"),
        "archived": data.get("archived", False),
    }


def fmt_int(value) -> str:
    return f"{value:,}" if isinstance(value, int) else "n/d"


def fmt_k(value) -> str:
    if not isinstance(value, int):
        return "n/d"
    if value >= 1000:
        return f"{value / 1000:.1f}k"
    return str(value)


def fmt_date(value) -> str:
    return value[:10] if isinstance(value, str) and len(value) >= 10 else "n/d"


def load_previous() -> dict:
    if not DATA.exists():
        return {}
    try:
        return json.loads(DATA.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def last_sunday_utc(year: int, month: int) -> datetime:
    day = datetime(year, month, 31, tzinfo=timezone.utc)
    while day.weekday() != 6:  # 6 = Sunday
        day -= timedelta(days=1)
    return day.replace(hour=1, minute=0, second=0, microsecond=0)


def madrid_now(now_utc: datetime) -> tuple[datetime, str]:
    """Return Madrid time and the CET/CEST label.

    On Linux (GitHub Actions) it uses zoneinfo. On Windows without tzdata it
    applies the European summer-time rule: last Sunday of March to last Sunday
    of October.
    """
    try:
        local = now_utc.astimezone(ZoneInfo("Europe/Madrid"))
        return local, (local.strftime("%Z") or "CET")
    except Exception:  # noqa: BLE001
        start = last_sunday_utc(now_utc.year, 3)
        end = last_sunday_utc(now_utc.year, 10)
        offset = 2 if start <= now_utc < end else 1
        local = now_utc.astimezone(timezone(timedelta(hours=offset)))
        return local, "CEST" if offset == 2 else "CET"


def collect(previous: dict) -> tuple[dict, dict, list[str]]:
    previous_counts = previous.get("counts", {})
    previous_repos = previous.get("repos", {})
    errors: list[str] = []

    counts: dict[str, int | None] = {}
    for query, label in SEARCHES:
        try:
            counts[label] = search_count(query)
        except Exception as exc:  # noqa: BLE001
            counts[label] = previous_counts.get(label)
            errors.append(f"Search `{query}`: {exc}")

    repos: dict[str, dict] = {}
    for full_name in REPOS:
        try:
            repos[full_name] = repo_info(full_name)
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                repos[full_name] = {
                    "full_name": full_name,
                    "html_url": f"https://github.com/{full_name}",
                    "stars": None,
                    "forks": None,
                    "open_issues": None,
                    "pushed_at": None,
                    "archived": True,
                    "status": 404,
                }
                errors.append(f"`{full_name}`: 404 (not available)")
            else:
                repos[full_name] = previous_repos.get(full_name, {})
                errors.append(f"`{full_name}`: HTTP {exc.code}")
        except Exception as exc:  # noqa: BLE001
            repos[full_name] = previous_repos.get(full_name, {})
            errors.append(f"`{full_name}`: {exc}")

    return counts, repos, errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--render-only",
        action="store_true",
        help="Do not call the API; render from data/status.json",
    )
    args = parser.parse_args()

    previous = load_previous()

    if args.render_only:
        if not previous:
            print("No data/status.json for --render-only", file=sys.stderr)
            return 1
        counts = previous.get("counts", {})
        repos = previous.get("repos", {})
        errors = previous.get("errors", [])
        generated = previous.get("generated_at_local")
        local = datetime.fromisoformat(generated) if generated else datetime.now(timezone.utc)
        tz_label = previous.get("timezone_label") or "CET"
    else:
        counts, repos, errors = collect(previous)
        now_utc = datetime.now(timezone.utc)
        local, tz_label = madrid_now(now_utc)
        if not any(isinstance(value, int) for value in counts.values()) and not any(
            repo.get("stars") is not None for repo in repos.values()
        ):
            print("No data was fetched; aborting without writing.", file=sys.stderr)
            return 1

    stamp = local.strftime("%d-%m-%Y, %H:%M") + f" {tz_label}"
    payload = {
        "generated_at_utc": local.astimezone(timezone.utc).isoformat(timespec="seconds"),
        "generated_at_local": local.isoformat(timespec="seconds"),
        "timezone": "Europe/Madrid",
        "timezone_label": tz_label,
        "source": "GitHub API",
        "counts": counts,
        "repos": repos,
        "errors": errors,
    }

    if not args.render_only:
        DATA.parent.mkdir(parents=True, exist_ok=True)
        DATA.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    xcl = repos.get("xcl-dev/xcl", {})
    victory = repos.get("Marvisak/VIctory", {})
    leonida = repos.get("ubiquitarianism/leonida", {})

    readme_block = f"""### Status right now (auto-updated)

**Last update:** {stamp} (Europe/Madrid).

- **GTA VI:** released on 19-11-2026 on PS5 and Xbox Series X|S; no PC version announced.
- **Unofficial port:** no public project is playable; the best state is menus and a black world load.
- **GitHub:** `gta 6` {fmt_int(counts.get("gta 6"))} · `gta6` {fmt_int(counts.get("gta6"))} · `leonida` {fmt_int(counts.get("leonida"))} · `topic:gta6` {fmt_int(counts.get("topic:gta6"))}.
- **XCL:** {fmt_k(xcl.get("stars"))} stars · {fmt_int(xcl.get("open_issues"))} issues+PRs · last push {fmt_date(xcl.get("pushed_at"))}.
- **VIctory:** {fmt_k(victory.get("stars"))} stars · {fmt_int(victory.get("open_issues"))} issues+PRs · last push {fmt_date(victory.get("pushed_at"))}.
- **Leonida:** {fmt_k(leonida.get("stars"))} stars · {fmt_int(leonida.get("open_issues"))} issues+PRs · last push {fmt_date(leonida.get("pushed_at"))}.
- **Legal:** Take-Two continues DMCA takedowns; the 18-11 notice is about GTA V (Muguet), not GTA VI.
- **Cloud:** GTA VI on Xbox Cloud Gaming is console-only; on PC only Remote Play from a console.

[Full detail](STATUS.md) · [JSON data](data/status.json)"""

    status_lines = [
        "# Project status (auto-updated)",
        "",
        f"**Last update:** {stamp} (Europe/Madrid).",
        "**Source:** GitHub API. **Time zone:** Europe/Madrid.",
        "",
        "> Read-only data. It may be delayed or affected by API errors; it is not an official source.",
        "",
        "## Searches",
        "",
        "| Search | Results |",
        "|---|---:|",
    ]
    for _, label in SEARCHES:
        status_lines.append(f"| `{label}` | {fmt_int(counts.get(label))} |")
    status_lines += [
        "",
        "## Repositories",
        "",
        "| Repository | Stars | Forks | Issues+PRs | Last push |",
        "|---|---:|---:|---:|---|",
    ]
    for full_name in REPOS:
        repo = repos.get(full_name, {})
        status_lines.append(
            f"| [`{full_name}`](https://github.com/{full_name}) | {fmt_k(repo.get('stars'))} | "
            f"{fmt_int(repo.get('forks'))} | {fmt_int(repo.get('open_issues'))} | {fmt_date(repo.get('pushed_at'))} |"
        )
    status_lines += ["", "## Errors from the last run", ""]
    if errors:
        status_lines += [f"- {error}" for error in errors]
    else:
        status_lines.append("None.")
    status_lines.append("")
    STATUS.write_text("\n".join(status_lines), encoding="utf-8")

    readme = README.read_text(encoding="utf-8")
    pattern = re.compile(r"<!-- AUTO:STATUS:START -->.*?<!-- AUTO:STATUS:END -->", re.DOTALL)
    if not pattern.search(readme):
        print("AUTO:STATUS markers not found in README.md", file=sys.stderr)
        return 1
    replacement = f"<!-- AUTO:STATUS:START -->\n{readme_block}\n<!-- AUTO:STATUS:END -->"
    new_readme = pattern.sub(replacement, readme)
    if new_readme != readme:
        README.write_text(new_readme, encoding="utf-8")

    print(f"Updated: {stamp} | errors: {len(errors)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
