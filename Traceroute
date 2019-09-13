import os
myCmd = 'tracert -d ' + input ("Enter the IP/name: ") + ' > trace.txt && type trace.txt'
output = os.system(myCmd)
num_lines = 0
with open("trace.txt") as f:
    for line in f:
        num_lines += 1


# to print a particular line
with open("trace.txt") as f:
    lines = f.readlines()
print("Last Hop is:")
last_hop = (lines[num_lines - 4])
print(last_hop)  # or whatever you want to do with this line
last_ip = last_hop.split()
print("last IP is: " + last_ip[-1])
f.close()
