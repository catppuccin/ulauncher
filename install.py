import os
from pathlib import Path
import argparse
import json
import shutil

flavors = ["mocha", "frappe", "macchiato", "latte"]
accents = ["rosewater", "flamingo", "pink", "mauve", "red", "maroon", "peach",
           "yellow", "green", "teal", "sky", "sapphire", "blue", "lavender"]

parser = argparse.ArgumentParser(
    description="ULauncher Catppuccin Theme Installer",
)

parser.add_argument("--radius", "-r",
                    metavar="radius",
                    type=int,
                    dest="radius",
                    choices=range(0, 49),
                    help="border radius of the theme (0 to 48)",
                    default=14,
                    )

parser.add_argument("--flavor", "-f",
                    metavar="flavor",
                    type=str,
                    nargs="+",
                    dest="flavor",
                    choices=flavors + ["all"],
                    help="it can include %s or all" % (", ".join(flavors)),
                    default=["mocha"],
                    )

parser.add_argument("--accent", "-a",
                    metavar="accent",
                    type=str,
                    nargs="+",
                    dest="accent",
                    choices=accents + ["all"],
                    help="it can include %s or all" % (", ".join(accents)),
                    default=["blue"],
                    )

colorPalette = {
    "latte": {
        "baseColor": "#eff1f5",
        "textColor": "#4c4f69",
        "subTextColor": "#5c5f77",
        "rosewater": "#dc8a78",
        "flamingo": "#dd7878",
        "pink": "#ea76cb",
        "mauve": "#8839ef",
        "red": "#d20f39",
        "maroon": "#e64553",
        "peach": "#fe640b",
        "yellow": "#df8e1d",
        "green": "#40a02b",
        "teal": "#179299",
        "sky": "#04a5e5",
        "sapphire": "#209fb5",
        "blue": "#1e66f5",
        "lavender": "#7287fd"
    },
    "frappe": {
        "baseColor": "#303446",
        "textColor": "#c6d0f5",
        "subTextColor": "#b5bfe2",
        "rosewater": "#f2d5cf",
        "flamingo": "#eebebe",
        "pink": "#f4b8e4",
        "mauve": "#ca9ee6",
        "red": "#e78284",
        "maroon": "#ea999c",
        "peach": "#ef9f76",
        "yellow": "#e5c890",
        "green": "#a6d189",
        "teal": "#81c8be",
        "sky": "#99d1db",
        "sapphire": "#85c1dc",
        "blue": "#8caaee",
        "lavender": "#babbf1"
    },
    "macchiato": {
        "baseColor": "#24273a",
        "textColor": "#cad3f5",
        "subTextColor": "#b8c0e0",
        "rosewater": "#f4dbd6",
        "flamingo": "#f0c6c6",
        "pink": "#f5bde6",
        "mauve": "#c6a0f6",
        "red": "#ed8796",
        "maroon": "#ee99a0",
        "peach": "#f5a97f",
        "yellow": "#eed49f",
        "green": "#a6da95",
        "teal": "#8bd5ca",
        "sky": "#91d7e3",
        "sapphire": "#7dc4e4",
        "blue": "#8aadf4",
        "lavender": "#b7bdf8"
    },
    "mocha": {
        "baseColor": "#1e1e2e",
        "textColor": "#cdd6f4",
        "subTextColor": "#bac2de",
        "rosewater": "#f5e0dc",
        "flamingo": "#f2cdcd",
        "pink": "#f5c2e7",
        "mauve": "#cba6f7",
        "red": "#f38ba8",
        "maroon": "#eba0ac",
        "peach": "#fab387",
        "yellow": "#f9e2af",
        "green": "#a6e3a1",
        "teal": "#94e2d5",
        "sky": "#89dceb",
        "sapphire": "#74c7ec",
        "blue": "#89b4fa",
        "lavender": "#b4befe",
    }
}


def installTheme(flavor, accent, radius):
    isLatte = flavor == "latte"
    selectedBackgroundOpacity = 0.1 if isLatte else 0.3
    gearHoverOpacity = 0.2 if isLatte else 1.0
    themeName = f"Catppuccin-{flavor.capitalize()}-{accent.capitalize()}"
    accentColor = colorPalette[flavor][accent]

    try:
        userThemes = Path(os.path.expanduser("~"), ".config",
                          "ulauncher", "user-themes", themeName)
        userThemes.mkdir(parents=True, exist_ok=True)

        manifest = {
            "manifest_version": "1",
            "name": themeName,
            "display_name": themeName.replace("-", " "),
            "extend_theme": "light",
            "css_file": "theme.css",
            "css_file_gtk_3.20+": "theme-gtk-3.20.css",
            "matched_text_hl_colors": {
                "when_selected": accentColor,
                "when_not_selected": accentColor
            }
        }

        with open(str(userThemes) + "/manifest.json", "w") as manifestFile:
            manifestFile.write(json.dumps(manifest, indent=2))

        with open(str(userThemes) + "/theme-gtk-3.20.css", "w") as themeGTKFile:
            themeGTKFile.write("\n".join([
                "@import url(\"theme.css\");",
                ".input {",
                "    caret-color: %s;" % (accentColor),
                "}",
                "/* workaround for a bug in GTK+ < 3.20 */",
                ".selected.item-box {",
                "    border: none;",
                "}",
            ]))

        with open(str(userThemes) + "/theme.css", "w") as themeFile:
            themeFile.write("\n".join([
                "/*Catpuccin colors*/",
                "@define-color backgroundColor %s;" % (
                    colorPalette[flavor]["baseColor"]),
                "@define-color accentColor %s;" % (accentColor),
                "@define-color textColor %s;" % (
                    colorPalette[flavor]["textColor"]),
                "@define-color subTextColor %s;" % (
                    colorPalette[flavor]["subTextColor"]),
                ".app {",
                "    background-color: @backgroundColor;",
                "    border-color: @accentColor;",
                "    border-radius: %ipx;" % (radius),
                "}",
                ".input {",
                "    color: @accentColor;",
                "}",
                ".input *:selected,",
                ".input *:focus,",
                "*:selected:focus {",
                "    background-color: alpha (@accentColor, 0.4);",
                "    color: @textColor;",
                "}",
                ".item-text {",
                "    color: @textColor;",
                "}",
                ".item-name {",
                "    color: @textColor;",
                "    font-size: 1.2rem;",
                "}",
                ".selected.item-box {",
                "    background-color: alpha (@accentColor, %.1f);" % (
                    selectedBackgroundOpacity),
                "    border-radius: %ipx;" % (radius),
                "}",
                ".selected.item-box .item-text {",
                "    color: @textColor;",
                "}",
                ".selected.item-box .item-name {",
                "    color: @textColor;",
                "    font-size: 1.2rem;",
                "}",
                ".item-shortcut {",
                "    color: @accentColor;",
                "}",
                ".selected.item-box .item-shortcut {",
                "    color: @accentColor;",
                "    font-size: 1.1rem;",
                "}",
                ".selected.item-box{",
                "    color: @accentColor;",
                "}",
                ".prefs-btn {",
                "    opacity: 1;",
                "}",
                ".prefs-btn:hover {",
                "    background-color: alpha (@accentColor, %.1f);" % (
                    gearHoverOpacity),
                "}",
            ]))

    except Exception as exc:
        print(exc)


args = parser.parse_args()

if "all" in args.flavor:
    args.flavor = flavors
if "all" in args.accent:
    args.accent = accents

if not shutil.which("ulauncher"):
    exit("Ulauncher not found")

for flavor in args.flavor:
    for accent in args.accent:
        print(
            f"Installing Catppuccin-{flavor.capitalize()}-{accent.capitalize()}")
        installTheme(flavor, accent, args.radius)
