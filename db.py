#!/usr/bin/python

import dropbox
import pathlib
import re

# the source file
folder = pathlib.Path(".")    # located in this folder
filename = "log-rpi-zero-w.txt"         # file name
filepath = folder / filename  # path object, defining the file

# target location in Dropbox
target = "/IP_Log/"              # the target folder
targetfile = target + filename   # the target path and file name

# Create a dropbox object using an API v2 key
d = dropbox.Dropbox('<api key here>')

# open the file and upload it
with filepath.open("rb") as f:
   # upload gives you metadata about the file
   # we want to overwite any previous version of the file
   meta = d.files_upload(f.read(), targetfile, mode=dropbox.files.WriteMode("overwrite"))

# create a shared link
#link = d.sharing_create_shared_link(targetfile)

# url which can be shared
#url = link.url

# link which directly downloads by replacing ?dl=0 with ?dl=1
#dl_url = re.sub(r"\?dl\=0", "?dl=1", url)
#print (dl_url)
