# Shape (corner radius)

Token prefix: `md.sys.shape.corner.*`

| Token | Radius (dp) | Typical use |
|---|---|---|
| none | 0 | full-screen surfaces, app bars, nav bar |
| extra-small | 4 | menus, snackbars, tooltips, text field top corners |
| small | 8 | chips |
| medium | 12 | cards, small FABs, rich tooltips |
| large | 16 | FABs, extended FABs, drawers, date picker docked |
| extra-large | 28 | dialogs, bottom sheets, large FABs, search view |
| full | 50% | buttons, switch, badges, icon button state layers |

```css
:root {
  --md-sys-shape-corner-none: 0;
  --md-sys-shape-corner-extra-small: 4px;
  --md-sys-shape-corner-small: 8px;
  --md-sys-shape-corner-medium: 12px;
  --md-sys-shape-corner-large: 16px;
  --md-sys-shape-corner-extra-large: 28px;
  --md-sys-shape-corner-full: 9999px;
}
```

Asymmetric variants exist: `extra-small-top`, `large-top`, `large-end`, `large-start`, `extra-large-top` (round only those corners).
