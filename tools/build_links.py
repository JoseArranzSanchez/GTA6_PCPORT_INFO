#!/usr/bin/env python3
"""Regenera ENLACES.csv (con columna `abrir`) y ENLACES.md a partir del CSV.

Uso:
    python tools/build_links.py

- Mantiene las columnas originales: categoria, nombre, url, nota.
- Añade `abrir` con una fórmula =HYPERLINK() para Excel/LibreOffice.
- Genera ENLACES.md con enlaces Markdown clicables para GitHub.
"""

from __future__ import annotations

import csv
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "ENLACES.csv"
MD_PATH = ROOT / "ENLACES.md"
HTML_PATH = ROOT / "ENLACES.html"

FIELDS = ["categoria", "nombre", "url", "nota", "abrir"]

CONTACTS = [
    ("Contacto", "XCL — maintainer", "https://github.com/xcl-dev", "GitHub del proyecto"),
    ("Contacto", "XCL — Discord", "https://discord.gg/xcl", "Canal oficial"),
    ("Contacto", "VIctory — maintainer", "https://github.com/Marvisak", "GitHub"),
    ("Contacto", "VIctory — issues", "https://github.com/Marvisak/VIctory/issues", "Soporte"),
    ("Contacto", "Leonida — maintainer", "https://github.com/ubiquitarianism", "GitHub"),
    ("Contacto", "Leonida — Discord", "https://discord.gg/ETf4qj5acN", "Canal publicado en el README"),
    ("Contacto", "Xbox2Windows — maintainer", "https://github.com/R0Y00", "GitHub"),
    ("Contacto", "Xbox2Windows — Discord", "https://discord.gg/DMcmNtpd6R", "Canal oficial"),
    ("Contacto", "AnyXboxX — maintainer", "https://github.com/LooperSalty", "GitHub"),
    ("Contacto", "AnyXboxX — Discord", "https://discord.gg/TcX42vRyPU", "Canal oficial"),
    ("Contacto", "OpenScarlett — maintainer", "https://github.com/californiaAlmonds", "GitHub"),
    ("Contacto", "OpenScarlett — Discord", "https://discord.gg/sShMY2fjR", "Canal oficial"),
    ("Contacto", "XValkyrie — maintainer", "https://github.com/sammwyy", "GitHub"),
    ("Contacto", "XValkyrie — X/Twitter", "https://x.com/sammwyy", "Perfil público"),
    ("Contacto", "XValkyrie — web", "https://sammwy.com/", "Web personal"),
    ("Contacto", "GTA6-BootTest — maintainer", "https://github.com/OnlyMoisties", "GitHub"),
    ("Contacto", "GTA6-BootTest — issues", "https://github.com/OnlyMoisties/GTA6-BootTest/issues", "Soporte"),
    ("Contacto", "awesome-gta6-RE — maintainer", "https://github.com/Ahmet-Dedeler", "GitHub"),
    ("Contacto", "awesome-gta6-RE — Discord", "https://discord.gg/CjcDBg3nf", "Canal oficial"),
    ("Contacto", "awesome-gta6-RE — X/Twitter", "https://x.com/ahmetbuilds", "Perfil público"),
    ("Contacto", "GTA6-Asset-Info — maintainer", "https://github.com/TrinitronClient", "GitHub"),
    ("Contacto", "GTA6-Asset-Info — issues", "https://github.com/TrinitronClient/GTA6-Asset-Info/issues", "Soporte"),
    ("Contacto", "rpf9-explorer — maintainer", "https://github.com/breadbbbb", "GitHub"),
    ("Contacto", "rpf9-explorer — issues", "https://github.com/breadbbbb/rpf9-explorer/issues", "Soporte"),
    ("Contacto", "PercyStar — maintainer", "https://github.com/rpatty-dev", "GitHub"),
    ("Contacto", "PercyStar — web", "https://nitech.dev", "Web"),
    ("Contacto", "SixNG — maintainer", "https://github.com/holdmysocks", "GitHub"),
    ("Contacto", "SixNG — web", "https://holdmysocks.dev", "Web"),
    ("Contacto", "Project Leonida Legacy — maintainer", "https://github.com/ProjectLeonidaL", "GitHub"),
    ("Contacto", "Project Leonida Legacy — Discord", "https://discord.gg/dxMD2XqyEJ", "Canal publicado en el README"),
    ("Contacto", "Code Bear — YouTube", "https://www.youtube.com/@thecodebear", "Autor del vídeo"),
    ("Contacto", "Code Bear — Instagram", "https://instagram.com/thecodebear", "Publicado en la descripción"),
    ("Contacto", "Este repositorio — maintainer", "https://github.com/JoseArranzSanchez", "GitHub"),
    ("Contacto", "Este repositorio — issues", "https://github.com/JoseArranzSanchez/GTA6_PCPORT_INFO/issues", "Contacto"),
]


def markdown_escape(value: str) -> str:
    return (value or "").replace("|", "\\|")


def main() -> None:
    with CSV_PATH.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    # Normaliza columnas y elimina una posible columna `abrir` previa.
    for row in rows:
        row.pop("abrir", None)

    existing = {(row.get("categoria", ""), row.get("nombre", "")) for row in rows}
    for categoria, nombre, url, nota in CONTACTS:
        if (categoria, nombre) not in existing:
            rows.append({"categoria": categoria, "nombre": nombre, "url": url, "nota": nota})

    for row in rows:
        url = (row.get("url") or "").strip()
        row["url"] = url
        row["abrir"] = f'=HYPERLINK("{url}","Abrir")' if url else ""

    with CSV_PATH.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        writer.writerows(rows)

    grouped: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        grouped.setdefault(row.get("categoria", "Otros"), []).append(row)

    lines = [
        "# Enlaces — GTA VI en PC / Xbox Series X",
        "",
        "**Corte:** 24-11-2026, 19:00 CET. **Método:** enlaces revisados en la fecha de corte; "
        "no se enlazan descargas, ejecutables, claves ni material filtrado.",
        "",
        "Versión CSV con columna `abrir` para Excel/LibreOffice: [`ENLACES.csv`](ENLACES.csv).",
        "Si tu hoja de cálculo no evalúa `=HYPERLINK()`, usa la columna `url` o esta página.",
        "",
    ]

    for categoria in sorted(grouped, key=lambda c: (c != "Video", c)):
        lines.append(f"## {categoria}")
        lines.append("")
        lines.append("| Nombre | Enlace | Nota |")
        lines.append("|---|---|---|")
        for row in grouped[categoria]:
            nombre = markdown_escape(row.get("nombre", ""))
            url = row.get("url", "")
            nota = markdown_escape(row.get("nota", "")) or "—"
            lines.append(f"| {nombre} | [Abrir]({url}) | {nota} |")
        lines.append("")

    MD_PATH.write_text("\n".join(lines), encoding="utf-8")

    html_lines = [
        "<!doctype html>",
        '<html lang="es">',
        "<head>",
        '  <meta charset="utf-8">',
        '  <meta name="viewport" content="width=device-width, initial-scale=1">',
        "  <title>Enlaces — GTA VI en PC / Xbox Series X</title>",
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
        "  <h1>Enlaces — GTA VI en PC / Xbox Series X</h1>",
        '  <p class="note"><strong>Corte:</strong> 24-11-2026, 19:00 CET. Enlaces revisados en la fecha de corte; '
        "no se enlazan descargas, ejecutables, claves ni material filtrado.</p>",
        '  <p class="note">Versión de datos: <a href="ENLACES.csv">ENLACES.csv</a> · '
        'Versión Markdown: <a href="ENLACES.md">ENLACES.md</a> · '
        '<a href="README.md">Volver al README</a></p>',
    ]

    for categoria in sorted(grouped, key=lambda c: (c != "Video", c)):
        html_lines.append(f"  <h2>{html.escape(categoria)}</h2>")
        html_lines.append("  <table>")
        html_lines.append("    <thead><tr><th>Nombre</th><th>Enlace</th><th>Nota</th></tr></thead>")
        html_lines.append("    <tbody>")
        for row in grouped[categoria]:
            nombre = html.escape(row.get("nombre", ""))
            url = html.escape(row.get("url", ""), quote=True)
            nota = html.escape(row.get("nota", "")) or "—"
            html_lines.append(
                f'      <tr><td>{nombre}</td><td><a href="{url}" target="_blank" rel="noopener noreferrer">Abrir</a></td><td>{nota}</td></tr>'
            )
        html_lines.append("    </tbody>")
        html_lines.append("  </table>")

    html_lines.extend(["</body>", "</html>", ""])
    HTML_PATH.write_text("\n".join(html_lines), encoding="utf-8")


if __name__ == "__main__":
    main()
