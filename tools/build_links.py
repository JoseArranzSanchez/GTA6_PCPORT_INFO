#!/usr/bin/env python3
"""Regenerate LINKS.csv (with an `open` column) and LINKS.md / LINKS.html.

Usage:
    python tools/build_links.py

- Keeps the original columns: category, name, url, note.
- Adds `open` with an =HYPERLINK() formula for Excel/LibreOffice.
- Generates LINKS.md with clickable Markdown links for GitHub.
- Generates LINKS.html with clickable links for any browser.
"""

from __future__ import annotations

import csv
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "LINKS.csv"
MD_PATH = ROOT / "LINKS.md"
HTML_PATH = ROOT / "LINKS.html"

FIELDS = ["category", "name", "url", "note", "open"]

CATEGORY_MAP = {
    "Aprender": "Learn",
    "Busqueda": "Search",
    "Búsqueda": "Search",
    "Contacto": "Contact",
    "Herramienta": "Tool",
    "Legal": "Legal",
    "Oficial": "Official",
    "Prensa": "Press",
    "REA": "REA",
    "Repo": "Repository",
    "Seguridad": "Security",
    "Tracker": "Tracker",
    "Video": "Video",
}

NAME_MAP = {
    "Canal Code Bear": "Code Bear channel",
    "XDA exe filtrado": "XDA leaked exe",
    "TweakTown 3 horas": "TweakTown 3 hours",
    "VGTimes menus no gameplay": "VGTimes menus, no gameplay",
    "TwistedVoxel dev abandona": "TwistedVoxel developer quits",
    "MakeUseOf port no oficial": "MakeUseOf unofficial port",
    "XDA hoax GTA V reciclado": "XDA hoax recycled GTA V",
    "Notebookcheck PS5 Pro DLSS5": "Notebookcheck PS5 Pro DLSS 5",
    "Leonida continuacion": "Leonida continuation",
    "Repos gta 6": "gta 6 repositories",
    "Repos gta6": "gta6 repositories",
    "Repos leonida": "leonida repositories",
    "Topic gta6": "topic:gta6",
    "Topic leonida": "topic:leonida",
    "Topic xbox-series-x": "topic:xbox-series-x",
    "Topic reverse-engineer-anything": "topic:reverse-engineer-anything",
    "TorrentFreak demanda re3": "TorrentFreak re3 lawsuit",
    "RTE GTA hacker": "RTÉ GTA hacker",
    "Cyber Security News 355 dominios": "Cyber Security News 355 domains",
    "Xbox Wire cloud y remote play 23-11": "Xbox Wire cloud and Remote Play 23-11",
    "Ficha GTA VI Xbox": "GTA VI Xbox store page",
    "Este repositorio — maintainer": "This repository — maintainer",
    "Este repositorio — issues": "This repository — issues",
}

NOTE_MAP = {
    "Autor del vídeo": "Video author",
    "Bloquea bots": "Blocks bots",
    "Canal oficial": "Official channel",
    "Canal publicado en el README": "Channel published in the README",
    "Claims auto-reportados": "Self-reported claims",
    "Contacto": "Contact",
    "Decoder BCPack": "BCPack decoder",
    "Es sobre Muguet GTA V": "It is about Muguet (GTA V)",
    "Explorador RPF9": "RPF9 explorer",
    "Fork de XCL": "XCL fork",
    "GitHub del proyecto": "Project GitHub",
    "Lista curada": "Curated list",
    "Perfil público": "Public profile",
    "Publicado en la descripción": "Published in the description",
    "Recompilacion estatica": "Static recompilation",
    "Soporte": "Support",
    "Specs de formato": "Format specs",
    "Web personal": "Personal website",
}

CONTACTS = [
    ("Contact", "XCL — maintainer", "https://github.com/xcl-dev", "Project GitHub"),
    ("Contact", "XCL — Discord", "https://discord.gg/xcl", "Official channel"),
    ("Contact", "VIctory — maintainer", "https://github.com/Marvisak", "Project GitHub"),
    ("Contact", "VIctory — issues", "https://github.com/Marvisak/VIctory/issues", "Support"),
    ("Contact", "Leonida — maintainer", "https://github.com/ubiquitarianism", "Project GitHub"),
    ("Contact", "Leonida — Discord", "https://discord.gg/ETf4qj5acN", "Channel published in the README"),
    ("Contact", "Xbox2Windows — maintainer", "https://github.com/R0Y00", "Project GitHub"),
    ("Contact", "Xbox2Windows — Discord", "https://discord.gg/DMcmNtpd6R", "Official channel"),
    ("Contact", "AnyXboxX — maintainer", "https://github.com/LooperSalty", "Project GitHub"),
    ("Contact", "AnyXboxX — Discord", "https://discord.gg/TcX42vRyPU", "Official channel"),
    ("Contact", "OpenScarlett — maintainer", "https://github.com/californiaAlmonds", "Project GitHub"),
    ("Contact", "OpenScarlett — Discord", "https://discord.gg/sShMY2fjR", "Official channel"),
    ("Contact", "XValkyrie — maintainer", "https://github.com/sammwyy", "Project GitHub"),
    ("Contact", "XValkyrie — X/Twitter", "https://x.com/sammwyy", "Public profile"),
    ("Contact", "XValkyrie — website", "https://sammwy.com/", "Personal website"),
    ("Contact", "GTA6-BootTest — maintainer", "https://github.com/OnlyMoisties", "Project GitHub"),
    ("Contact", "GTA6-BootTest — issues", "https://github.com/OnlyMoisties/GTA6-BootTest/issues", "Support"),
    ("Contact", "awesome-gta6-RE — maintainer", "https://github.com/Ahmet-Dedeler", "Project GitHub"),
    ("Contact", "awesome-gta6-RE — Discord", "https://discord.gg/CjcDBg3nf", "Official channel"),
    ("Contact", "awesome-gta6-RE — X/Twitter", "https://x.com/ahmetbuilds", "Public profile"),
    ("Contact", "GTA6-Asset-Info — maintainer", "https://github.com/TrinitronClient", "Project GitHub"),
    ("Contact", "GTA6-Asset-Info — issues", "https://github.com/TrinitronClient/GTA6-Asset-Info/issues", "Support"),
    ("Contact", "rpf9-explorer — maintainer", "https://github.com/breadbbbb", "Project GitHub"),
    ("Contact", "rpf9-explorer — issues", "https://github.com/breadbbbb/rpf9-explorer/issues", "Support"),
    ("Contact", "PercyStar — maintainer", "https://github.com/rpatty-dev", "Project GitHub"),
    ("Contact", "PercyStar — website", "https://nitech.dev", "Web"),
    ("Contact", "SixNG — maintainer", "https://github.com/holdmysocks", "Project GitHub"),
    ("Contact", "SixNG — website", "https://holdmysocks.dev", "Web"),
    ("Contact", "Project Leonida Legacy — maintainer", "https://github.com/ProjectLeonidaL", "Project GitHub"),
    ("Contact", "Project Leonida Legacy — Discord", "https://discord.gg/dxMD2XqyEJ", "Channel published in the README"),
    ("Contact", "Code Bear — YouTube", "https://www.youtube.com/@thecodebear", "Video author"),
    ("Contact", "Code Bear — Instagram", "https://instagram.com/thecodebear", "Published in the description"),
    ("Contact", "This repository — maintainer", "https://github.com/JoseArranzSanchez", "GitHub"),
    ("Contact", "This repository — issues", "https://github.com/JoseArranzSanchez/GTA6_PCPORT_INFO/issues", "Contact"),
    ("Contact", "PortWatch VI — maintainer", "https://github.com/4lwayz", "Project GitHub"),
    ("Contact", "PortWatch VI — X/Twitter", "https://x.com/lithuaniangroyp", "Tracker account"),
]

TRACKERS = [
    ("Tracker", "PortWatch VI — site", "https://portwatch-vi.xyz/", "Live tracker"),
    ("Tracker", "PortWatch VI — repository", "https://github.com/4lwayz/portwatch-vi", "Source code"),
    ("Tracker", "PortWatch VI — data", "https://portwatch-vi.xyz/data/tracker.json", "Machine-readable data"),
    (
        "Press",
        "Notebookcheck — PortWatch VI",
        "https://www.notebookcheck.net/GTA-6-This-website-lets-you-track-the-PC-recompilation-live.1458797.0.html",
        "Published 24-11-2026",
    ),
]


def normalize(row: dict) -> dict:
    return {
        "category": (row.get("category") or row.get("categoria") or "Other").strip(),
        "name": (row.get("name") or row.get("nombre") or "").strip(),
        "url": (row.get("url") or "").strip(),
        "note": (row.get("note") or row.get("nota") or "").strip(),
    }


def translate(row: dict) -> dict:
    row["category"] = CATEGORY_MAP.get(row["category"], row["category"])
    row["name"] = NAME_MAP.get(row["name"], row["name"])
    row["note"] = NOTE_MAP.get(row["note"], row["note"])
    return row


def markdown_escape(value: str) -> str:
    return (value or "").replace("|", "\\|")


def main() -> None:
    with CSV_PATH.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = [translate(normalize(row)) for row in csv.DictReader(handle)]

    # Rebuild the contact block in English instead of keeping the old Spanish rows.
    rows = [row for row in rows if row["category"] != "Contact"]
    existing = {(row["category"], row["name"]) for row in rows}
    for category, name, url, note in TRACKERS + CONTACTS:
        if (category, name) not in existing:
            rows.append({"category": category, "name": name, "url": url, "note": note})

    for row in rows:
        url = row["url"]
        row["open"] = f'=HYPERLINK("{url}","Open")' if url else ""

    with CSV_PATH.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        writer.writerows(rows)

    grouped: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        grouped.setdefault(row["category"], []).append(row)

    lines = [
        "# Links — GTA VI on PC / Xbox Series X",
        "",
        "**Cut-off:** 24-11-2026, 19:00 CET. **Method:** links reviewed at the cut-off date; "
        "no downloads, executables, keys or leaked material are linked.",
        "",
        "CSV version with an `open` column for Excel/LibreOffice: [`LINKS.csv`](LINKS.csv).",
        "If your spreadsheet does not evaluate `=HYPERLINK()`, use the `url` column or this page.",
        "",
    ]

    for category in sorted(grouped, key=lambda c: (c != "Video", c)):
        lines.append(f"## {category}")
        lines.append("")
        lines.append("| Name | Link | Note |")
        lines.append("|---|---|---|")
        for row in grouped[category]:
            name = markdown_escape(row["name"])
            url = row["url"]
            note = markdown_escape(row["note"]) or "—"
            lines.append(f"| {name} | [Open]({url}) | {note} |")
        lines.append("")

    MD_PATH.write_text("\n".join(lines), encoding="utf-8")

    html_lines = [
        "<!doctype html>",
        '<html lang="en">',
        "<head>",
        '  <meta charset="utf-8">',
        '  <meta name="viewport" content="width=device-width, initial-scale=1">',
        "  <title>Links — GTA VI on PC / Xbox Series X</title>",
        "  <style>",
        "    body{font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;margin:2rem;line-height:1.5;color:#111}",
        "    table{border-collapse:collapse;width:100%;margin:1rem 0 2rem}",
        "    th,td{border:1px solid #ccc;padding:.45rem .6rem;text-align:left;vertical-align:top}",
        "    th{background:#f3f3f3}",
        "    a{color:#0645ad}",
        "    h1{margin-bottom:.25rem}",
        "    .note{color:#555}",
        "  </style>",
        "</head>",
        "<body>",
        "  <h1>Links — GTA VI on PC / Xbox Series X</h1>",
        '  <p class="note"><strong>Cut-off:</strong> 24-11-2026, 19:00 CET. Links reviewed at the cut-off date; '
        "no downloads, executables, keys or leaked material are linked.</p>",
        '  <p class="note">Data version: <a href="LINKS.csv">LINKS.csv</a> · '
        'Markdown version: <a href="LINKS.md">LINKS.md</a> · '
        '<a href="README.md">Back to the README</a></p>',
    ]

    for category in sorted(grouped, key=lambda c: (c != "Video", c)):
        html_lines.append(f"  <h2>{html.escape(category)}</h2>")
        html_lines.append("  <table>")
        html_lines.append("    <thead><tr><th>Name</th><th>Link</th><th>Note</th></tr></thead>")
        html_lines.append("    <tbody>")
        for row in grouped[category]:
            name = html.escape(row["name"])
            url = html.escape(row["url"], quote=True)
            note = html.escape(row["note"]) or "—"
            html_lines.append(
                f'      <tr><td>{name}</td><td><a href="{url}" target="_blank" rel="noopener noreferrer">Open</a></td><td>{note}</td></tr>'
            )
        html_lines.append("    </tbody>")
        html_lines.append("  </table>")

    html_lines.extend(["</body>", "</html>", ""])
    HTML_PATH.write_text("\n".join(html_lines), encoding="utf-8")


if __name__ == "__main__":
    main()
