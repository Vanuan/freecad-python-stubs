import subprocess

import os
#raise Exception('%s %s' % (os.getcwd(), os.listdir('.')))

rc = subprocess.call("./rename.sh", shell=True)
