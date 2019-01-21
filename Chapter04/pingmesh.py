import getmeshvalue
from getmeshvalue import getallvalues

getdevinformation={}
devicenamemapping={}
arraydeviceglobal=[]
pingmeshvalues={}

arraydeviceglobal=["192.168.255.240","192.168.255.245","192.168.255.248","192.168.255.249","4.2.2.2"]

devicenamemapping['192.168.255.240']="R1"
devicenamemapping['192.168.255.245']="R2"
devicenamemapping['192.168.255.248']="R3"
devicenamemapping['192.168.255.249']="R4"
devicenamemapping['4.2.2.2']="Random"

def getmeshvalues():
        global arraydeviceglobal
        global pingmeshvalues
        arraydeviceglobal=sorted(set(arraydeviceglobal))
        tval=getallvalues(arraydeviceglobal)
        pingmeshvalues = dict(tval)

getmeshvalues()

def createhtml():
    global arraydeviceglobal
    fopen=open("C:\pingmesh\pingmesh.html","w") ### this needs to be changed as web path of the html location

    head="""<html><head><meta http-equiv="refresh" content="60" ></head>"""
    head=head+"""<script type="text/javascript">
function updatetime() {
    var x = new Date(document.lastModified);
    document.getElementById("modified").innerHTML = "Last Modified: "+x+" ";
}
</script>"""+"<body onLoad='updatetime();'>"
    head=head+"<div style='display: inline-block;float: right;font-size: 80%'><h4><h4><p id='modified'></p></div>"
    head=head+"<div style='display: inline-block;float: left;font-size: 90%'></h4><center><h2>Network Health Dashboard<h2></div>"
    head=head+"<br><div><table border='1' align='center'><caption><b>Ping Matrix</b></caption>"
    head=head+"<center><br><br><br><br><br><br><br><br>"
    fopen.write(head)
    dval=""
    fopen.write("<tr><td>Devices</td>")
    for fromdevice in arraydeviceglobal:
        fopen.write("<td><b>"+devicenamemapping[fromdevice]+"</b></td>")
    fopen.write("</tr>")
    for fromdevice in arraydeviceglobal:
        fopen.write("<tr>")
        fopen.write("<td><b>"+devicenamemapping[fromdevice]+"</b></td>")
        for todevice in arraydeviceglobal:
            askvalue=fromdevice+":"+todevice
            if (askvalue in pingmeshvalues):
                getallvalues=pingmeshvalues.get(askvalue)
                bgcolor='lime'
                if (getallvalues == "False"):
                    bgcolor='salmon'
            fopen.write("<td align='center' font size='2' height='2' width='2' bgcolor='"+bgcolor+"'title='"+askvalue+"'>"+"<font color='white'><b>"+getallvalues+"</b></font></td>")
        fopen.write("</tr>\n")
    fopen.write("</table></div>")
    fopen.close()
    
createhtml()


print("All done!!!!")
