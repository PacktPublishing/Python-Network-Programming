from orionsdk import SwisClient

npm_server = 'mysolarwindsserver'
username = "test"
password = "test"

verify = False
if not verify:
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

swis = SwisClient(npm_server, username, password)

print("My IPAM test:")
results=swis.query("SELECT TOP 1 Status, DisplayName FROM IPAM.IPNode WHERE Status=2")
print (results)

### for a formatted printing
for row in results['results']:
 print("Avaliable: {DisplayName}".format(**row))
