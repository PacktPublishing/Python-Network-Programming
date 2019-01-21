from netmiko import ConnectHandler
import itertools
import re

class linecheck:
    def __init__(self):
        self.state = 0
    def __call__(self, line):
        if line and not line[0].isspace():
            self.state += 1
        return self.state

def getbgpipaddress(routerip):
    uname="cisco"
    passwd="cisco"
    device = ConnectHandler(device_type='cisco_ios', ip=routerip, username=uname, password=passwd)
    cmds="show running-config"
    outputx=device.send_command(cmds)
    device.disconnect()
    for _, group in itertools.groupby(outputx.splitlines(), key=linecheck()):
        templist=list(group)
        if (len(templist) == 1):
            if "!" in str(templist):
                continue 
        if "router bgp" in str(templist):
            for line in templist:
                if ("neighbor " in line):
                    remoteip=re.search("\d+.\d+.\d+.\d+",line)
                    print ("Remote ip: "+remoteip.group(0))


getbgpipaddress("192.168.255.249")
