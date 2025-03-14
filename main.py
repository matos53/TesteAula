import requests

reqUrl = "https://api.github.com/octocat"

hearderList = {
    "Accept": "aplication/vnd.github+json",
    "User-Agent": "Thurder Client (https://www.thuderclient.com)",
    "X-GitHub-Aoi-Version": "2022-11-28"
    
}

payload = ""

response = requests.request("GET", reqUrl, data=payload, headers=hearderList)

print(response.text)