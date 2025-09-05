import matplotlib

# Force backend BEFORE pyplot (only if necessary)
matplotlib.use('TkAgg')   # optional, remove if your default backend works

import matplotlib.pyplot as plt

# Show available styles
print("Available styles:", plt.style.available)

# Apply style BEFORE creating the figure
plt.style.use('dark_background')

a = [1, 2, 4, 5]
b = [1, 2, 4, 5]

# Create figure + axes
fig, ax = plt.subplots()
ax.plot(a, b)

plt.show()


#All the Available styles

"""Categorized Styles:

1️⃣ Classic / Default baseline

_classic_test_patch → testing/legacy

classic → original Matplotlib look

_mpl-gallery, _mpl-gallery-nogrid → gallery examples

2️⃣ Dark background / high contrast

dark_background → all dark, neon colors, for presentations

seaborn-v0_8-dark, seaborn-v0_8-dark-palette, seaborn-v0_8-darkgrid → dark-focused seaborn variants

3️⃣ Light / Clean / Publication-ready

Solarize_Light2 → solarized light, modern minimal

bmh → light grey background, subtle grid, paper-friendly

ggplot → inspired by R ggplot2, light background, grid emphasized

fast → lightweight, minimal styling

grayscale → black-and-white, print-friendly

4️⃣ Seaborn family (most nuanced variations, color palettes)

seaborn-v0_8 → default seaborn theme

seaborn-v0_8-bright → vivid colors

seaborn-v0_8-colorblind → colorblind-safe

seaborn-v0_8-deep → deeper palette

seaborn-v0_8-muted → softer, muted tones

seaborn-v0_8-notebook → designed for Jupyter

seaborn-v0_8-paper → publication-ready

seaborn-v0_8-pastel → light pastel colors

seaborn-v0_8-poster, seaborn-v0_8-talk → presentation scaling (fonts/lines larger)

seaborn-v0_8-ticks → ticks emphasized

seaborn-v0_8-white, seaborn-v0_8-whitegrid → clean light backgrounds, grid optional

5️⃣ Other presentation / color-focused

fivethirtyeight → mimics 538 style, grey background, strong grid lines

tableau-colorblind10 → Tableau’s 10-color colorblind-safe palette

petroff10 → less common, specific color palette"""