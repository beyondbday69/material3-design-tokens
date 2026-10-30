# Components: lists, data and feedback

Source: Material Web component tokens v0.192 (generated from the M3 spec). Sizes in dp. Shape names map to the shape scale in [shape.md](shape.md); `full` = fully rounded. Expressive-era components are not covered: check m3.material.io for those.

## Lists, data and feedback

| Component | Size | Notes |
|---|---|---|
| List item | 56 (1 line), 72 (2 lines), 88 (3 lines) | leading/trailing space 16; avatar 40; icon 24; image 56x56; video 100x56 |
| Data table | header 56, row 52, footer 52 | 1 outline; container extra-small (4) |
| Circular progress (flat / wavy) | 40 / 48, stroke 4, gap 4 | see [components-slider-progress.md](components-slider-progress.md) |
| Linear progress (flat / wavy) | 4 high / 10 high, gap 4, stop 4 | see [components-slider-progress.md](components-slider-progress.md) |
| Banner | mobile 54 (1 line), 112 (2 lines); desktop 52 (1 line) | shape none; image 40 |
| Date picker modal | 360x568 | shape extra-large (28); day cell 40 |
| Date picker docked | 360x456 | shape large (16); day cell 48 |
| Time picker | clock dial 256, container shape extra-large (28) | selector handle 48 |


## Component state rules

- Disabled container opacity 0.12, disabled label/content opacity 0.38.
- Buttons: hover raises elevated/filled by one level (filled hover = level 1), pressed returns to level 0.
- Label text on buttons and chips uses Label Large (14/20, weight 500).
- Keep 48x48dp touch targets even when the visual is smaller (chips 32, switches, checkboxes).
