import requests
from requests.structures import CaseInsensitiveDict
url = "http://accounts.robloxalts.info/api/public/demand/generate"
headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
data = '{"apikey":"YOUR API KEY HERE","amount":2}'
resp = requests.post(url, data=data).json().get("accounts")
for account in resp:
    print("{}:{}".format(account["username"], account["password"]))
