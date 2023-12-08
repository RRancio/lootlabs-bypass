import requests
import re

def clean_url(url):
    cleaned = re.sub(r'<.*|&quot;.*', '', url)
    return cleaned

def epl(url):
    try:
        res = requests.get(url)

        if res.status_code == 200:
            match = re.search(r"p\['PUBLISHER_LINK'\] = '(.*?)'", res.text)

            if match:
                pl = match.group(1)
                cpl = clean_url(pl)
                print(cpl)
            else:
                print('not supported link found')

        else:
            print(f'error: {res.status_code}')

    except Exception as e:
        print(f'error: {e}')

if __name__ == "__main__":
    inputkjj = input("google drive: ")

    resp = requests.get(inputkjj)
    tc = resp.text

    urlh = re.findall(r'https://[^\s"\']+', tc)

    fu = [clean_url(url.rstrip("\\")) for url in urlh if any(keyword in url for keyword in ["loot", "link", "dest"])]

    unique = list(set(fu))

    for url in unique:
        epl(url)