#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function
import os
import subprocess
from debfix import user_choice

def do_copy_dotfiles():
  """Copy dot-files (default desktop & apps config) to $HOME"""
  if user_choice('Copy configuration dot-files to ' + os.environ['HOME']):
    subprocess.call('cp -vr ./.[a-zA-Z0-9]* ~/', shell=True)
    if user_choice('Do you wish to use Xfce with Windows-like panel layout'):
      subprocess.call('cp -v '
          '~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-panel.xml.windows '
          '~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-panel.xml', shell=True)

def main():
  if os.getuid() == 0:
    print('This script should be RUN WITH NORMAL USER PRIVILEGES, yet currently you are root.')
    if not user_choice('Are you sure you want to copy dot-files to root user\'s home dir (/root)'):
      exit()
  do_copy_dotfiles()
  if user_choice('Make XDG_* directories ~/multimedia ~/tmp ~/documents ~/documents/images'):
    subprocess.call('mkdir ~/multimedia ~/tmp ~/documents ~/documents/images', shell=True)
  print('All done.')

if __name__ == '__main__':
  main()
