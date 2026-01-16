from __future__ import annotations

from typing import List


def clean_urls(urls: List[str]) -> List[str]:
    """Trim and filter empty URL inputs."""
    out: List[str] = []
    for u in urls:
        if not u:
            continue
        u = u.strip()
        if u:
            out.append(u)
    return out


def unique_preserve_order(items: List[str]) -> List[str]:
    """Deduplicate while preserving original order."""
    seen = set()
    out: List[str] = []
    for x in items:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out
