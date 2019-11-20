import os
import netmiko
from netmiko import ConnectHandler
CHG = input("CHGXXXXXXXXX : ")

UN = input("Username : ")
PW = getpass.getpass("Password : ")

with open ("device.txt") as f:
        content = f.readlines()
        f.close()


for ip in content:
    print ("print the device ip:"+ip)
    print (ip)
    device = ConnectHandler(device_type='cisco_ios',ip, port=22, username=UN, password=PW)
    output = device.send_command("show run | i  user")
    print ("---------Local Credentials Before Change--------")
    print (output)
    config_commands = ['username xxxx privilege 15 secret xxxx']
    output1	= device.send_config_set(config_commands)
    print (output1)
    output2 = device.send_command("show run | i  user")
    print ("---------Local Credentials After Change--------")
    print (output2)
    f = open(CHG + ".txt" , "a" )
    f.write(output)
    f.write(output1)
    f.write(output2)
    f.close()
    device.disconnect()
