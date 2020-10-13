import paramiko
import pysftp
from base64 import decodebytes
import sys
from datetime import datetime
import os
from conf.config import *

cnopts = pysftp.CnOpts()

hostkeys = None

if cnopts.hostkeys.lookup(myHostname) == None:
    print('\033[32m' + "New host - will accept any host key")
    # Backup loaded .ssh/known_hosts file
    hostkeys = cnopts.hostkeys
    # And do not verify host key of the new host
    cnopts.hostkeys = None

remotePath = "./"

class Host_name_connect():
    def __init__(self):
        self.date = datetime.now().strftime('%d/%m/%Y %H:%M:%S');
        self.host = myHostname
        self.username = myUsername
        self.password = myPassword

    def connexion(self):
        with pysftp.Connection(host=self.host, username=self.username, password=self.password,  cnopts=cnopts) as sftp:
            if hostkeys != None:
                print('\033[32m' + 'Connected to new host, caching its hostkey please restart the scripts')
                hostkeys.add(myHostname, sftp.remote_server_key.get_name(), sftp.remote_server_key)
                hostkeys.save(pysftp.helpers.known_hosts())
            else:
                print('\033[32m' + self.date + ' Connection established successfully ...' + '\033[0m')
                myFileList = sftp.listdir(remotePath)
                for filename in myFileList:
                    print(filename)
                    print(os.path.isdir(remotePath))

            # print(myFileList)
            # if (filename.rfind('./' + dn) != -1):
            #     print('blablabla')
            #     sftp.get("./" + filename, "/tmp/" + filename)
