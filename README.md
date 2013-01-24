debfix - Small fixes for Debian (or derivative) GNU/Linux distribution
======================================================================

This repository consists mostly of dot-files for a swell Xfce-based experience
and some administrative scripts that increase the performance and convenience
of GNU/Linux as a desktop environment. In other words, this repository should
contain all that I need to turn a vanilla install (of mainly Debian or
Debian-based) into my mom's favorite OS.

It it comprised of two parts:
* dot-files
* debfix.py script

About dot-files
===============
You can easily copy the configuration dot-files to your $HOME with
copy_dotfiles.py script.

Files and directories starting with dot thus hold:
* a nice and useful [`.bashrc`](https://github.com/kernc/debfix/tree/master/.bashrc)
* some gathered `.fonts`
* some gathered scripts in [`.local/bin`](https://github.com/kernc/debfix/tree/master/.local/bin)
* autostart (devilspie, tilda, disable tapping while typing, disable alert, ...)
* custom [XDG user directories](https://github.com/kernc/debfix/blob/master/.config/user-dirs.dirs)
* Xfce4 (currently gtk-2.0 only) and xfwm4 `.themes`
* additional configuration is included for, but not limited to:
    * Audacious (..., [yaxamp skin](http://www.allwinampskins.com/yaxamp.wsz))
    * devilspie
        * hide audacious from taskbar (status icon in notification area is enough)
        * minimal-sized skype call windows
        * sticky Pidgin conversations, Firefox, and Geany
    * evince
    * Geany (config and nice dark syntax highlighting for [some languages](https://github.com/kernc/debfix/blob/master/.config/geany/filedefs))
    * GiMP (a couple of custom keybinings)
    * IPython (default profile more shell-like & default __future__ import, numpy, ...)
    * Mousepad (smaller font)
    * Pidgin (prefs, custom smileys (some localized to sl, sorry))
    * qBittorrent (lite interface & solid settings)
    * SpeedCrunch
    * Thunar (small icons, toolbar-style location, custom actions)
    * tilda: drop-down, quake-like terminal (on (my) 'cedilla' key, above Tab)
    * Xfce4 (solid settings for novices ([windows look](https://github.com/kernc/debfix/blob/master/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-panel.xml.windows)) & pros)
    * xfce4-terminal (small font, large scrollback history, no scroll on output)
    * Mozilla Firefox (and Iceweasel)
        * look & feel (window, context menu)
        * about:config prefs
        * extensions anyone should have
            * Custom Buttons
            * dictionaries (Slovene, English)
            * Dictionary Lookup Extension
            * Greasemonkey
            * Image Zoom
            * keyconfig (to remap annoying Ctrl+Q)
            * NoScript
            * Adblock Plus
            * Text Link
            * Tree Style Tab
            * X-notifier
            * for developers (WebDeveloper, FireBug & extensions, TamperData, Links and Forms, View Dependencies, View Frames)

