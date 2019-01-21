#!/usr/bin/env python
import re
import sys
import os
import time
from netmiko import ConnectHandler
from threading import Thread
from random import randrange
username="cisco"
password="cisco"

splitlist = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]

returns = {}
resultoutput={}
devlist=[]
cmdlist=""

       
def fetchallvalues(sourceip,sourcelist,delay,cmddelay):
    print ("checking for....."+sourceip)
    cmdend=" repeat 10" # this is to ensure that we ping for 10 packets
    splitsublist=splitlist(sourcelist,6) # this is to ensure we open not more than 6 sessions on router at a time
    threads_imagex= []
    for item in splitsublist:
        t = Thread(target=fetchpingvalues, args=(sourceip,item,cmdend,delay,cmddelay,))
        t.start()
        time.sleep(randrange(1,2,1)/20)
        threads_imagex.append(t)

    for t in threads_imagex:
        t.join()
  
    
def fetchpingvalues(devip,destips,cmdend,delay,cmddelay):
    global resultoutput
    ttl="0"
    destip="none"
    command=""
    try:
        output=""
        device = ConnectHandler(device_type='cisco_ios', ip=devip, username=username, password=password, global_delay_factor=cmddelay)
        time.sleep(delay)
        device.clear_buffer()
        for destip in destips:
            command="ping "+destip+" source "+devip+cmdend
            output = device.send_command_timing(command,delay_factor=cmddelay)
            if ("round-trip" in output):
                resultoutput[devip+":"+destip]="True"
            elif ("Success rate is 0 percent" in output):
                resultoutput[devip+":"+destip]="False"
        device.disconnect()
    except:
        print ("Error connecting to ..."+devip)
        for destip in destips:
            resultoutput[devip+":"+destip]="False"


def getallvalues(allips):
    global resultoutput
    threads_imagex= []
    for item in allips:
        #print ("calling "+item)
        t = Thread(target=fetchallvalues, args=(item,allips,2,1,))
        t.start()
        time.sleep(randrange(1,2,1)/30)
        threads_imagex.append(t)
    for t in threads_imagex:
        t.join()
    dnew=sorted(resultoutput.items()) 
    return dnew


#print (getallvalues(["192.168.255.240","192.168.255.245","192.168.255.248","192.168.255.249","4.2.2.2"]))
