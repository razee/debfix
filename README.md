# debfix - dotfiles and tweaks

## Tweaks for Debian (or derivative) GNU/Linux distribution

This repository consists mostly of dot-files for a swell Xfce-based experience
and some administrative scripts that increase the performance and convenience
of GNU/Linux as a desktop environment. In other words, this repository should
contain all that I need to turn a vanilla install (of mainly Debian or
Debian-based) into my mom's favorite OS.

It it comprised of two parts:
* user configuration [dot-files](https://github.com/kernc/debfix#about-dot-files)
* [debfix.py script](https://github.com/kernc/debfix#debfix-system-tweaks) for system-wide tweaks


## Debfix System Tweaks

With the help of 'common' files in `debfix` directory, `debfix.py` script
sequentially prompts the user to:
* (performance)
    * [defer all DPkg triggers](http://raphaelhertzog.com/2011/05/30/trying-to-make-dpkg-triggers-more-useful-and-less-painful/)
    * set 'noatime' flag on all `/etc/fstab` mounts
    * apply sysctl optimizations (for a desktop workstation)
* (convenience)
    * set a [neat](http://http.debian.net/) sources.list (including deb-multimedia.org)
    * set nice default synaptics config (should be part of dot-files if it weren't `/root`'s)
    * set xorg.conf for synaptics touchpad with tapping and edge scrolling
    * add tmpfs `/tmp` mount to `/etc/fstab` with `size=2G`
    * add usbfs mount to `/etc/fstab` for VirtualBox (seems like not needed any more?)
    * fix resume from hibernation issues
    * disable (blacklist) PC-speaker
    * install 'sections' of packages (defined in [debfix/debfix-packages.conf](https://github.com/kernc/debfix/blob/master/debfix/debfix-packages.conf))
        * install appropriate VirtualBox Extension Pack
        * track and pin the latest [iceweasel-esr](http://www.mozilla.org/en-US/firefox/organizations/) from mozilla.debian.org
    * install latest TeamViewer
    * install latest Skype


## About dot-files

You can easily copy the configuration dot-files to your `$HOME` with
`copy_dotfiles.py` script.

Files and directories starting with `.` thus hold:
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
    * IPython (default profile more shell-like & default `__future__` & scientific imports ...)
    * Mousepad (smaller font)
    * Pidgin (prefs, custom smileys (some localized to sl, sorry))
    * qBittorrent (lite interface & solid settings)
    * SpeedCrunch
    * Thunar (small icons, toolbar-style location, custom actions)
    * tilda: drop-down, quake-like terminal (on (my) 'cedilla' key, above Tab)
    * Xfce4 (solid settings for novices ([windows look](https://github.com/kernc/debfix/blob/master/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-panel.xml.windows)) & pros)
    * xfce4-terminal (small font, large scrollback history, no auto scrolling)
    * Mozilla Firefox (and Iceweasel)
        * look & feel (window, context menu)
        * about:config prefs
        * extensions anyone should have*
            * Adblock Plus
            * Custom Buttons (for JavaScript-run buttons on your chrome)
            * dictionaries (Slovene, English)
            * Dictionary Lookup Extension
            * Greasemonkey
            * Image Zoom
            * keyconfig (to remap annoying Ctrl+Q)
            * NoScript
            * Text Link
            * Tree Style Tab (for proper vertical hierarchical tabs)
            * X-notifier (for all of your Gmail et al. accounts)
            * for developers (FireBug & extensions, Links and Forms, TamperData, View Dependencies, View Frames, WebDeveloper)
    