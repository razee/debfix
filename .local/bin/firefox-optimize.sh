#!/bin/bash

ZEN="/usr/bin/zenity";
SQLITE3="/usr/bin/sqlite3";
if test -f "${SQLITE3}";then
    if test -f "${ZEN}";then
      zenity --info --text "Firefox will be closed for database optimization." && 
      killall firefox
      echo "Please wait while the databases are optimized..."
      find $HOME/.mozilla/ \( -name "*.sqlite" \) -exec sqlite3 {} "vacuum" \; &&
      echo "Firefox databases optimized with success!"
      zenity --info --text "Firefox databases optimized with success!" 
    else
      killall firefox
      echo "Please wait while the databases are optimized..."
      find $HOME/.mozilla/ \( -name "*.sqlite" \) -exec sqlite3 {} "vacuum" \;
      echo "Firefox databases optimized with success!"
    fi
else
    if test -f "${ZEN}";then
      zenity --info --text "You need to install sqlite3 package."
      echo "You need to install sqlite3 package."
    else
      echo "You need to install sqlite3 package."
    fi
fi


