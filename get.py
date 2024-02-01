import httpx

urls = [
"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=1000&country=all&ssl=all&anonymity=all",
"https://proxyspace.pro/http.txt",
"https://www.proxy-list.download/api/v1/get?type=http",
]

with open("proxy.txt", 'w') as file:
    for url in urls:
        response = httpx.get(url)
        file.write(response.text + "\n")