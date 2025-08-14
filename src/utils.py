"""
Utility helpers for the DoD Supply Chain project (integrated).
"""
from __future__ import annotations
from pathlib import Path
import re

def find_project_root(start: Path) -> Path:
    """Walk upward to find a folder containing 'data'."""
    for p in [start, *start.parents]:
        if (p / "data").exists():
            return p
    return start

def ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)

def simple_vendor_normalize(name: str) -> str:
    """Normalize vendor name without heavy fuzzy matching."""
    if not isinstance(name, str):
        return ""
    n = name.upper()
    n = re.sub(r"[.,&']", " ", n)  # remove punctuation
    n = f" {n} "
    for s in [" CORPORATION ", " CORP ", " INC ", " LLC ", " CO ", " LTD ", " TECHNOLOGIES "]:
        n = n.replace(s, " ")
    n = re.sub(r"\s+", " ", n).strip()
    return n

def clean_naics(raw_code) -> str:
    """Return a 6-digit NAICS (as string) if possible; else empty string."""
    if raw_code is None:
        return ""
    s = str(raw_code)
    digits = re.sub(r"\D", "", s)
    return digits[:6] if digits else ""

US_STATE_MAP = {
    "ALABAMA":"AL","ALASKA":"AK","ARIZONA":"AZ","ARKANSAS":"AR","CALIFORNIA":"CA","COLORADO":"CO",
    "CONNECTICUT":"CT","DELAWARE":"DE","FLORIDA":"FL","GEORGIA":"GA","HAWAII":"HI","IDAHO":"ID",
    "ILLINOIS":"IL","INDIANA":"IN","IOWA":"IA","KANSAS":"KS","KENTUCKY":"KY","LOUISIANA":"LA",
    "MAINE":"ME","MARYLAND":"MD","MASSACHUSETTS":"MA","MICHIGAN":"MI","MINNESOTA":"MN",
    "MISSISSIPPI":"MS","MISSOURI":"MO","MONTANA":"MT","NEBRASKA":"NE","NEVADA":"NV","NEW HAMPSHIRE":"NH",
    "NEW JERSEY":"NJ","NEW MEXICO":"NM","NEW YORK":"NY","NORTH CAROLINA":"NC","NORTH DAKOTA":"ND",
    "OHIO":"OH","OKLAHOMA":"OK","OREGON":"OR","PENNSYLVANIA":"PA","RHODE ISLAND":"RI",
    "SOUTH CAROLINA":"SC","SOUTH DAKOTA":"SD","TENNESSEE":"TN","TEXAS":"TX","UTAH":"UT",
    "VERMONT":"VT","VIRGINIA":"VA","WASHINGTON":"WA","WEST VIRGINIA":"WV","WISCONSIN":"WI","WYOMING":"WY"
}

def to_usps_state(value: str) -> str:
    """Map full state names to USPS two-letter codes; pass through 2-letter codes."""
    if not isinstance(value, str):
        return ""
    v = value.strip().upper()
    if len(v) == 2:
        return v
    return US_STATE_MAP.get(v, v)
