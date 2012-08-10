#
# Script to set up the vimrc files and directories in the right places
#

import os
import sys
import platform
import shutil
import subprocess

home_path = os.path.expanduser('~')
vim_path = os.path.join(home_path, ".vim")

try:
    print 'Creating directory %s' % vim_path
    if not os.path.exists(vim_path): os.mkdir(vim_path)

    print 'Creating backups directory'
    backups_path = os.path.join(vim_path, "backups")
    if not os.path.exists(backups_path): os.mkdir(backups_path)

    print 'Creating swaps directory'
    swaps_path = os.path.join(vim_path, "swaps")
    if not os.path.exists(swaps_path): os.mkdir(swaps_path)

    print 'Creating bundle directory'
    bundle_path = os.path.join(vim_path, "bundle")
    if not os.path.exists(bundle_path): os.mkdir(bundle_path)

except IOError, e:
    print e
    sys.exit()

if not os.path.exists(os.path.join(bundle_path, "vundle")):
    vundle_repo = "https://github.com/gmarik/vundle.git"
    print 'Vundle not detected. Attempting to clone from %s' % vundle_repo
    try:
        subprocess.call(["git", "clone", vundle_repo, os.path.join(bundle_path, "vundle")])
    except:
        print 'An error occurred while attempting to clone Vundle, please clone manually afterward.'
else:
    print 'Vundle installation detected'

if platform.system() == 'Windows':
    leading_mark = '_'
else: 
    leading_mark = '.'

dest_vimrc = os.path.join(home_path, leading_mark + 'vimrc')
dest_gvimrc = os.path.join(home_path, leading_mark + 'gvimrc')  

print 'Copying _vimrc to %s' % dest_vimrc
shutil.copy('_vimrc', dest_vimrc)
print 'Copying _gvimrc to %s' % dest_gvimrc
shutil.copy('_gvimrc', dest_gvimrc)

print 'Done'

