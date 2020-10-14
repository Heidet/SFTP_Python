import paramiko
import pysftp
#from base64 import decodebytes
#import sys
from datetime import datetime
import os




class Host_name_connect:
    def __init__(self,myHostname,myUsername,myPassword):
        self.date = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        self.host = myHostname
        self.username = myUsername
        self.password = myPassword
        self.remote = './' 
        self.hostkeys = None

    def ssh_connexion(self): 
        self.cnopts = pysftp.CnOpts()
        self.hostkeys = None

        if self.cnopts.hostkeys.lookup(self.host) == None:
            print('\033[32m' + "New host - will accept any host key")
            # Backup loaded .ssh/known_hosts file
            self.hostkeys = self.cnopts.hostkeys
            # And do not verify host key of the new host
            self.cnopts.hostkeys = None

    def connexion(self):
        self.ssh_connexion()
        with pysftp.Connection(host=self.host, username=self.username, password=self.password,  cnopts=self.cnopts) as sftp:
            if self.hostkeys != None:
                print('\033[32m' + 'Connected to new host, caching its hostkey please restart the scripts')
                self.hostkeys.add(self.host, sftp.remote_server_key.get_name(), sftp.remote_server_key)
                self.hostkeys.save(pysftp.helpers.known_hosts())
            else:
                print('\033[32m' + self.date + ' Connection established successfully ...' + '\033[0m')
                myFileList = sftp.listdir(self.remote)
                for filename in myFileList:
                    print(filename)
                    print(os.path.isdir(self.remote))

            # print(myFileList)
            # if (filename.rfind('./' + dn) != -1):
            #     print('blablabla')
            #     sftp.get("./" + filename, "/tmp/" + filename)

