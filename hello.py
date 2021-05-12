import requests
url = 'https://replier.herokuapp.com/' ##change rasablog with your app name
myobj = {
"message": "hi",
"sender": 1,
}
x = requests.post(url, json = myobj)
print(x.text)
