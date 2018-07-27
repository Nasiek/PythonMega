In case you missed it from the previous video here is again how to install a third party Python library (e.g. glob2 ).

Simply open your command line / terminal and execute:

pip install glob2

If that doesn't work then do this:

python -m pip install glob2

If you have multiple Pythons (both version 2 and 3) installed you may need to use pip3:

pip3 install glob2

If that doesn't work please execute:

python3 -m pip install glob2



##########more notes on install packages in python3
#python3 is specific and not the defaultself.
#it seems to need to be specified at all times when it's being used.
#so to use it.. do this:

# download and install setuptools
curl -O https://bootstrap.pypa.io/ez_setup.py
python3 ez_setup.py
# download and install pip
curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py

#just use pip3 to do whatever you want to
# eg
pip3 --version #gives
#then
python3 -m pip install glob2 #you already had it though.
#or
pip3 install glob2


#then
pip3 install requests
#enter python shell
python3
#and alas
import requests
requests
dir(requests)
#^^ this is the format for whatever you wanna import after pip3 install...
import glob2
glob2
#using builtin python methods to get info
#on what's inside of a package/library/module
dir(glob2) #directory
help(glob2) #help gives you readable nicely formatted pagination
help(glob2.glob)
dir(glob2.glob) #you can go inside
[for name in name dir(glob2)] #gives same result as help or dir
[for name in name dir(requests) if 'http' in name.lower()]
#last argument checks for a string within the name
[for name in name dir(requests) if 'conn' in name.lower()]
help(requests.ConnectionTimeout)

### extra great tip here:
bpython

import requests
requests. #shows all available names
requests.HTTPError(#
#this can be done in pycharm or in sublime text with the anaconda plugin.
