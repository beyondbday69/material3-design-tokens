# Component motion recipes

What animates on each component, with which duration and easing token, plus drop-in CSS. Tokens come from [motion.md](motion.md). Spring-like overshoot is approximated on the web with `cubic-bezier(0.34, 1.56, 0.64, 1)` (use real springs on Compose/Flutter).

Per-component timings below are recommended defaults built from the M3 rules of thumb (small = short, containers = medium, full screen = long; enter decelerates, exit accelerates and is shorter). Verify against m3.material.io for exact spec values.

```css
:root {
  --md-sys-motion-duration-short2: 100ms;
  --md-sys-motion-duration-short3: 150ms;
  --md-sys-motion-duration-short4: 200ms;
  --md-sys-motion-duration-medium1: 250ms;
  --md-sys-motion-duration-medium2: 300ms;
  --md-sys-motion-duration-medium3: 350ms;
  --md-sys-motion-duration-long2: 500ms;
  --md-sys-motion-easing-standard: cubic-bezier(0.2, 0, 0, 1);
  --md-sys-motion-easing-emphasized-decelerate: cubic-bezier(0.05, 0.7, 0.1, 1);
  --md-sys-motion-easing-emphasized-accelerate: cubic-bezier(0.3, 0, 0.8, 0.15);
  --md-sys-motion-spring-spatial: cubic-bezier(0.34, 1.56, 0.64, 1);
}
```

## Summary

| Component | What animates | Duration | Easing |
|---|---|---|---|
| Button | state layer opacity, ripple | short2 (state), medium2 (ripple) | standard |
| Switch | handle size 16/28/24, position, track color | short4 | spatial spring / standard |
| Checkbox | fill, check stroke draw | short4 | standard |
| Filter chip | container fill, check icon, label shift | medium1 | standard |
| Slider (Expressive) | handle width 4 to 2 when pressed, active/inactive track resize, value indicator | short2 | standard |
| Text field | label float + scale, outline 1 to 2dp | medium1 | standard |
| Dialog | scrim fade, container scale + fade | enter medium3, exit short4 | emphasized-decelerate / accelerate |
| Menu | container scaleY from anchor, items fade | enter medium1, exit short2 | emphasized-decelerate |
| Bottom sheet | translateY, scrim | enter long2, exit medium2 | emphasized-decelerate / accelerate |
| Snackbar | translateY + fade in, fade out | enter medium1, exit short2 | emphasized-decelerate |
| Card | elevation, state layer | short3 | standard |
| FAB (extended) | width morph, label fade | medium3 | emphasized |
| Navigation bar | indicator scaleX, icon color | medium1 | emphasized-decelerate |
| Tabs | indicator slide, label color | medium1 | standard |
| Shared axis X | translateX 30dp + fade | out short2 (90ms), in 210ms | accelerate / decelerate |
| Container transform | bounds + radius morph, content crossfade | long2 | emphasized |
| Progress (wavy) | wave travels 1 wavelength/s, amplitude ramps 0 to full between 10% and 95%, determinate change | ramp long2, change long2 | standard / linear |
| Progress (flat, indeterminate) | bars or arc loop | 1.4 to 2 s | standard |

## Button

```css
.md-button { position: relative; overflow: hidden; }
.md-button::before { /* state layer */
  content: ""; position: absolute; inset: 0; background: currentColor; opacity: 0;
  transition: opacity var(--md-sys-motion-duration-short2) linear;
}
.md-button:hover::before { opacity: 0.08; }
.md-button:focus-visible::before { opacity: 0.10; }
.md-button:active::before { opacity: 0.10; }
```

## Switch

```css
.md-switch__handle {
  width: 16px; height: 16px;
  transition: transform var(--md-sys-motion-duration-short4) var(--md-sys-motion-spring-spatial),
              background-color var(--md-sys-motion-duration-short4) var(--md-sys-motion-easing-standard);
}
.md-switch:active .md-switch__handle { transform: scale(1.75); }          /* 28dp pressed */
.md-switch[aria-checked="true"] .md-switch__handle { transform: translateX(20px) scale(1.5); } /* 24dp */
.md-switch[aria-checked="true"] .md-switch__track { background: var(--md-sys-color-primary); }
```

## Checkbox

```css
.md-checkbox__mark { stroke-dasharray: 14; stroke-dashoffset: 14;
  transition: stroke-dashoffset var(--md-sys-motion-duration-short4) var(--md-sys-motion-easing-standard); }
.md-checkbox:checked ~ svg .md-checkbox__mark { stroke-dashoffset: 0; }
```

## Text field (outlined)

```css
.md-field__label {
  transform-origin: left center;
  transition: transform var(--md-sys-motion-duration-medium1) var(--md-sys-motion-easing-standard),
              color var(--md-sys-motion-duration-medium1) var(--md-sys-motion-easing-standard);
}
.md-field:focus-within .md-field__label,
.md-field--filled .md-field__label { transform: translateY(-30px) scale(0.75); } /* 16sp to 12sp */
.md-field:focus-within .md-field__outline { border-width: 2px; border-color: var(--md-sys-color-primary); }
```

## Dialog

```css
.md-scrim   { opacity: 0; transition: opacity var(--md-sys-motion-duration-medium3) linear; }
.md-dialog  { opacity: 0; transform: scale(0.8);
  transition: opacity var(--md-sys-motion-duration-short4), transform var(--md-sys-motion-duration-short4);
  transition-timing-function: var(--md-sys-motion-easing-emphasized-accelerate); }  /* exit */
.md-dialog[open] { opacity: 1; transform: scale(1);
  transition-duration: var(--md-sys-motion-duration-medium3);
  transition-timing-function: var(--md-sys-motion-easing-emphasized-decelerate); }  /* enter */
.md-dialog[open] ~ .md-scrim { opacity: 0.32; }
```

## Menu

```css
.md-menu { transform-origin: top left; opacity: 0; transform: scaleY(0.3);
  transition: transform var(--md-sys-motion-duration-medium1) var(--md-sys-motion-easing-emphasized-decelerate),
              opacity var(--md-sys-motion-duration-short2) linear; }
.md-menu[open] { opacity: 1; transform: scaleY(1); }
```

## Bottom sheet

```css
.md-sheet { transform: translateY(100%);
  transition: transform var(--md-sys-motion-duration-medium2) var(--md-sys-motion-easing-emphasized-accelerate); }
.md-sheet[open] { transform: translateY(0);
  transition: transform var(--md-sys-motion-duration-long2) var(--md-sys-motion-easing-emphasized-decelerate); }
```

## Snackbar

```css
@keyframes md-snack-in { from { opacity: 0; transform: translateY(24px); } }
.md-snackbar { animation: md-snack-in var(--md-sys-motion-duration-medium1) var(--md-sys-motion-easing-emphasized-decelerate); }
.md-snackbar[data-leaving] { opacity: 0; transition: opacity var(--md-sys-motion-duration-short2) linear; }
```

## Card (elevated)

```css
.md-card { box-shadow: 0 1px 3px rgb(0 0 0 / .3), 0 1px 2px rgb(0 0 0 / .15);        /* level 1 */
  transition: box-shadow var(--md-sys-motion-duration-short3) var(--md-sys-motion-easing-standard); }
.md-card:hover { box-shadow: 0 2px 6px rgb(0 0 0 / .3), 0 1px 2px rgb(0 0 0 / .15); } /* level 2 */
```

## Extended FAB

```css
.md-fab { width: 56px; transition: width var(--md-sys-motion-duration-medium3) var(--md-sys-motion-easing-emphasized-decelerate); overflow: hidden; }
.md-fab--extended { width: 150px; }
.md-fab__label { opacity: 0; transition: opacity var(--md-sys-motion-duration-short3) linear; }
.md-fab--extended .md-fab__label { opacity: 1; transition-delay: var(--md-sys-motion-duration-short3); }
```

## Navigation bar indicator

```css
.md-nav__indicator { transform: scaleX(0); transition: transform var(--md-sys-motion-duration-medium1) var(--md-sys-motion-easing-emphasized-decelerate); }
.md-nav__item[aria-current="page"] .md-nav__indicator { transform: scaleX(1); } /* 64x32, grows from center */
```

## Tabs

```css
.md-tabs__indicator { height: 3px; border-radius: 3px 3px 0 0;
  transition: transform var(--md-sys-motion-duration-medium1) var(--md-sys-motion-easing-standard),
              width var(--md-sys-motion-duration-medium1) var(--md-sys-motion-easing-standard); }
```

## Transitions

Shared axis X (forward). Reverse the signs for back navigation.

```css
@keyframes md-axis-out { to   { opacity: 0; transform: translateX(-30px); } }
@keyframes md-axis-in  { from { opacity: 0; transform: translateX(30px); } }
.page-leave { animation: md-axis-out 90ms  var(--md-sys-motion-easing-emphasized-accelerate) forwards; }
.page-enter { animation: md-axis-in  210ms 90ms var(--md-sys-motion-easing-emphasized-decelerate) backwards; }
```

Container transform: animate the card's box (position, size, radius) into the destination box while the card content fades out and the page content fades in. On the web use the View Transitions API with a shared `view-transition-name`:

```css
.card.open  { view-transition-name: hero; }
::view-transition-group(hero) {
  animation-duration: var(--md-sys-motion-duration-long2);
  animation-timing-function: var(--md-sys-motion-easing-standard);
}
```

Fade through: outgoing fades out in 90ms, incoming fades in and scales from 0.92 to 1 over 210ms.

## Slider (Expressive)

Full spec in [components-slider-progress.md](components-slider-progress.md).

```css
.md-slider__handle { width: 4px; transition: width var(--md-sys-motion-duration-short2) var(--md-sys-motion-easing-standard); }
.md-slider__handle:active, .md-slider__handle:focus-visible { width: 2px; }  /* pressed/focused handle narrows */
.md-slider__active, .md-slider__inactive { transition: width 0s; }           /* track follows the handle with no lag */
```

## Wavy progress

On the web draw the active part as an SVG path of a sine wave (amplitude 3, wavelength 40 for linear; amplitude 1.6, wavelength 15 for circular) and shift its phase at 1 wavelength per second. Fade the amplitude to 0 below 10% and above 95% progress over long2.

```css
@keyframes md-wave { to { transform: translateX(-40px); } }   /* one wavelength */
.md-linear-wavy__active { animation: md-wave 1s linear infinite; }
.md-linear-wavy { clip-path: inset(0 var(--remaining, 40%) 0 0 round 2px); }
```

## Progress (flat, indeterminate)

```css
@keyframes md-spin { to { transform: rotate(360deg); } }
@keyframes md-dash {
  0%   { stroke-dasharray: 6 107;  stroke-dashoffset: 0; }
  50%  { stroke-dasharray: 72 41;  stroke-dashoffset: -22; }
  100% { stroke-dasharray: 6 107;  stroke-dashoffset: -113; }
}
.md-circular       { animation: md-spin 1.6s linear infinite; }
.md-circular circle { stroke-width: 4; stroke-linecap: round; fill: none; animation: md-dash 1.6s var(--md-sys-motion-easing-standard) infinite; }
```
