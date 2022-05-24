# cirpyckup
Backup tools for circuitpython projects

First step: Simple script to:
1) Copy files from CIRCUITPY drive to backup location (where?)
2) Update in local git repo (not worried about git-remote for now, just local backup-with-history)

questions:
- how to figure out if drive is detected? Right now, works only for Mac using `/Volumes/CIRCUITPY`.
- manage ignorable with .gitignore in CIRCUITPY (that gets copied: Noy yet implemented)
- native python git library: https://www.dulwich.io/docs/tutorial/porcelain.html

### TODO (for a "real" release)
* lock managment
* logging and exception handling
* project management (file on drive->project on FS?)
* add "--restore", which copies files back to an empty drive.
* add ".gitignore" and management of dotfiles (which are ignored in current process)

### Notes
Worth trying to figure out is circuitpython (thru C libs, if at all) can set up a TCP/IP connection thru the USB controller. Essentially, when plugged into USB, a system could upload/forward all stored logs automatically just thru the USB connection.


Or, on ESP32 boards, a community-store-and-forward based on something like MQTT over https://openwisp.org/whatis.html.

ASIDE: 

Check on Circuitpython plugin for VS code: does it do soomething already? local copy?
keep copy over drive eject (hard-reset vs. soft-reboot). Similar issue with having files 
open and restoring serial connection after reset.
