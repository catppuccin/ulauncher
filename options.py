import os
import sys
from pathlib import Path


class Theme:
    codeName = ""
    baseColor = ""
    textColor = ""
    subTextColor = ""
    rosewater = ""
    flamingo = ""
    pink = ""
    mauve = ""
    red = ""
    maroon = ""
    peach = ""
    yellow = ""
    green = ""
    teal = ""
    sky = ""
    sapphire = ""
    blue = ""
    lavender = ""

    def __init__(self, codeName: str, baseColor, textColor, subTextColor, rosewater,
                 flamingo, pink, mauve, red, maroon, peach, yellow, green,
                 teal, sky, sapphire, blue, lavender):

        self.codeName = codeName
        self.baseColor = baseColor
        self.textColor = textColor
        self.subTextColor = subTextColor
        self.rosewater = rosewater
        self.flamingo = flamingo
        self.pink = pink
        self.mauve = mauve
        self.red = red
        self.maroon = maroon
        self.peach = peach
        self.yellow = yellow
        self.green = green
        self.teal = teal
        self.sky = sky
        self.sapphire = sapphire
        self.blue = blue
        self.lavender = lavender


borderRadius = "14px"

LatteTheme = Theme(codeName="Latte",
                   baseColor="#eff1f5",
                   textColor="#4c4f69",
                   subTextColor="#5c5f77",
                   rosewater="#dc8a78",
                   flamingo="#dd7878",
                   pink="#ea76cb",
                   mauve="#8839ef",
                   red="#d20f39",
                   maroon="#e64553",
                   peach="#fe640b",
                   yellow="#df8e1d",
                   green="#40a02b",
                   teal="#179299",
                   sky="#04a5e5",
                   sapphire="#209fb5",
                   blue="#1e66f5",
                   lavender="#7287fd")

FrappeTheme = Theme(codeName="Frappe",
                    baseColor="#303446",
                    textColor="#c6d0f5",
                    subTextColor="#b5bfe2",
                    rosewater="#f2d5cf",
                    flamingo="#eebebe",
                    pink="#f4b8e4",
                    mauve="#ca9ee6",
                    red="#e78284",
                    maroon="#ea999c",
                    peach="#ef9f76",
                    yellow="#e5c890",
                    green="#a6d189",
                    teal="#81c8be",
                    sky="#99d1db",
                    sapphire="#85c1dc",
                    blue="#8caaee",
                    lavender="#babbf1")

MacchiatoTheme = Theme(codeName="Macchiato",
                       baseColor="#24273a",
                       textColor="#cad3f5",
                       subTextColor="#b8c0e0",
                       rosewater="#f4dbd6",
                       flamingo="#f0c6c6",
                       pink="#f5bde6",
                       mauve="#c6a0f6",
                       red="#ed8796",
                       maroon="#ee99a0",
                       peach="#f5a97f",
                       yellow="#eed49f",
                       green="#a6da95",
                       teal="#8bd5ca",
                       sky="#91d7e3",
                       sapphire="#7dc4e4",
                       blue="#8aadf4",
                       lavender="#b7bdf8")

MochaTheme = Theme(codeName="Mocha",
                   baseColor="#1e1e2e",
                   textColor="#cdd6f4",
                   subTextColor="#bac2de",
                   rosewater="#f5e0dc",
                   flamingo="#f2cdcd",
                   pink="#f5c2e7",
                   mauve="#cba6f7",
                   red="#f38ba8",
                   maroon="#eba0ac",
                   peach="#fab387",
                   yellow="#f9e2af",
                   green="#a6e3a1",
                   teal="#94e2d5",
                   sky="#89dceb",
                   sapphire="#74c7ec",
                   blue="#89b4fa",
                   lavender="#b4befe")


def installTheme(theme: Theme, accentName):

    itsLatte = theme == LatteTheme
    selectedBackgroundOpacity = 0.1 if itsLatte else 0.3
    gearHoverOpacity = 0.2 if itsLatte else 1


    try:

        userThemes = Path(os.path.expanduser('~'), '.config', 'ulauncher',
                      'user-themes',
                      f"Catpuccin-{theme.codeName}-{accentName}") 

        userThemes.mkdir(parents=True, exist_ok=True)

        if (accentName == "Rosewater"): accentColor = theme.rosewater
        if (accentName == "Flamingo"): accentColor = theme.flamingo
        if (accentName == "Pink"): accentColor = theme.pink
        if (accentName == "Mauve"): accentColor = theme.mauve
        if (accentName == "Red"): accentColor = theme.red
        if (accentName == "Maroon"): accentColor = theme.maroon
        if (accentName == "Peach"): accentColor = theme.peach
        if (accentName == "Yellow"): accentColor = theme.yellow
        if (accentName == "Green"): accentColor = theme.green
        if (accentName == "Teal"): accentColor = theme.teal
        if (accentName == "Sky"): accentColor = theme.sky
        if (accentName == "Sapphire"): accentColor = theme.sapphire
        if (accentName == "Blue"): accentColor = theme.blue
        if (accentName == "Lavender"): accentColor = theme.lavender

        with open(str(userThemes) + "/manifest.json", "w") as manifestFile:
            manifestFile.write("""
{
    "manifest_version": "1",
    "name": "Catpuccin-%s-%s",
    "display_name": "Catpuccin %s %s",
    "extend_theme": "light",
    "css_file": "theme.css",
    "css_file_gtk_3.20+": "theme-gtk-3.20.css",
    "matched_text_hl_colors": {
        "when_selected": "%s",
        "when_not_selected": "%s"
    }
}
""" % (theme.codeName, accentName, theme.codeName, accentName, accentColor, accentColor))

        with open(str(userThemes) + "/theme-gtk-3.20.css", "w") as themeGTKFile:
            themeGTKFile.write("""
@import url("theme.css");

.input {
    caret-color: %s;
}
.selected.item-box {
    /* workaround for a bug in GTK+ < 3.20 */
    border: none;
}
""" % (accentColor))

        with open(str(userThemes) + "/theme.css", "w") as themeFile:
            themeFile.write("""
/*Catppuccin colors*/
@define-color backgroundColor %s;
@define-color accentColor %s;
@define-color textColor %s;
@define-color subTextColor %s;


.app {
    background-color: @backgroundColor;
    border-color: @accentColor;
    border-radius: %s;
}

.input {
    color: @accentColor;
}


.input *:selected,
.input *:focus,
*:selected:focus {
    background-color: alpha (@accentColor, 0.4);
    color: @textColor;
}

.item-text {
    color: @textColor;
}
.item-name {
    color: @textColor;
    font-size: 1.2rem;
}

.selected.item-box {
    background-color: alpha (@accentColor, %s);
    border-radius: %s;
}

.selected.item-box .item-text {
    color: @textColor;
}
.selected.item-box .item-name {
    color: @textColor;
    font-size: 1.2rem;
}


.item-shortcut {
    color: @accentColor;
}
.selected.item-box .item-shortcut {
    color: @accentColor;
    font-size: 1.1rem;
}

.selected.item-box{
    color: @accentColor;
}

.prefs-btn {
    opacity: 1;
}
.prefs-btn:hover {
    background-color: alpha (@accentColor, %s);
}

""" % (theme.baseColor, accentColor, theme.textColor, theme.subTextColor,
            borderRadius, selectedBackgroundOpacity, borderRadius,
            gearHoverOpacity))

    except Exception as exc:
        print(exc)


try:

    arguments = sys.argv
    if "--flat" in arguments: borderRadius = "2px"

    for argument in arguments:

        argument = argument.lower()

        if argument == "--all":
            installTheme(LatteTheme, "Rosewater")
            installTheme(LatteTheme, "Flamingo")
            installTheme(LatteTheme, "Pink")
            installTheme(LatteTheme, "Mauve")
            installTheme(LatteTheme, "Red")
            installTheme(LatteTheme, "Maroon")
            installTheme(LatteTheme, "Peach")
            installTheme(LatteTheme, "Yellow")
            installTheme(LatteTheme, "Green")
            installTheme(LatteTheme, "Teal")
            installTheme(LatteTheme, "Sky")
            installTheme(LatteTheme, "Sapphire")
            installTheme(LatteTheme, "Blue")
            installTheme(LatteTheme, "Lavender")
            installTheme(FrappeTheme, "Rosewater")
            installTheme(FrappeTheme, "Flamingo")
            installTheme(FrappeTheme, "Pink")
            installTheme(FrappeTheme, "Mauve")
            installTheme(FrappeTheme, "Red")
            installTheme(FrappeTheme, "Maroon")
            installTheme(FrappeTheme, "Peach")
            installTheme(FrappeTheme, "Yellow")
            installTheme(FrappeTheme, "Green")
            installTheme(FrappeTheme, "Teal")
            installTheme(FrappeTheme, "Sky")
            installTheme(FrappeTheme, "Sapphire")
            installTheme(FrappeTheme, "Blue")
            installTheme(FrappeTheme, "Lavender")
            installTheme(MacchiatoTheme, "Rosewater")
            installTheme(MacchiatoTheme, "Flamingo")
            installTheme(MacchiatoTheme, "Pink")
            installTheme(MacchiatoTheme, "Mauve")
            installTheme(MacchiatoTheme, "Red")
            installTheme(MacchiatoTheme, "Maroon")
            installTheme(MacchiatoTheme, "Peach")
            installTheme(MacchiatoTheme, "Yellow")
            installTheme(MacchiatoTheme, "Green")
            installTheme(MacchiatoTheme, "Teal")
            installTheme(MacchiatoTheme, "Sky")
            installTheme(MacchiatoTheme, "Sapphire")
            installTheme(MacchiatoTheme, "Blue")
            installTheme(MacchiatoTheme, "Lavender")
            installTheme(MochaTheme, "Rosewater")
            installTheme(MochaTheme, "Flamingo")
            installTheme(MochaTheme, "Pink")
            installTheme(MochaTheme, "Mauve")
            installTheme(MochaTheme, "Red")
            installTheme(MochaTheme, "Maroon")
            installTheme(MochaTheme, "Peach")
            installTheme(MochaTheme, "Yellow")
            installTheme(MochaTheme, "Green")
            installTheme(MochaTheme, "Teal")
            installTheme(MochaTheme, "Sky")
            installTheme(MochaTheme, "Sapphire")
            installTheme(MochaTheme, "Blue")
            installTheme(MochaTheme, "Lavender")

        elif argument == "--latte":
            installTheme(LatteTheme, "Rosewater")
            installTheme(LatteTheme, "Flamingo")
            installTheme(LatteTheme, "Pink")
            installTheme(LatteTheme, "Mauve")
            installTheme(LatteTheme, "Red")
            installTheme(LatteTheme, "Maroon")
            installTheme(LatteTheme, "Peach")
            installTheme(LatteTheme, "Yellow")
            installTheme(LatteTheme, "Green")
            installTheme(LatteTheme, "Teal")
            installTheme(LatteTheme, "Sky")
            installTheme(LatteTheme, "Sapphire")
            installTheme(LatteTheme, "Blue")
            installTheme(LatteTheme, "Lavender")

        elif argument == "--latte-rosewater":
            installTheme(LatteTheme, "Rosewater")

        elif argument == "--latte-flamingo":
            installTheme(LatteTheme, "Flamingo")

        elif argument == "--latte-pink":
            installTheme(LatteTheme, "Pink")

        elif argument == "--latte-mauve":
            installTheme(LatteTheme, "Mauve")

        elif argument == "--latte-red":
            installTheme(LatteTheme, "Red")

        elif argument == "--latte-maroon":
            installTheme(LatteTheme, "Maroon")

        elif argument == "--latte-peach":
            installTheme(LatteTheme, "Peach")

        elif argument == "--latte-yellow":
            installTheme(LatteTheme, "Yellow")

        elif argument == "--latte-green":
            installTheme(LatteTheme, "Green")

        elif argument == "--latte-teal":
            installTheme(LatteTheme, "Teal")

        elif argument == "--latte-sky":
            installTheme(LatteTheme, "Sky")

        elif argument == "--latte-sapphire":
            installTheme(LatteTheme, "Sapphire")

        elif argument == "--latte-blue":
            installTheme(LatteTheme, "Blue")

        elif argument == "--latte-lavender":
            installTheme(LatteTheme, "Lavender")

        elif argument == "--frappe":
            installTheme(FrappeTheme, "Rosewater")
            installTheme(FrappeTheme, "Flamingo")
            installTheme(FrappeTheme, "Pink")
            installTheme(FrappeTheme, "Mauve")
            installTheme(FrappeTheme, "Red")
            installTheme(FrappeTheme, "Maroon")
            installTheme(FrappeTheme, "Peach")
            installTheme(FrappeTheme, "Yellow")
            installTheme(FrappeTheme, "Green")
            installTheme(FrappeTheme, "Teal")
            installTheme(FrappeTheme, "Sky")
            installTheme(FrappeTheme, "Sapphire")
            installTheme(FrappeTheme, "Blue")
            installTheme(FrappeTheme, "Lavender")

        elif argument == "--frappe-rosewater":
            installTheme(FrappeTheme, "Rosewater")

        elif argument == "--frappe-flamingo":
            installTheme(FrappeTheme, "Flamingo")

        elif argument == "--frappe-pink":
            installTheme(FrappeTheme, "Pink")

        elif argument == "--frappe-mauve":
            installTheme(FrappeTheme, "Mauve")

        elif argument == "--frappe-red":
            installTheme(FrappeTheme, "Red")

        elif argument == "--frappe-maroon":
            installTheme(FrappeTheme, "Maroon")

        elif argument == "--frappe-peach":
            installTheme(FrappeTheme, "Peach")

        elif argument == "--frappe-yellow":
            installTheme(FrappeTheme, "Yellow")

        elif argument == "--frappe-green":
            installTheme(FrappeTheme, "Green")

        elif argument == "--frappe-teal":
            installTheme(FrappeTheme, "Teal")

        elif argument == "--frappe-sky":
            installTheme(FrappeTheme, "Sky")

        elif argument == "--frappe-sapphire":
            installTheme(FrappeTheme, "Sapphire")

        elif argument == "--frappe-blue":
            installTheme(FrappeTheme, "Blue")

        elif argument == "--frappe-lavender":
            installTheme(FrappeTheme, "Lavender")
        
        elif argument == "--macchiato":
            installTheme(MacchiatoTheme, "Rosewater")
            installTheme(MacchiatoTheme, "Flamingo")
            installTheme(MacchiatoTheme, "Pink")
            installTheme(MacchiatoTheme, "Mauve")
            installTheme(MacchiatoTheme, "Red")
            installTheme(MacchiatoTheme, "Maroon")
            installTheme(MacchiatoTheme, "Peach")
            installTheme(MacchiatoTheme, "Yellow")
            installTheme(MacchiatoTheme, "Green")
            installTheme(MacchiatoTheme, "Teal")
            installTheme(MacchiatoTheme, "Sky")
            installTheme(MacchiatoTheme, "Sapphire")
            installTheme(MacchiatoTheme, "Blue")
            installTheme(MacchiatoTheme, "Lavender")

        elif argument == "--macchiato-rosewater":
            installTheme(MacchiatoTheme, "Rosewater")

        elif argument == "--macchiato-flamingo":
            installTheme(MacchiatoTheme, "Flamingo")

        elif argument == "--macchiato-pink":
            installTheme(MacchiatoTheme, "Pink")

        elif argument == "--macchiato-mauve":
            installTheme(MacchiatoTheme, "Mauve")

        elif argument == "--macchiato-red":
            installTheme(MacchiatoTheme, "Red")

        elif argument == "--macchiato-maroon":
            installTheme(MacchiatoTheme, "Maroon")

        elif argument == "--macchiato-peach":
            installTheme(MacchiatoTheme, "Peach")

        elif argument == "--macchiato-yellow":
            installTheme(MacchiatoTheme, "Yellow")

        elif argument == "--macchiato-green":
            installTheme(MacchiatoTheme, "Green")

        elif argument == "--macchiato-teal":
            installTheme(MacchiatoTheme, "Teal")

        elif argument == "--macchiato-sky":
            installTheme(MacchiatoTheme, "Sky")

        elif argument == "--macchiato-sapphire":
            installTheme(MacchiatoTheme, "Sapphire")

        elif argument == "--macchiato-blue":
            installTheme(MacchiatoTheme, "Blue")

        elif argument == "--macchiato-lavender":
            installTheme(MacchiatoTheme, "Lavender")
        
        elif argument == "--mocha":
            installTheme(MochaTheme, "Rosewater")
            installTheme(MochaTheme, "Flamingo")
            installTheme(MochaTheme, "Pink")
            installTheme(MochaTheme, "Mauve")
            installTheme(MochaTheme, "Red")
            installTheme(MochaTheme, "Maroon")
            installTheme(MochaTheme, "Peach")
            installTheme(MochaTheme, "Yellow")
            installTheme(MochaTheme, "Green")
            installTheme(MochaTheme, "Teal")
            installTheme(MochaTheme, "Sky")
            installTheme(MochaTheme, "Sapphire")
            installTheme(MochaTheme, "Blue")
            installTheme(MochaTheme, "Lavender")

        elif argument == "--mocha-rosewater":
            installTheme(MochaTheme, "Rosewater")

        elif argument == "--mocha-flamingo":
            installTheme(MochaTheme, "Flamingo")

        elif argument == "--mocha-pink":
            installTheme(MochaTheme, "Pink")

        elif argument == "--mocha-mauve":
            installTheme(MochaTheme, "Mauve")

        elif argument == "--mocha-red":
            installTheme(MochaTheme, "Red")

        elif argument == "--mocha-maroon":
            installTheme(MochaTheme, "Maroon")

        elif argument == "--mocha-peach":
            installTheme(MochaTheme, "Peach")

        elif argument == "--mocha-yellow":
            installTheme(MochaTheme, "Yellow")

        elif argument == "--mocha-green":
            installTheme(MochaTheme, "Green")

        elif argument == "--mocha-teal":
            installTheme(MochaTheme, "Teal")

        elif argument == "--mocha-sky":
            installTheme(MochaTheme, "Sky")

        elif argument == "--mocha-sapphire":
            installTheme(MochaTheme, "Sapphire")

        elif argument == "--mocha-blue":
            installTheme(MochaTheme, "Blue")

        elif argument == "--mocha-lavender":
            installTheme(MochaTheme, "Lavender")

except:
    pass
