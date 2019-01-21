from netmiko import ConnectHandler
import time

def ipphoneconfig(routerip,switchport):
    uname="cisco"
    passwd="cisco"
    device = ConnectHandler(device_type='cisco_ios', ip=routerip, username=uname, password=passwd)
    cmds="interface "+switchport
    cmds=cmds+"\nswitchport mode access\nswitchport access vlan 100\n"
    cmds=cmds+ "switchport voice vlan 200\nspanning-tree portfast\nno shut\n"
    xcheck=device.send_config_set(cmds)
    print (xcheck)
    device.disconnect()

def validateswitchport(routerip,switchport):
    print ("\nValidating switchport...."+switchport)
    uname="cisco"
    passwd="cisco"
    device = ConnectHandler(device_type='cisco_ios', ip=routerip, username=uname, password=passwd)
    cmds="show interface "+switchport+" switchport "
    outputx=device.send_command(cmds)
    print (outputx)
    outputx=outputx.split("\n")
    for line in outputx:
        if ("Trunking Native Mode VLAN: 10" in line):
            changenativevlan(routerip,switchport,"20")
    device.disconnect()
     
ipphoneconfig("192.168.255.245","FastEthernet2/5")
time.sleep(5) # 5 seconds
validateswitchport("192.168.255.245","FastEthernet2/5")
