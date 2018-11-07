import requests
import json

app_id = '7d3cf58e'
app_key = '0bcae74996c617bc772af577cd0d737a'

userWord = input('Enter word for definition \n')

language = 'en'
word_id = userWord

url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

res = r.json()


print("code {}\n".format(r.status_code))
print("text \n" + r.text)
##print("json \n" + json.dumps(r.json()))





    
