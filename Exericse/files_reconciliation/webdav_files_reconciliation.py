"""
    webdav files reconciliation
    pip install webdavclient3
    pip install PyWebDAV3
    pip install certifi
"""

import os

from webdav3.client import Client

options = {
    "webdav_hostname": "https://192.168.50.162:8283/remote.php/dav/files/cho/Pixel5",
    "webdav_login": "cho",
    "webdav_password": "Gre@tR/cl98z",
    "cert_path": "C:\\Users\\chin.p.ho\\Downloads\\nextcloud.crt"
}

client = Client(options)
client.verify = False

print((client.list("Camera/*")))
