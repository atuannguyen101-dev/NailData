# Nail Image Labeling Instructions

This document outlines the workflow for an AI agent to label nail art images using the Chrome DevTools MCP.

## Goal
Process images from the `train/` folder, extract visual features, append them to the appropriate `C:\Users\atuan\work\NailSite\scripts\trainingJson\1xxx.json`, and move the processed images to `trained/`.

## Prerequisites
- **Chrome DevTools MCP** must be installed and active.
- Access to the local file system.
- **batch_viewer.html** - HTML template for viewing multiple images at once.

## Workflow

1.  **List Files**: Get the list of images currently in the `train/` directory.
2.  **Process Loop (Batch of 4)**: For each batch of 4 image files, you must do it batch-by-batch only next one of after previous is completed:
    a.  **Open Batch Viewer**: Use `mcp_io_github_chr_new_page` to open the batch viewer with images as URL parameters.
        *   Format: `file:///c:/Users/atuan/work/NailSite/scripts/batch_viewer.html?images=img1.jpg,img2.jpg,img3.jpg,img4.jpg`
    b.  **Capture Vision**: Use `mcp_io_github_chr_take_screenshot` to capture all 4 images at once.
    c.  **Analyze & Label**: Analyze the screenshot to determine features for ALL 4 images based on the schema in `nail_labels.json`:
        *   `shape` (e.g., Almond, Coffin, Square)
        *   `length` (e.g., Short, Medium, Long)
        *   `color` (List of colors)
        *   `color_scheme` (Solid, Duo, Multi)
        *   `finish` (Glossy, Matte, Glitter, etc.)
        *   `complexity` (Minimal, Moderate, Maximal)
        *   `french_tip` (None, Classic, etc.)
        *   `set_style` (Uniform, AccentNail, etc.)
        *   `art_type` (Floral, Geometric, etc.)
        *   `embellishments` (Crystals, Foil, etc.)
        *   `vibe` (Elegant, Cute, Edgy, etc.)
    d.  **Update Database**: Append ALL 4 new JSON objects to the `labels` array in `nail_labels.json` in one edit.
        *   *Crucial*: Ensure valid JSON syntax (commas between objects).
    e.  **Move Files**: Use `run_in_terminal` with PowerShell to move all 4 files at once.
        *   Command: `Move-Item -Path "path\img1.jpg","path\img2.jpg","path\img3.jpg","path\img4.jpg" -Destination "path\trained\"`
    f.  **Cleanup**: Close the browser page using `mcp_io_github_chr_close_page` to free up resources.

## Schema Reference
Refer to the `nail_labels.json` file for the exact allowed values for each feature field.
