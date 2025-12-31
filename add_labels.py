import json

with open(r'c:\Users\atuan\work\NailSite\scripts\nail_labels.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

new_labels = [
    {
        'filename': '1548.jpg',
        'shape': 'Almond',
        'length': 'Medium',
        'color': ['Pink', 'Nude'],
        'color_scheme': 'Solid',
        'finish': ['Glossy'],
        'complexity': 'Minimal',
        'french_tip': 'None',
        'set_style': 'Uniform',
        'art_type': ['None'],
        'embellishments': ['None'],
        'vibe': ['Natural', 'Elegant', 'Minimalist']
    },
    {
        'filename': '1549.jpg',
        'shape': 'Almond',
        'length': 'Long',
        'color': ['Nude', 'Beige', 'Gold'],
        'color_scheme': 'Duo',
        'finish': ['Glossy'],
        'complexity': 'Minimal',
        'french_tip': 'Colored',
        'set_style': 'Uniform',
        'art_type': ['None'],
        'embellishments': ['None'],
        'vibe': ['Elegant', 'Glamorous']
    },
    {
        'filename': '1550.jpg',
        'shape': 'Square',
        'length': 'Short',
        'color': ['Black'],
        'color_scheme': 'Solid',
        'finish': ['Glossy'],
        'complexity': 'Minimal',
        'french_tip': 'None',
        'set_style': 'Uniform',
        'art_type': ['None'],
        'embellishments': ['None'],
        'vibe': ['Edgy', 'Bold']
    },
    {
        'filename': '1551.jpg',
        'shape': 'Coffin',
        'length': 'Long',
        'color': ['Pink', 'White'],
        'color_scheme': 'Duo',
        'finish': ['Glossy', 'Shimmer'],
        'complexity': 'Minimal',
        'french_tip': 'None',
        'set_style': 'Uniform',
        'art_type': ['Ombre'],
        'embellishments': ['None'],
        'vibe': ['Elegant', 'Glamorous', 'Romantic']
    }
]

data['labels'].extend(new_labels)

with open(r'c:\Users\atuan\work\NailSite\scripts\nail_labels.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print(f"Added {len(new_labels)} labels. Total labels: {len(data['labels'])}")
