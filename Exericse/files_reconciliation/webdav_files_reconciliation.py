"""
    webdav files reconciliation - https://pypi.org/project/webdavclient3/
    pip install webdavclient3
    pip install PyWebDAV3
    pip install certifi
"""

import os

from webdav3.client import Client

print("Get Current Directory: ", os.getcwd())
os.chdir("G:\\PICTURES\\2023_iphoneMaxBackup\\networkTransfer\\NextCloud\\")
print("Get Changed Directory: ", os.getcwd())


options = {
    "webdav_hostname": "https://192.168.50.162:8283/remote.php/dav/files/annachow/iPhone13Max",
    "webdav_login": "annachow",
    "webdav_password": "6463460876",
    "cert_path": "C:\\Users\\chin.p.ho\\Downloads\\nextcloud.crt",
}
client = Client(options)
client.verify = False

print("Total files on NextCloud:", len(client.list()))
print("Total files on Local Folder:", len(os.listdir()))

setNextCloud = set(client.list())
setLocal = set(os.listdir())

missing_file = setNextCloud.difference(setLocal)
print("missing file:", missing_file)
