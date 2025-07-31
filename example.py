import requests


url = 'https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv'

response = requests.get(url)
with open('GLB.Ts+dSST.csv', 'wb') as f:
    f.write(response.content)

print("Downloaded GLB.Ts+dSST.csv")
