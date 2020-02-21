# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 14:59:45 2020

@author: Ankit
"""

import paramiko
import time
import getpass
import os



CHG = input("CHGXXXXXXXXX : ")

with open ("device.txt") as f:
        content = f.readlines()
        f.close()

for ip_address in content:
    ip_address=ip_address.strip('\n')
    print (ip_address)
    
    #printing the new device name
    f = open(CHG + ".txt" , "a" )
    f.write('\n')
    f.write("*********************************************************************")
    f.write('\n')
    f.write(ip_address)
    f.write('\n')
    f.close()
    
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip_address,port=22, username='admin', password='Cisco@123')
        remote = ssh.invoke_shell()
        remote.send('term len 0\n')
        time.sleep(1)
    
        remote.send("conf t\n")
        time.sleep(2)
        buf = remote.recv(65000).decode('utf-8')
        print (buf)
        f = open(CHG + ".txt" , "a" )
        f.write(buf)
        f.close()
        
        remote.send("no cdp enable\n")
        time.sleep(2)
        buf = remote.recv(65000).decode('utf-8')
        print (buf)
        f = open(CHG + ".txt" , "a" )
        f.write(buf)
        f.close()
    
        remote.send("no cdp run\n")
        time.sleep(2)
        buf = remote.recv(65000).decode('utf-8')
        print (buf)
        f = open(CHG + ".txt" , "a" )
        f.write(buf)
        f.close()
        
        
        remote.send("cdp enable\n")
        time.sleep(2)
        buf = remote.recv(65000).decode('utf-8')
        print (buf)
        f = open(CHG + ".txt" , "a" )
        f.write(buf)
        f.close()
    
        remote.send("cdp run\n")
        time.sleep(2)
        buf = remote.recv(65000).decode('utf-8')
        print (buf)
        f = open(CHG + ".txt" , "a" )
        f.write(buf)
        f.close()
    
        ssh.close()
    
    except paramiko.ssh_exception.AuthenticationException:
        print("Authentication failed, please verify your credentials: %s")
    except paramiko.ssh_exception.SSHException as sshException:
        print("Unable to establish SSH connection: %s" % sshException)
    except paramiko.ssh_exception.BadHostKeyException as badHostKeyException:
        print("Unable to verify server's host key: %s" % badHostKeyException)
    except paramiko.ssh_exception.NoValidConnectionsError:
        print("Unable to connect to port 22")	
    finally:
        pass
