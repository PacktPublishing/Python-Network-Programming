from netmiko import ConnectHandler

device = ConnectHandler(device_type='cisco_ios', ip='192.168.255.249', username='cisco', password='cisco')
output = device.send_command("show version")
print (output)
device.disconnect()
