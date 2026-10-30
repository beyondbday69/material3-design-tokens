# State layers and elevation

## State layer opacity (`md.sys.state.*`)

| State | Opacity |
|---|---|
| Hover | 0.08 |
| Focus | 0.10 |
| Pressed | 0.10 |
| Dragged | 0.16 |

Disabled: content 0.38, container 0.12.

The state layer is an overlay in the content color (for example `on-primary` on a filled button) drawn over the container at the opacity above.

## Elevation (`md.sys.elevation.level*`)

| Level | dp |
|---|---|
| 0 | 0 |
| 1 | 1 |
| 2 | 3 |
| 3 | 6 |
| 4 | 8 |
| 5 | 12 |

Filled and elevated buttons: hover goes up one level (filled: 0 to 1), pressed returns to the resting level.
