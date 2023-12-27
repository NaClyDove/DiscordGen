import requests
import json
 
# Create a session object
session = requests.Session()
 
# Set the user agent for the session
session.headers.update({'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36'})
 
link = "https://discord.com/billing/partner-promotions/1180231712274387115/"
 
# Define the request headers
headers = {
    "authority": "api.discord.gx.games",
    "method": "POST",
    "path": "/v1/direct-fulfillment",
    "scheme": "https",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "da-DK,da;q=0.9,en-US;q=0.8,en;q=0.7",
    "origin": "https://www.opera.com",
    "referer": "https://www.opera.com/",
    "sec-ch-ua": '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site"
}
 
# Define the request body
body = {
    "partnerUserId": "d931f806b6707abc8983129404d7e1ed99e0db168f1a62a1e8bd3b719440e046"
}
 
# Make the POST request
response = session.post("https://api.discord.gx.games/v1/direct-fulfillment", headers=headers, json=body)
 
# Print the response
#print(response.text)
y = json.loads(response.text)
#print(y)
token = y["token"]
 
print(link + token)
