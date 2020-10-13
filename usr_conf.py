import os
from conf.sftpconfig import *



print('Welcome')
print('Please enter the hostname for SFTP :')
myHostname = input()
print('Please enter the username :')
myUsername = input()
print('Please enter the password :')
myPassword = input() 

hostname = Host_name_connect()
hostname.connexion()