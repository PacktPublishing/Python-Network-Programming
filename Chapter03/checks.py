#!/usr/bin/env python
import cgi
import paramiko
import time
import re
import sys
import os
import requests
import urllib
import datetime
from datetime import datetime
from threading import Thread
from random import randrange

form = cgi.FieldStorage()
searchterm = form.getvalue('searchbox')
cmds = form.getvalue('cmds')
changeid = form.getvalue('changeid')
prepost=form.getvalue('prepost')
searchterm=searchterm.split(",")
xval=""
xval=datetime.now().strftime("%Y-%m-%d_%H_%M_%S")

returns = {}
def getoutput(devip,cmd):
    try:
        output=""
        mpath="C:/iistest/logs/"
        fname=changeid+"_"+devip+"_"+prepost+"_"+xval+".txt"
        fopen=open(mpath+fname,"w")
        remote_conn_pre = paramiko.SSHClient()
        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        remote_conn_pre.connect(devip, username='cisco', password='cisco', look_for_keys=False, allow_agent=False)
        remote_conn = remote_conn_pre.invoke_shell()
        remote_conn.settimeout(60)
        command=cmd
        remote_conn.send(command+"\n")
        time.sleep(15)
        output=(remote_conn.recv(250000)).decode()
        fopen.write(output)
        remote_conn.close()
        fopen.close()
        returns[devip]=("Success: <a href='http://localhost/test/logs/"+fname+"' target='_blank'>"+fname +"</a> Created")
    except:
        returns[devip]="Error. Unable to fetch details"

try:
    xtmp=""
    cmdval="terminal length 0\n"
    if (str(cmds).count("show") > 1):
        for cmdvalue in cmds:
            if ("show" in cmdvalue):
                if ("show log" in cmdvalue):
                    cmdvalue="terminal shell\nshow log | tail 100"
                cmdval=cmdval+cmdvalue+"\n\n"
    else:
        if ("show" in cmds):
            if ("show log" in cmds):
                cmds="terminal shell\nshow log | tail 100"
            cmdval=cmdval+cmds+"\n\n"
    threads_imagex= []
    for devip in searchterm:
        devip=devip.strip()
        t = Thread(target=getoutput, args=(devip,cmdval,))
        t.start()
        time.sleep(randrange(1,2,1)/20)
        threads_imagex.append(t)
    
    for t in threads_imagex:
        t.join()
        
    print("Content-type: text/html")
    print()
    xval=""
    for key in returns:
        print ("<b>"+key+"</b>:"+returns[key]+"<br>")
        
    print ("<br>Next step: <a href='http://localhost/test/selectfiles.aspx'> Click here to compare files </a>")
    print ("<br>Next step: <a href='http://localhost/test/prepostcheck.html'> Click here to perform pre/post check </a>")

except:
    print("Content-type: text/html")
    print()
    print("Error fetching details. Need manual validation")
    print ("<br>Next step: <a href='http://localhost/test/selectfiles.aspx'> Click here to compare files </a>")
    print ("<br>Next step: <a href='http://localhost/test/prepostcheck.html'> Click here to perform pre/post check </a>")
