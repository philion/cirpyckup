# cirpyckup
Backup tools for circuitpython projects

First step: Simple script to:
1) Copy files from CIRCUITPY drive to backup location (where?)
2) Update in local git repo (not worried about git-remote for now, just local backup-with-history)

questions:
- how to figure out if drive is detected? (just volume name?)
- manage ignorable with .gitignore in CIRCUITPY (that gets copied)
- native python git library? https://gitpython.readthedocs.io/en/stable/tutorial.html#tutorial-label

Check on Circuitpython plugin for VS code: does it do soomething already? local copy?
keep copy over drive eject (hard-reset vs. soft-reboot). Similar issue with having files 
open and restoring serial connection after reset.
