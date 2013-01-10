#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function as print_function
import subprocess, shlex
import logging

data_dir = 'debfix_files/'  # where files are, except dot-files

log = logging.getLogger()
def init_logging():
  log.setLevel(logging.DEBUG)
  ch = logging.StreamHandler()
  ch.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
  log.addHandler(ch)

def user_choice(question):
  choice = '("" in "ynq") resolves to True, so choice must be non-blank'
  while choice not in 'ynq':
    choice = raw_input(question + ' ? (y/N/q): ').lower() or 'n'
    if   choice == 'y': return True
    elif choice == 'n': return False
    elif choice == 'q': exit()

def sudo(command_line):
  """Return True if no error"""
  returncode = subprocess.call('/usr/bin/sudo ' + command_line, shell=True)
  if returncode:
    log.warn('/usr/bin/sudo failed, trying su to root')
    returncode = subprocess.call('su root && ' + command_line, shell=True)
  return returncode == 0    

def do_copy_apt_config_no_triggers():
  """Optimize performance of apt by defering DPkg triggers"""
  if sudo('cp {}99defer-triggers /etc/apt/apt.conf.d/'.format(data_dir)):
    log.info('Created /etc/apt/apt.conf.d/99defer-triggers')
  else:
    log.warn('Failed to copy 99defer-triggers to /etc/apt/apt.conf.d')

def do_copy_xorg_synaptics_config():
  """Set touchpad tap-to-click and edge scrolling"""
  if sudo('cp {}10-synaptics.conf /etc/X11/xorg.conf.d/'.format(data_dir)):
    log.info('Created /etc/X11/xorg.conf.d/10-synaptics.conf')
  else:
    log.warn('Failed to copy 10-synaptics.conf to /etc/X11/xorg.conf.d')

def do_copy_dotfiles():
  """Copy dot-files (default desktop & apps config) to $HOME"""
  pass

def do_set_debian_sources_list():
  """Set Debian /etc/apt/sources.list"""
  release = 'wheezy'
  release = raw_input('Debian release to track (stable/sid/...) [{}]: '
                      .format(release)).lower() or release
  command = ('mv /etc/apt/sources.list{{,~debfix}} && '
             'mv {}sources.list /etc/apt/sources.list && '
             'sed -i "s/wheezy/{}/g" /etc/apt/sources.list'.format(data_dir, release))
  if sudo(command):
    log.info('Created /etc/apt/sources.list (Back-up as sources.list~debfix)')
  else:
    log.warn('Failed to create /etc/apt/sources.list. '
             'Please DO investigate manually!')

def do_set_noatime_in_fstab_mounts():
  """Filesystem may make *SEVERAL DIRK WRITES FOR EACH READ* operation
as it updates the access times of accessed files and parent directories!
Setting 'noatime' flag on local mount points may reduce disk-writing.
Set 'noatime' flag on local mounts defined in /etc/fstab"""
  f = open('/etc/fstab')
  

def do_add_tmpfs_mount_to_fstab():
  """Firefox may store partly downloaded files/YouTube videos to /tmp.
As a result, /tmp can sometimes grow quite large, well over 800M default.
Add 'tmpfs /tmp ...size=2G...' to /etc/fstab"""
  if sudo('echo -e "\ntmpfs /tmp tmpfs nodev,nosuid,size=2G,mode=1777 0 0" >> /etc/fstab'):
    log.info('tmpfs line added to /etc/fstab.')
  else:
    log.warn('Failed to add tmpfs line to /etc/fstab')

def do_add_usbfs_mount_to_fstab():
  """VirtualBox (and VMWare, etc.) may need the following line in /etc/fstab:
usbfs /proc/bus/usb usbfs busgid=1000,busmode=0775,devgid=1000,devmode=0664 0 0
Add above line to /etc/fstab"""
  if sudo('echo -e "\nusbfs /proc/bus/usb usbfs busgid=1000,busmode=0775,devgid=1000,devmode=0664 0 0" >> /etc/fstab'):
    log.info('usbfs line added to /etc/fstab.')
  else:
    log.warn('Failed to add usbfs line to /etc/fstab')

def do_fix_initramfs_hibernate_resume():
  """The value in /etc/initramfs-tools/conf.d/resume must match to the UUID of
the swap partition (from /etc/fstab or result of `blkid`) in order for resume
(from hibernation) to work.
Ensure UUIDs match"""
  f = open('/etc/fstab')
  uuid = re.search('([^\s]+)\s\w+\sswap\s\w+\s0\s0', f.read()).groups()[0]
  f.close()
  if sudo('echo "RESUME=' + uuid + '" > /etc/initramfs-tools/conf.d/resume') and
     sudo('update-initramfs -u'):
    log.info('/etc/initramfs-tools/conf.d/resume set to ' + uuid)
  else:
    log.warn('Failed to set /etc/initramfs-tools/conf.d/resume to ' + uuid)



def main():
  init_logging()
  for fname, func in globals().items():
    if fname.startswith('do_') and user_choice(func.__doc__):
      func()

if __name__=='__main__':
    main()
