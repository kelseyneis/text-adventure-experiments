import requests
import asciiArt

resp = requests.get('https://duckduckgo.com/i.js?l=us-en&o=json&q=dad&vqd=3-49532440798089657093500378949342997378-271479886593792702073736046745927873658&f=size:Medium,,,&p=1')
data = resp.json()
imgResp = requests.get(data['results'][1]['url'])
if imgResp.status_code == 200:
    with open('../resources/img.png', 'wb') as f:
        for chunk in imgResp:
            f.write(chunk)

asciiArt.handle_image_conversion('../resources/img.png')
