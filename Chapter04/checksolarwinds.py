from orionsdk import SwisClient
import requests

npm_server = 'myserver'
username = "username"
password = "password"

verify = False
if not verify:
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

swis = SwisClient(npm_server, username, password)

results = swis.query("SELECT NodeID, DisplayName FROM Orion.Nodes Where Vendor= 'Cisco'")

for row in results['results']:
    print("{NodeID:<5}: {DisplayName}".format(**row))
