import requests

cookies = {
'__cfduid': 'd7631a89a3960c3a50720b6976c05826e1553345678',
}

headers = {
'Host': 'ipltmv.com',
'Cache-Control': 'max-age=0',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
}

response = requests.get('http://ipltmv.com/js.php', headers=headers, cookies=cookies).content
print(response)
