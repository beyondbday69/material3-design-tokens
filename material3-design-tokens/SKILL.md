---
name: material3-design-tokens
description: Reference of Material Design 3 (M3, Material You, M3 Expressive) design tokens - motion (duration, easing, springs), shape, elevation, state layers, typography scale, window size classes, spacing, touch targets and component dimensions and component motion recipes (buttons, FABs, chips, cards, dialogs, navigation, text fields, switch, Expressive slider, flat and wavy progress indicators, button groups, lists, pickers). Use this skill whenever the user mentions Material 3, Material You, m3.material.io, md.sys or md.comp tokens, Material animation/easing/duration values, Material Expressive springs, or asks for CSS, Compose, Flutter, or Android values that follow Material guidelines, even if they don't say "tokens". Also use when building UI that should "feel like Material" and needs concrete numbers.
---

# Material 3 Design Tokens

Concrete values for building M3-consistent UI. Prefer these over guessing. This file is an index: read only the reference file(s) the task needs.

m3.material.io is JavaScript-rendered, so for newer or exact values, web search implementations (Flutter `gen_defaults`, Material Web, Compose) or tell the user to verify at m3.material.io.

## Which file to read

| Need | Read |
|---|---|
| Duration, easing, springs, transition rules | [references/motion.md](references/motion.md) |
| Corner radius scale | [references/shape.md](references/shape.md) |
| Hover/focus/pressed opacity, elevation levels | [references/state-and-elevation.md](references/state-and-elevation.md) |
| Type scale (Display to Label) | [references/typography.md](references/typography.md) |
| Window size classes, margins, touch targets, grid | [references/layout.md](references/layout.md) |
| Buttons, icon buttons, FABs, chips | [references/components-actions.md](references/components-actions.md) |
| Cards, dialogs, sheets, menus, snackbar, tooltips, badge | [references/components-containment.md](references/components-containment.md) |
| App bars, navigation bar/rail/drawer, tabs, search | [references/components-navigation.md](references/components-navigation.md) |
| Text fields, select, checkbox, radio, switch, slider | [references/components-inputs.md](references/components-inputs.md) |
| Lists, data table, progress, banner, pickers | [references/components-lists-feedback.md](references/components-lists-feedback.md) |
| Button group (press grows a button, neighbors compress), button sizes XS to XL | [references/components-button-group.md](references/components-button-group.md) |
| Slider (XS to XL, pill handle, gap) and progress indicators (flat and wavy) | [references/components-slider-progress.md](references/components-slider-progress.md) |
| How each component animates (timings, easing, CSS recipes) | [references/component-motion.md](references/component-motion.md) |

## How to apply

1. Read only the matching reference file(s), not all of them.
2. Pick the token, not a raw number, when the target platform has token names (CSS custom properties, Compose `MotionTokens`, Flutter `Durations`/`Easing`).
3. When emitting code, output the full token block the user needs (CSS variables, Kotlin object, or Dart constants) rather than a prose list.
4. Keep spatial and effects motion separate: spatial springs/emphasized easing for movement, effects springs or standard easing for opacity and color.
5. Spring values and the `emphasized` curve are from implementations: flag them as "verify against the spec" if precision matters.
6. Not covered (color roles, dynamic color/HCT, Expressive-only components): web search m3.material.io and implementations rather than inventing values.
