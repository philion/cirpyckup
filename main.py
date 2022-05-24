# main.py

from distutils.log import error
from ntpath import join
import os
import sys
import platform 
import re
import shutil
import glob

from dulwich.repo import Repo
from dulwich import porcelain

# TODO Add logger

EXPECTED_VOLUME = "CIRCUITPY"
#BACKUP_DIR = "{}/.cirpyckup".format(os.path.expanduser("~"))
BACKUP_DIR = os.path.expanduser("~/.cirpyckup/circuitpy")
DOT_FILES = [".gitignore"]

# make sure backdir is ready

# repo is a Repo instance pointing to the git-python repository.
# For all you know, the first argument to Repo is a path to the repository
# you want to work with

def getRepo(dir = BACKUP_DIR):
    # check for existing di
    if os.path.isdir(dir):
        repo = porcelain.open_repo(dir)
    else:
        print("creating new repo:", dir)
        os.mkdir(dir)
        repo = porcelain.init(dir)
    return repo

def findTarget(target: str) -> str:
    match platform.system():
        case "Windows":
            print("Your system is Windows FIXME")
        case "Linux":
            print("Your system is Linux FIXME")
        case "Darwin":
            if os.path.ismount("/Volumes/" + EXPECTED_VOLUME):
                return os.path.abspath("/Volumes/" + EXPECTED_VOLUME)
            else:
                return ""
            
        case _:
            print("Error, unknown system:", platform.system) # log error
            return ""

    # TODO Find a better way to manage 

def main() -> int:
    # Find the CIRCUITPY volume
    toBackup = findTarget(EXPECTED_VOLUME)
    if toBackup:
        repo = getRepo()
        if repo: 
            print("backing up to", str(repo))

            # jumps right in, assuming nothing else is going on in that directory.
            # TODO add a lock file.
            for filename in glob.iglob('{}/**/*'.format(toBackup), recursive=True):
                if os.path.isdir(filename):
                    print("skipping", filename)
                else:
                    # file name issie: filename container absolute path, including "/Volumes/CIRCUITPY"
                    # strip leading chars with filename[len(toBackup)+1:]
                    toFile = os.path.join(BACKUP_DIR, filename[len(toBackup)+1:])
                    print(os.path.abspath(filename), "-->", toFile)
                    shutil.copy2(filename, toFile)
                    porcelain.add(repo, toFile)

            porcelain.commit(repo, "backing up code")        
            return 0
    else:
        print("can't find attached drive")
        return 1

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit