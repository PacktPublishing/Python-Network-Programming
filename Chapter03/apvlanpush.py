from netmiko import ConnectHandler
import time

def apvlanpush(routerip,switchport):
    uname="cisco"
    passwd="cisco"
    device = ConnectHandler(device_type='cisco_ios', ip=routerip, username=uname, password=passwd)
    cmds="interface "+switchport
    cmds=cmds+"\nswitchport mode trunk\nswitchport trunk encapsulation dot1q\n"
    cmds=cmds+ "switchport trunk native vlan 10\nswitchport trunk allowed vlan add 10,100,200\nno shut\n"
    xcheck=device.send_config_set(cmds)
    print (xcheck)
    device.disconnect()

def validateswitchport(routerip,switchport):
    uname="cisco"
    passwd="cisco"
    device = ConnectHandler(device_type='cisco_ios', ip=routerip, username=uname, password=passwd)
    cmds="show interface "+switchport+" switchport "
    outputx=device.send_command(cmds)
    print (outputx)
    device.disconnect()
     
apvlanpush("192.168.255.245","FastEthernet2/0")
time.sleep(5) # 5 seconds
validateswitchport("192.168.255.245","FastEthernet2/0")
