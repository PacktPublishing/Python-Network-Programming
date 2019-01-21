from netmiko import ConnectHandler

device = ConnectHandler(device_type='cisco_ios', ip='192.168.255.249', username='cisco', password='cisco')

def task1():
    output = device.send_command("show version")
    print (output)
    output= device.send_command("show ip int brief")
    print (output)
    output= device.send_command("show clock")
    print (output)
    output= device.send_command("show running-config | in username")
    output=output.splitlines()
    for item in output:
        if ("username" in item):
            item=item.split(" ")
            print ("username configured: ",item[1])
            

def task2():
    global device
    configcmds=["username test privilege 15 secret test"]
    device.send_config_set(configcmds)
    output= device.send_command("show running-config | in username")
    output=output.splitlines()
    for item in output:
        if ("username" in item):
            item=item.split(" ")
            print ("username configured: ",item[1])
    device.disconnect()
    try:
        device = ConnectHandler(device_type='cisco_ios', ip='192.168.255.249', username='test', password='test')
        print ("Authenticated successfully with username test")
        device.disconnect()
    except:
        print ("Unable to authenticate with username test")

def task3():
    device = ConnectHandler(device_type='cisco_ios', ip='192.168.255.249', username='test', password='test')
    output= device.send_command("show running-config | in username")
    output=output.splitlines()
    for item in output:
        if ("username" in item):
            if ("test" not in item):
                item=item.split(" ")
                cmd="no username "+item[1]
                outputnew=device.send_config_set(cmd)
    output= device.send_command("show running-config | in username")
    output=output.splitlines()
    for item in output:
        if ("username" in item):
            item=item.split(" ")
            print ("username configured: ",item[1])
            
    device.disconnect()
    
    
#Call task1 by writing task1()
#task1()
#Call task2 by writing task2()
#task2()
#Call task3 by writing task3()
#task3()
