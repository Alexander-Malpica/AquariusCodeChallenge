
import requests
import json

#API url, username & password
url = 'https://challenge.bitcoinatm.dev/'
username = 'alexander_malpica'
password = 'RWtRUENoWG50dw=='

# GET Ping API
#Send out request
response = requests.get(url)
print(response)

#Display Response Content
print(response.content)

# POST Login API
url_auth = url + 'auth'
print(url_auth)

headers = {
    'Authorization': 'Basic ' + username + ':' + password
}

result = requests.post(url_auth, headers=headers)

#Display Result of Response
print(result)

#Create Token
user_token = result.json()['token']
print(user_token)
token ={
    'token': user_token
}


# POST Wallet API
url_wallet = url + 'wallet/send_me_bitcoin'
print(url_wallet)

content ={
    'username': username,
    'email': 'alexander.malpica@upr.edu',
    'phone': '(787) 478-8490',
    'my_wallet_address': '3LEyNjRsoB1VXr8NQwPAsLSjHgtsiuiJTj'
}
data = json.dumps(content)

headers1 = {
    'Authorization': 'Bearer ' + str(token),
    'Content-Type': 'application/json'
}

result2 = requests.post(url_wallet, data=data, headers=headers1)
#Display Result of Response
print(result2)

success = {
    'msg': 'Congratulations you got a token.'
}
failure ={
    'msg': 'Failed to get token.'
}
