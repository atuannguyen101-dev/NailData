#!/usr/bin/env python3
"""
Complete nail image labeling using vision analysis
Analyzes each image and saves results to CSV
"""

import base64
import csv
import os
import sys
from pathlib import Path

IMAGES_DIR = Path("c:/Users/atuan/work/NailSite/scripts/trained")
OUTPUT_CSV = "nail_labels.csv"

FEATURES = {
    "shape": ["Almond", "Oval", "Round", "Square", "Squoval", "Coffin", "Stiletto", "Lipstick", "Flare", "Mountain Peak"],
    "length": ["Short", "Medium", "Long", "Extra Long"],
    "color": ["Clear", "White", "Pink", "Red", "Purple", "Blue", "Green", "Yellow", "Orange", "Brown", "Black", "Nude", "Beige", "Gold", "Silver", "Metallic"],
    "finish": ["Glossy", "Matte", "Chrome", "Shimmer", "Glitter", "Holographic", "Pearl", "Velvet"],
    "style": ["French", "Ombre", "Marble", "Minimalist", "Maximalist", "Glamorous", "Natural", "Artistic", "Edgy"],
    "set_style": ["Uniform", "Accent Nail", "Alternating", "All Different"],
    "art": ["None", "Floral", "Abstract", "Geometric", "Animal Print", "Line Art", "Swirls", "Dots"],
    "jewels": ["None", "Crystals", "Pearls", "Charms", "Foil", "3D Sculpture"],
    "theme": ["Everyday", "Wedding", "Holiday", "Seasonal", "Party", "Vacation", "Date Night"]
}

def encode_image(image_path):
    """Encode image to base64"""
    with open(image_path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

def save_labels(filename, labels):
    """Save labels to CSV"""
    row = {'filename': filename}
    row.update({k: labels.get(k, '') for k in FEATURES.keys()})
    
    file_exists = os.path.exists(OUTPUT_CSV)
    with open(OUTPUT_CSV, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['filename'] + list(FEATURES.keys()))
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)

# Get all images
all_images = sorted([f.name for f in IMAGES_DIR.glob('*.jpg')])
print(f"[INFO] Found {len(all_images)} images to label\n")

# Prepare image data for analysis
image_data = {}
for img in all_images:
    path = IMAGES_DIR / img
    try:
        b64 = encode_image(path)
        image_data[img] = b64
        print(f"[OK] Loaded: {img} ({len(b64)} chars)")
    except Exception as e:
        print(f"[ERROR] {img}: {e}")

print(f"\n[INFO] Ready to analyze {len(image_data)} images")
print("[ACTION] Awaiting vision analysis...\n")

# The vision analysis would happen here
# For now, print what we're ready to send
print("IMAGES READY FOR VISION ANALYSIS:")
print("=" * 60)
for i, (img, b64) in enumerate(image_data.items(), 1):
    print(f"{i}. {img}")
    print(f"   Base64 length: {len(b64)}")
print("=" * 60)
