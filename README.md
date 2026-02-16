# scope-color-test

Simple color overlay/blend test plugin for Daydream Scope.

## What it does

Blends a solid color with input video using RGBA controls. Perfect for testing the plugin system and understanding basic video processing.

## Installation

### From Git (for sharing)

```bash
# In Scope Settings > Plugins, install from:
git+https://github.com/andrwsun/scope-color-test.git
```

### Local Development

```bash
# In Scope Settings > Plugins, browse to:
/Users/andrew/Desktop/scope local/scope-color-test
```

Click **Install** and Scope will restart with the plugin loaded.

## Parameters

| Parameter | Type | Range | Default | Description |
|-----------|------|-------|---------|-------------|
| Red | Float | 0.0 - 1.0 | 1.0 | Red channel value |
| Green | Float | 0.0 - 1.0 | 1.0 | Green channel value |
| Blue | Float | 0.0 - 1.0 | 1.0 | Blue channel value |
| Alpha | Float | 0.0 - 1.0 | 0.5 | Blend amount (0 = original, 1 = full color) |

All parameters are **runtime** - adjust them live during streaming!

## Usage

1. Connect a video source (camera or file)
2. Select **Color Test** from the pipeline dropdown
3. Adjust RGB sliders to pick your color
4. Use Alpha to control how much it blends with the original video

## Development

After editing the code:
1. Go to Settings > Plugins
2. Click **Reload** next to "scope-color-test"
3. Changes take effect immediately (no reinstall needed)

## How it works

```python
# Blending formula
result = original_video * (1 - alpha) + solid_color * alpha
```

- `alpha = 0.0`: Shows 100% original video
- `alpha = 0.5`: 50/50 mix
- `alpha = 1.0`: Shows 100% solid color
