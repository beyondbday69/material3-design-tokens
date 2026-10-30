---
name: material3-design-tokens
description: Reference of Material Design 3 (M3, Material You, M3 Expressive) design tokens - motion (duration, easing, springs), shape, elevation, state layers, typography scale, window size classes, spacing and touch targets. Use this skill whenever the user mentions Material 3, Material You, m3.material.io, md.sys tokens, Material animation/easing/duration values, Material Expressive springs, or asks for CSS, Compose, Flutter, or Android values that follow Material guidelines, even if they don't say "tokens". Also use when building UI that should "feel like Material" and needs concrete numbers.
---

# Material 3 Design Tokens

Concrete values for building M3-consistent UI. Prefer these over guessing. m3.material.io is JavaScript-rendered, so if the user needs newer or exact values, web search for implementations (Flutter `gen_defaults`, Material Web, Compose) or tell them to verify at m3.material.io/styles/motion.

Spring values and `emphasized` curve details are from memory/implementations: flag them as "verify against the spec" if precision matters.

## Motion: duration tokens (`md.sys.motion.duration.*`)

| Token | ms | Token | ms |
|---|---|---|---|
| short1 | 50 | long1 | 450 |
| short2 | 100 | long2 | 500 |
| short3 | 150 | long3 | 550 |
| short4 | 200 | long4 | 600 |
| medium1 | 250 | extra-long1 | 700 |
| medium2 | 300 | extra-long2 | 800 |
| medium3 | 350 | extra-long3 | 900 |
| medium4 | 400 | extra-long4 | 1000 |

## Motion: easing tokens (`md.sys.motion.easing.*`)

```css
--md-sys-motion-easing-linear: cubic-bezier(0, 0, 1, 1);
--md-sys-motion-easing-standard: cubic-bezier(0.2, 0, 0, 1);
--md-sys-motion-easing-standard-decelerate: cubic-bezier(0, 0, 0, 1);
--md-sys-motion-easing-standard-accelerate: cubic-bezier(0.3, 0, 1, 1);
--md-sys-motion-easing-emphasized: path("M0,0 C0.05,0 0.133,0.06 0.166,0.4 C0.208,0.82 0.208,1 1,1");
--md-sys-motion-easing-emphasized-decelerate: cubic-bezier(0.05, 0.7, 0.1, 1);
--md-sys-motion-easing-emphasized-accelerate: cubic-bezier(0.3, 0, 0.8, 0.15);
```

`emphasized` is a two-segment spline. Native (Android/Flutter) can use it directly. On the web use the `path()` form where supported (e.g. `linear()` or `path()` in newer browsers), otherwise approximate with `cubic-bezier(0.2, 0, 0, 1)`.

## Motion: M3 Expressive springs

| Spring | Stiffness | Damping ratio | Use |
|---|---|---|---|
| spatial fast | 1400 | 0.9 | small position/size/shape changes |
| spatial default | 700 | 0.9 | most spatial motion |
| spatial slow | 300 | 0.9 | large, full-screen movement |
| effects fast | 3800 | 1.0 | color/opacity, quick |
| effects default | 1600 | 1.0 | color/opacity |
| effects slow | 800 | 1.0 | color/opacity, gentle |

Spatial springs (position, size, shape morph) overshoot slightly; effects springs (color, opacity) never overshoot.

## Motion: rules of thumb

- Small elements (switch, icon swap, ripple): short2-short4 (100-200ms)
- Cards, menus, FAB morph, dialogs: medium1-medium3 (250-350ms)
- Page and full-screen transitions: long1-long2 (450-500ms)
- Entering the screen: decelerate easing. Leaving: accelerate. Moving within screen: standard/emphasized.
- Exit animations are usually shorter than enter animations.
- Transition patterns: container transform, shared axis (X/Y/Z), fade through, fade.

## Shape (corner radius)

None 0 / Extra-small 4 / Small 8 / Medium 12 / Large 16 / Extra-large 28 / Full 50% (dp)

## State layer opacity

Hover 0.08, Focus 0.10, Pressed 0.10, Dragged 0.16. Disabled: content 0.38, container 0.12.

## Elevation

Level 0: 0dp, Level 1: 1dp, Level 2: 3dp, Level 3: 6dp, Level 4: 8dp, Level 5: 12dp

## Typography scale (size / line height, sp)

| Role | Large | Medium | Small |
|---|---|---|---|
| Display | 57/64 | 45/52 | 36/44 |
| Headline | 32/40 | 28/36 | 24/32 |
| Title | 22/28 | 16/24 | 14/20 |
| Body | 16/24 | 14/20 | 12/16 |
| Label | 14/20 | 12/16 | 11/16 |

## Window size classes (dp width)

Compact < 600, Medium 600-839, Expanded 840-1199, Large 1200-1599, Extra-large 1600+

## Layout and sizing

- Minimum touch target 48x48dp
- Layout margins 16dp (compact), 24dp (larger)
- 4dp base grid, 8dp is the common step

## Components (dimensions, shape, icon sizes)

Source: Material Web component tokens v0.192 (generated from the M3 spec). Sizes in dp/px. Shape names map to the shape scale above (`full` = fully rounded). Expressive-era components (button groups, split buttons, loading indicator, new sizes) are not covered: check m3.material.io for those.

### Buttons and actions

| Component | Height | Shape | Icon | Notes |
|---|---|---|---|---|
| Filled / tonal / elevated / outlined / text button | 40 | full | 18 | outlined has 1 outline |
| Icon button (all variants) | 40 state layer | full | 24 | outlined: 1 outline; min touch 48 |
| Segmented button (outlined) | 40 | full | 18 | 1 outline |
| FAB small | 40x40 | medium (12) | 24 | |
| FAB | 56x56 | large (16) | 24 | |
| FAB large | 96x96 | extra-large (28) | 36 | |
| Extended FAB | 56 | large (16) | 24 | |
| Chip (assist / filter / input / suggestion) | 32 | small (8) | 18 | 1 outline; input avatar 24 |

### Containment

| Component | Size | Shape | Notes |
|---|---|---|---|
| Card (elevated / filled / outlined) | content | medium (12) | outlined: 1 outline |
| Dialog | content | extra-large (28) | icon 24 |
| Full-screen dialog | full | none | header 56 |
| Bottom sheet (docked) | full width | extra-large top (28) | drag handle 32x4 |
| Side sheet | docked 256 wide, 100% high | none (modal: large-start 16) | detached: large (16) |
| Menu | content | extra-small (4) | item height 48 |
| Snackbar | 48 (one line), 68 (two lines) | extra-small (4) | icon 24 |
| Plain tooltip | content | extra-small (4) | |
| Rich tooltip | content | medium (12) | |
| Carousel item | content | extra-large (28) | |
| Divider | 1 thick | n/a | |
| Badge | small 6, large 16 | full | |

### Navigation

| Component | Size | Indicator | Icon |
|---|---|---|---|
| Top app bar (small) | 64 | n/a | 24 |
| Top app bar (medium) | 112 | n/a | 24 |
| Top app bar (large) | 152 | n/a | 24 |
| Bottom app bar | 80 | n/a | 24 |
| Navigation bar | 80 | 64x32, full | 24 |
| Navigation rail | 80 wide | 56x32, full (no label: 56x56) | 24 |
| Navigation drawer | 360 wide, container shape large-end (16) | 336x56, full | 24 |
| Primary tab | 48 (64 with icon + label) | 3 high | 24 |
| Secondary tab | 48 | 2 high | 24 |
| Search bar | 56 | full | avatar 30 |
| Search view | docked header 56 (shape extra-large 28); full-screen header 72 | | |

### Inputs and selection

| Component | Size | Shape | Notes |
|---|---|---|---|
| Filled text field | 56 typical | extra-small top (4) | indicator 1 (focus 2); icons 24 |
| Outlined text field | 56 typical | extra-small (4) | outline 1 (focus 2); icons 24 |
| Select / autocomplete | same as text field | menu: extra-small (4) | menu item 48 |
| Checkbox | 18 box, 40 state layer | 2 box radius | unselected outline 2 |
| Radio | 20 icon, 40 state layer | full | |
| Switch | track 52x32, outline 2 | full | handle: 16 off, 24 on/with icon, 28 pressed; icon 16 |
| Slider | track 4, handle 20, state layer 40 | full | value label 28 high; tick 2 |

### Lists, data and feedback

| Component | Size | Notes |
|---|---|---|
| List item | 56 (1 line), 72 (2 lines), 88 (3 lines) | leading/trailing space 16; avatar 40; icon 24; image 56x56; video 100x56 |
| Data table | header 56, row 52, footer 52 | 1 outline; container extra-small (4) |
| Circular progress | 48, stroke 4 | |
| Linear progress | 4 high | track and indicator shape none |
| Banner | mobile 54 (1 line), 112 (2 lines); desktop 52 (1 line) | shape none; image 40 |
| Date picker modal | 360x568 | shape extra-large (28); day cell 40 |
| Date picker docked | 360x456 | shape large (16); day cell 48 |
| Time picker | clock dial 256, container shape extra-large (28) | selector handle 48 |

### Component state rules

- Disabled container opacity 0.12, disabled label/content opacity 0.38.
- Buttons: hover raises elevated/filled by one level (filled hover = level 1), pressed returns to level 0.
- Label text on buttons and chips uses Label Large (14/20, weight 500).
- Keep 48x48dp touch targets even when the visual is smaller (chips 32, switches, checkboxes).

## How to apply

1. Pick the token, not a raw number, when the target platform has token names (CSS custom properties, Compose `MotionTokens`, Flutter `Durations`/`Easing`).
2. When emitting code, output the full token block the user needs (CSS variables, Kotlin object, or Dart constants) rather than a prose list.
3. Keep spatial and effects motion separate: use spatial springs/emphasized easing for movement, effects springs or standard easing for opacity and color.
4. For component sizes, use the Components tables above. If the user asks for something not covered here (color roles, dynamic color/HCT, Expressive-only components), web search m3.material.io and implementations rather than inventing values.
