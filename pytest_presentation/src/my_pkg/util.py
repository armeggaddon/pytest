import csv
import asyncio
from pathlib import Path

def add(a, b):
    return a + b

def inc(x):
    return x + 1

def is_palindrome(s: str) -> bool:
    s2 = ''.join(ch.lower() for ch in s if ch.isalnum())
    return s2 == s2[::-1]

def write_csv(path, rows):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

def read_csv(path):
    p = Path(path)
    with p.open('r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        return [row for row in reader]

async def async_fetch(x):
    # trivial async example to demonstrate pytest-asyncio
    await asyncio.sleep(0)
    return f"fetched:{x}"
