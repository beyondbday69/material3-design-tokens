# Slider and progress indicators (current M3 Expressive)

Both components were redesigned in M3 Expressive. Use the Expressive specs below by default. The older 2023 look (circle handle, 4dp track, flat indicators) is listed at the end for legacy apps.

Sources: Compose Material3 tokens (`SliderTokens`, `LinearProgressIndicatorTokens`, `CircularProgressIndicatorTokens`, `WavyProgressIndicatorDefaults`), Material Components Android docs, and the M3 design kit for the slider size scale. Sizes in dp.

## Slider

Anatomy: active track, **pill handle**, **gap**, inactive track, optional stop indicators, optional inset icon, value indicator.

| Detail | Value |
|---|---|
| Handle | 4 wide pill (`corner-full`); 2 wide while pressed or focused; 4 on hover |
| Gap between handle and track | 6 (`thumbTrackGapSize`) |
| Track outer corners | by size (below); inside corners next to the gap: 2 |
| Stop indicator | 4 dot, 6 trailing space, at track end (and at each step in the stops configuration) |
| Value indicator | container `inverse-surface`, text `inverse-on-surface`, Label Large, 12 above the handle |
| Colors | active track and handle `primary`, inactive track `secondary-container`, stop `primary` |
| Disabled | active track and handle opacity 0.38, inactive track 0.12 |
| Handle elevation (Android) | 2 |

### Sizes

| Size | Track height | Handle (W×H) | Track corner | Inset icon |
|---|---|---|---|---|
| XS (default) | 16 | 4×44 | 16 (full) | no |
| S | 24 | 4×44 | 8 | no |
| M | 40 | 4×52 | 12 | yes |
| L | 56 | 4×68 | 16 | yes |
| XL | 96 | 4×108 | 28 | yes |


Compose Material3 currently ships only XS. For S to XL, set sizes yourself (Android: `Widget.Material3Expressive.Slider.Small` to `.Xlarge`). Size values come from the M3 design kit: verify against m3.material.io.

Configurations: standard (continuous), stops (discrete), centered, range selection. Orientation: horizontal or vertical. Inset icon: standard slider, M and larger.

### Compose

```kotlin
Slider(
    value = value, onValueChange = { value = it },
    track = { state ->
        SliderDefaults.Track(
            sliderState = state,
            thumbTrackGapSize = 6.dp,      // default
            trackInsideCornerSize = 2.dp,  // default
            drawStopIndicator = { /* default 4dp dot */ },
        )
    },
)
```

### CSS

```css
.md-slider { --track: 16px; --handle-h: 44px; --handle-w: 4px; --gap: 6px; }
.md-slider__active   { height: var(--track); border-radius: calc(var(--track) / 2) 2px 2px calc(var(--track) / 2); background: var(--md-sys-color-primary); }
.md-slider__inactive { height: var(--track); border-radius: 2px calc(var(--track) / 2) calc(var(--track) / 2) 2px; background: var(--md-sys-color-secondary-container); margin-inline-start: var(--gap); }
.md-slider__handle   { width: var(--handle-w); height: var(--handle-h); border-radius: 9999px; background: var(--md-sys-color-primary);
  transition: width var(--md-sys-motion-duration-short2) var(--md-sys-motion-easing-standard); }
.md-slider__handle:active, .md-slider__handle:focus-visible { width: 2px; }
.md-slider__stop { width: 4px; height: 4px; border-radius: 50%; background: var(--md-sys-color-primary); inset-inline-end: 6px; }
```

## Progress indicators

Two shapes: **flat** and **wavy**. Both have **round caps**, a **gap** between the active indicator and the track, and (linear) a **stop indicator** at the track end.


### Linear

| Detail | Flat | Wavy |
|---|---|---|
| Active thickness / track thickness | 4 / 4 | 4 / 4 |
| Container height | 4 | 10 (amplitude 3 × 2 + stroke 4) |
| Wave amplitude | n/a | 3 |
| Wavelength | n/a | 40 determinate, 20 indeterminate |
| Gap (indicator to track) | 4 | 4 |
| Stop indicator | 4 dot, 0 trailing space | same |
| Default width (Compose) | 240 | 240 |
| Thick variant | thickness 8, corner radius 4 | thickness 8, corner radius 4 |

### Circular

| Detail | Flat | Wavy |
|---|---|---|
| Size | 40 (inset 4) | 48 |
| Active thickness / track thickness | 4 / 4 | 4 / 4 |
| Wave amplitude | n/a | 1.6 |
| Wavelength | n/a | 15 |
| Gap | 4 | 4 |
| Thick variant | thickness 8, corner radius 4, size 44 | thickness 8, corner radius 4, size 52 |

### Wave behavior

| Rule | Value |
|---|---|
| Wave speed | 1 wavelength per second (default `waveSpeed = wavelength`) |
| Amplitude by progress | 0 at or below 10%, full between, 0 at or above 95% (Android ramp: 0.1 to 0.9) |
| Amplitude animation | up: long2 (500ms) standard; down: long2 emphasized-accelerate |
| Determinate progress change | long2 (500ms), linear |
| Indeterminate | same wave, loops; stop indicator hidden |

Wavy makes long waits feel less static. Wavy linear is taller than flat, so reserve the 10dp container height to avoid layout shift. Use flat for dense lists and small spaces.

### Compose

```kotlin
LinearWavyProgressIndicator(progress = { progress })            // determinate
LinearWavyProgressIndicator()                                   // indeterminate
CircularWavyProgressIndicator(progress = { progress })
LinearProgressIndicator(progress = { progress })                // flat, with gap + stop indicator
```

### Android views

```xml
<com.google.android.material.progressindicator.LinearProgressIndicator
    style="@style/Widget.Material3Expressive.LinearProgressIndicator.Wavy"
    app:trackThickness="8dp" app:trackCornerRadius="4dp" />
```

Attributes: `wavelength`, `waveAmplitude`, `waveSpeed`, `indicatorTrackGapSize` (default 4dp), `trackStopIndicatorSize` (default 4dp).

## Legacy (M3 2023, pre-Expressive)

| Component | Spec |
|---|---|
| Slider | track 4, circle handle 20, handle state layer 40, value label 28 high, tick 2, no gap, no stop indicator |
| Linear progress | 4 high, no gap, no stop indicator, shape none (square ends) |
| Circular progress | 48, stroke 4, no track |
