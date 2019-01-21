from netmiko import ConnectHandler
import time

def pushbgpconfig(routerip,remoteip,localas,remoteas,newconfig="false"):
    uname="cisco"
    passwd="cisco"
    device = ConnectHandler(device_type='cisco_ios', ip=routerip, username=uname, password=passwd)
    cmds=""
    cmds="router bgp "+localas
    cmds=cmds+"\n neighbor "+remoteip+" remote-as "+remoteas
    xcheck=device.send_config_set(cmds)
    print (xcheck)
    outputx=device.send_command("wr mem")
    print (outputx)
    device.disconnect()


def validatebgp(routerip,remoteip):
    uname="cisco"
    passwd="cisco"
    device = ConnectHandler(device_type='cisco_ios', ip=routerip, username=uname, password=passwd)
    cmds="show ip bgp neighbors "+remoteip+" | include BGP state"
    outputx=device.send_command(cmds)
    if ("Established" in outputx):
        print ("Remote IP "+remoteip+" on local router "+routerip+" is in ESTABLISHED state")
    else:
        print ("Remote IP "+remoteip+" on local router "+routerip+" is NOT IN ESTABLISHED state")
    device.disconnect()
    
pushbgpconfig("192.168.255.249","192.168.255.248","200","200")
### we give some time for bgp to establish
print ("Now sleeping for 5 seconds....")
time.sleep(5) # 5 seconds
validatebgp("192.168.255.249","192.168.255.248")
