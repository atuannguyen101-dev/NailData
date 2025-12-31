#!/usr/bin/env python3
"""
Direct image labeling - Read images and prepare for vision analysis
"""

import base64
import csv
from pathlib import Path

IMAGES_DIR = Path("c:/Users/atuan/work/NailSite/scripts/trained")
OUTPUT_CSV = "nail_labels.csv"

# Images to process
IMAGES = sorted([f.name for f in IMAGES_DIR.glob('*.jpg')])

# Prepare analysis data
print("Preparing image data for analysis...")
print(f"Total images: {len(IMAGES)}\n")

# Read first image as base64 for testing
for i, img in enumerate(IMAGES[:5], 1):  # Just first 5 for now
    path = IMAGES_DIR / img
    with open(path, 'rb') as f:
        b64_data = base64.b64encode(f.read()).decode()
    
    print(f"[{i}] {img}")
    print(f"    Data length: {len(b64_data)} chars")
    print(f"    First 80 chars: {b64_data[:80]}...")
    print()

print("Ready for vision analysis...")
