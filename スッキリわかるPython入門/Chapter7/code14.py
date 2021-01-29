import http.client
conn = http.client.HTTPSConnection('www.python.org')
conn.request('GET', '/downloads/')
response = conn.getresponse()
text = response.read().decode('UTF-8')
print(text)
conn.close()
