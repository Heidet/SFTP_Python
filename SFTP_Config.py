import paramiko
import pysftp
from base64 import decodebytes
import sys
from datetime import datetime
import os


myHostname = "access793895954.webspace-data.io"
myUsername = "u98187406-antoine"
myPassword = "Test.antoine1234"

cnopts = pysftp.CnOpts()

hostkeys = None

if cnopts.hostkeys.lookup(myHostname) == None:
    print("New host - will accept any host key")
    # Backup loaded .ssh/known_hosts file
    hostkeys = cnopts.hostkeys
    # And do not verify host key of the new host
    cnopts.hostkeys = None

# dn = datetime.now().strftime("%Y%m%d%H");
remotePath = "./"

with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword,  cnopts=cnopts) as sftp:
    if hostkeys != None:
        print("Connecté au nouvel hôte, mettant en cache sa clé d'hôte")
        hostkeys.add(myHostname, sftp.remote_server_key.get_name(), sftp.remote_server_key)
        hostkeys.save(pysftp.helpers.known_hosts())
    else:
        print("Connexion établie avec succès ...")
        myFileList = sftp.listdir(remotePath)
        for filename in myFileList:
           print(filename)
           print(os.path.isdir(remotePath + filename))
           # print(myFileList)
           # if (filename.rfind('./' + dn) != -1):
           #     print('blablabla')
           #     sftp.get("./" + filename, "/tmp/" + filename)