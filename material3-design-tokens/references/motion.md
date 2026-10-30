# Motion tokens

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
