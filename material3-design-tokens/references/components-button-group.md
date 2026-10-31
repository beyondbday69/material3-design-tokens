# Button group (M3 Expressive)

An invisible container that spaces buttons and changes their shape and width on interaction. **When one button is pressed it grows and its neighbors compress**, so the total group width stays the same. Works with all button and icon button sizes (XS to XL).

Sources: Compose Material3 (`ButtonGroup.kt`, `ButtonGroupDefaults`, button size tokens) and Material Components Android `MaterialButtonGroup`. Sizes in dp.

## Two types

| Type | Spacing | Shape | Press behavior |
|---|---|---|---|
| Standard | 12 (`ButtonGroupSmallTokens.BetweenSpace`) | each button keeps its own shape (round or square) | pressed button grows 15%, neighbors compress, pressed shape morphs |
| Connected | 2 | outer corners full, inner corners 8 (small) | pressed inner corners 4 (extra-small), selected inner corners 50% (toggle) |

## Press expansion rule

| Rule | Value |
|---|---|
| Expanded ratio | 0.15 of the pressed button's width (`ButtonGroupDefaults.ExpandedRatio`; Android `childSizeChange` 15%) |
| Edge button pressed | pressed grows by `min(0.15 × width, neighbor limit)`; its one neighbor shrinks by the same amount |
| Middle button pressed | pressed grows by `0.15 × width` in total; each neighbor shrinks by half of it (`0.15 × width / 2`) |
| Neighbor limit | a neighbor never shrinks by more than its end content padding (16 for XS/S, 24 for M, 48 for L, 64 for XL) or its own width |
| Total group width | unchanged (growth equals compression) |
| Animation | fast spatial spring: Standard 1400 / 0.9, Expressive 800 / 0.6 (see [motion.md](motion.md)) |
| Shape on press | round (full) morphs to the size's pressed shape (below), together with the width change |

Worked example (size S, widths 80, 76, 96, 80, spacing 12), press the second button: it grows 76 to 87.4, the first shrinks 80 to 74.3, the third shrinks 96 to 90.3. Press the first button: it grows 80 to 92 and the second shrinks 76 to 64.

## Button sizes (apply to every button in the group)

| Size | Height | Icon | Leading / trailing space | Icon-label space | Round shape | Square shape | Pressed shape | Outline |
|---|---|---|---|---|---|---|---|---|
| XS | 32 | 20 | 16 | 8 | full | medium (12) | small (8) | 1 |
| S | 40 | 20 | 16 | 8 | full | medium (12) | small (8) | 1 |
| M | 56 | 24 | 24 | 8 | full | large (16) | medium (12) | 1 |
| L | 96 | 32 | 48 | 12 | full | extra-large (28) | large (16) | 2 |
| XL | 136 | 40 | 64 | 16 | full | extra-large (28) | large (16) | 3 |

Selected (toggle) buttons swap between the round and square shape.

<!-- the animated example lives in the repo README (assets/button-group.svg) -->

## Overflow

Android `overflowMode` moves children that do not fit into a menu behind an overflow icon button (default 3 dots). Compose: `ButtonGroup(overflowIndicator = { menuState -> ... })`.

## Compose

```kotlin
ButtonGroup(
    overflowIndicator = { menuState -> /* overflow icon button */ },
) {
    val interaction = remember { MutableInteractionSource() }
    clickableItem(onClick = { /* ... */ }, label = "Week")        // simple item
    customItem(
        buttonGroupContent = {
            Button(
                onClick = { },
                modifier = Modifier.animateWidth(interaction),     // grows when pressed, neighbors compress
                interactionSource = interaction,
            ) { Text("Month") }
        },
        menuContent = { /* overflow menu entry */ },
    )
}

// Connected: ConnectedButtonGroup with ToggleButton shapes
// ButtonGroupDefaults.connectedLeadingButtonShapes() / connectedMiddleButtonShapes() / connectedTrailingButtonShapes()
```

## Android views

```xml
<com.google.android.material.button.MaterialButtonGroup
    style="@style/Widget.Material3Expressive.MaterialButtonGroup"
    android:spacing="12dp"
    app:childSizeChange="15%" />

<!-- connected: 2dp spacing, 8dp inner corners, fully rounded outer corners -->
<com.google.android.material.button.MaterialButtonGroup
    style="@style/Widget.Material3Expressive.MaterialButtonGroup.Connected" />
```

## CSS / JS

Plain CSS cannot make the neighbors compress by exactly the pressed growth, so compute widths on pointer events and let CSS animate them.

```css
.md-button-group { display: flex; gap: 12px; }                 /* connected: gap 2px */
.md-button-group > .md-btn {
  flex: none; border-radius: 9999px;
  transition: width 120ms cubic-bezier(0.34, 1.3, 0.64, 1),     /* approximates the fast spatial spring */
              border-radius 120ms cubic-bezier(0.34, 1.3, 0.64, 1);
}
.md-button-group > .md-btn[data-pressed] { border-radius: 8px; }  /* size S pressed shape */
```

```js
function enableButtonGroup(group, ratio = 0.15) {
  const btns = [...group.children];
  const base = btns.map(b => b.getBoundingClientRect().width);
  const limit = b => parseFloat(getComputedStyle(b).paddingRight) || 16;     // end padding
  btns.forEach(b => (b.style.width = b.getBoundingClientRect().width + 'px'));
  const set = (i, pressed) => {
    btns.forEach((b, j) => { b.style.width = base[j] + 'px'; b.toggleAttribute('data-pressed', false); });
    if (!pressed || btns.length < 2) return;
    const last = btns.length - 1, w = base[i];
    if (i > 0 && i < last) {
      const g = Math.min(ratio * w / 2, limit(btns[i - 1]), limit(btns[i + 1]));
      btns[i - 1].style.width = base[i - 1] - g + 'px';
      btns[i + 1].style.width = base[i + 1] - g + 'px';
      btns[i].style.width = w + 2 * g + 'px';
    } else {
      const n = i === 0 ? 1 : i - 1;
      const g = Math.min(ratio * w, limit(btns[n]), base[n]);
      btns[n].style.width = base[n] - g + 'px';
      btns[i].style.width = w + g + 'px';
    }
    btns[i].setAttribute('data-pressed', '');
  };
  btns.forEach((b, i) => {
    b.addEventListener('pointerdown', () => set(i, true));
    ['pointerup', 'pointerleave', 'pointercancel'].forEach(e => b.addEventListener(e, () => set(i, false)));
  });
}
```
