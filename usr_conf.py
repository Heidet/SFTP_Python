import os
from conf.sftpconfig import Host_name_connect



print('Welcome')
print('Please enter the hostname for SFTP :')
myHostname = input()
print('Please enter the username :')
myUsername = input()
print('Please enter the password :')
myPassword = input() 

hostname = Host_name_connect(myHostname,myUsername,myPassword)
hostname.connexion()
