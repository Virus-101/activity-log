#!/usr/bin/env python3
"""Append a dated entry (with a quote) to DAILY_LOG.md, keeping the last 60 entries."""
import datetime as dt
import pathlib

LOG = pathlib.Path("DAILY_LOG.md")
KEEP = 60
QUOTES = [
    "Premature optimization is the root of all evil. - Knuth",
    "Make it work, make it right, make it fast. - Kent Beck",
    "Simplicity is prerequisite for reliability. - Dijkstra",
    "Programs must be written for people to read. - Abelson & Sussman",
    "Talk is cheap. Show me the code. - Linus Torvalds",
    "First, solve the problem. Then, write the code. - John Johnson",
    "Debugging is twice as hard as writing the code. - Kernighan",
    "Code is like humor. When you have to explain it, it's bad. - Cory House",
]

today = dt.datetime.now(dt.timezone.utc)
quote = QUOTES[today.toordinal() % len(QUOTES)]
entry = f"- **{today:%Y-%m-%d}** - {quote}"

header = "# Daily Log\n\n"
lines = []
if LOG.exists():
    lines = [l for l in LOG.read_text(encoding="utf-8").splitlines() if l.startswith("- **")]

if lines and lines[-1].startswith(f"- **{today:%Y-%m-%d}**"):
    print("Already logged today; nothing to do.")
    raise SystemExit(0)

lines.append(entry)
LOG.write_text(header + "\n".join(lines[-KEEP:]) + "\n", encoding="utf-8")
print(f"Added: {entry}")
