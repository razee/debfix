# [debfix](https://github.com/kernc/debfix) — dot-files and tweaks

## Tweaks for Debian (or derivative) GNU/Linux distribution

This repository consists mostly of **dot-files for a swell Xfce-based experience**
and some administrative scripts that increase the performance and convenience
of GNU/Linux as a desktop environment. In other words, this repository should
contain **all that is needed to turn a vanilla Debian** Xfce install (or
similar, YMMV) **into my and mom's favorite OS**.

It it comprised of two parts:
* user configuration [dot-files](https://github.com/kernc/debfix#about-dot-files)
* [debfix.py script](https://github.com/kernc/debfix#debfix-system-tweaks) for system-wide tweaks

Any feedback, suggestions, bugs, fixes, requests and ideas are welcome!

## Debfix System Tweaks

Using the 'template' files in `debfix` directory, `debfix.py` script 
sequentially prompts the user to:
* (performance)
    * [defer all DPkg triggers](http://raphaelhertzog.com/2011/05/30/trying-to-make-dpkg-triggers-more-useful-and-less-painful/) until the very end of installation
    * set 'noatime' flag on all `/etc/fstab` mounts (—is it OK to set it on ALL mounts?)
    * apply [sysctl optimizations](https://github.com/kernc/debfix/blob/master/debfix/etc_sysctl.d_debfix-desktop-performance.conf) (for a desktop workstation)
        * also [increase sampling_down_factor](http://forums.gentoo.org/viewtopic-p-6682533.html?sid=a180868bde5a91214fcf7a12e43770c6#6682533) of ondemand CPU governor
* (convenience)
    * set a [neat](http://http.debian.net/) ( **Debian only** ) sources.list (including deb-multimedia.org)
    * set nice default Synaptic config (should be part of dot-files if it weren't `/root`'s)
    * enable tapping and edge scrolling for touchpads (by xorg.conf rule)
    * add tmpfs `/tmp` mount to `/etc/fstab` with `size=2G` (—is it better to set TMP_SIZE in `/etc/default/tmpfs`??)
    * add usbfs mount to `/etc/fstab` for VirtualBox (—seems like not needed anymore?)
    * fix resume from hibernation issues
    * disable (blacklist) PC-speaker
    * install 'sections' of packages (defined in [debfix/debfix-packages.conf](https://github.com/kernc/debfix/blob/master/debfix/debfix-packages.conf))
        * install appropriate VirtualBox Extension Pack (only if 'virtualbox' section is selected)
        * track and pin the latest [iceweasel-esr](http://www.mozilla.org/en-US/firefox/organizations/) (only if 'mozilla' section is selected)
    * install latest TeamViewer (currently with a low-risk but open symlink attack vector :-) )
    * install latest Skype

Further details revealed with inspection of related `do_*` functions in the script.

You can suppy `-y` or `--assume-yes` to the script to choose 'yes' (or other
provided default) on all prompts. Unattended is hugely untested, though. :-)


## About dot-files

You can easily copy the configuration dot-files to your `$HOME` with
`copy_dotfiles.py` script.
Files and directories starting with `.` thus hold:
* a neat and useful [`.bashrc`](https://github.com/kernc/debfix/tree/master/.bashrc) with a nice `$PS1` prompt
* some gathered `.fonts`
* some gathered scripts in [`.local/bin`](https://github.com/kernc/debfix/tree/master/.local/bin)
* cross-session autostart (devilspie, tilda, disable tapping while typing, disable alert, ...)
* custom [XDG user directories](https://github.com/kernc/debfix/blob/master/.config/user-dirs.dirs)
* Xfce4 (currently gtk-2.0 only) and xfwm4 `.themes`
* additional configuration is included for, but not limited to:
    * **Audacious** (..., [yaxamp skin](http://www.allwinampskins.com/yaxamp.wsz))
    * **devilspie**
        * hide audacious from taskbar (status icon in notification area is enough)
        * minimal-sized skype call windows
        * sticky Pidgin conversations, Firefox, and Geany
    * **evince**
    * **Geany** (config and nice dark syntax highlighting for [some languages](https://github.com/kernc/debfix/blob/master/.config/geany/filedefs))
    * **GiMP** (a couple of custom keybinings)
    * **IPython** (default profile more shell-like & default `__future__.division` & scientific imports ...)
    * **Mousepad** (8px font)
    * **Pidgin** (prefs, custom smileys)
    * **qBittorrent** (lite interface & solid settings)
    * **SpeedCrunch**
    * **Thunar** (small icons, toolbar-style location, custom actions)
    * **tilda**: drop-down, quake-like terminal (set on (my) 'cedilla' key, above Tab)
    * **Xfce4** (solid settings for novices (optional [windows look](https://github.com/kernc/debfix/blob/master/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-panel.xml.windows)) & pros)
    * **xfce4-terminal** (small font, large scrollback history, no auto scrolling)
    * **Mozilla Firefox** (and Iceweasel)
        * look & feel (window, context menu)
        * about:config prefs
        * **extensions** anyone should have:
            * Adblock Plus
            * Custom Buttons (have JavaScript-run buttons on your chrome)
            * dictionaries (Slovene, English)
            * Dictionary Lookup Extension
            * Greasemonkey
            * Image Zoom
            * keyconfig (to remap annoying Ctrl+Q etc.)
            * NoScript
            * Text Link
            * Textarea Cache (never again lose your lengthy forum post)
            * Tree Style Tab (for proper vertical hierarchical tabs)
            * X-notifier (for all of your Gmail et al. accounts)
            * for developers (Firebug, Links & Forms, TamperData, View Deps, View Frames, WebDeveloper)

## Installation instructions

You can download the latest version in a
[.zip](https://github.com/kernc/debfix/archive/master.zip) or
[.tar.gz](https://github.com/kernc/debfix/archive/master.tar.gz) format.

You unpack it with:
```bash
$ unzip master.zip   # or
$ tar -xvzf master.tar.gz
```
Then:
```bash
$ cd debfix-master
$ python copy_dotfiles.py   # to copy dot-files to your $HOME,   and
$ sudo python debfix.py     # to run the interactive tweaking script
```

Please **let me know** if you experience any issues!