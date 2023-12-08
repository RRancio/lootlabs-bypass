import requests
import re
import time

def clean_url(url):
    cleaned = re.sub(r'<.*|&quot;.*', '', url)
    return cleaned

def epl(url, delay):
    time.sleep(delay)
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

        elif res.status_code == 429:
            print("too many requests")
        else:
            print(f'error: {res.status_code}')


    except Exception as e:
        print(f'error: {e}')

if __name__ == "__main__":
    inputkjj = input("google drive: ")
    inputkjj2 = input("delay seconds: ")

    delay = int(inputkjj2)

    resp = requests.get(inputkjj)
    tc = resp.text

    urlh = re.findall(r'https://[^\s"\']+', tc)

    fu = [clean_url(url.rstrip("\\")) for url in urlh if any(keyword in url for keyword in ["loot", "link", "dest", "links", "s?"])]

    unique = list(set(fu))

    for url in unique:
        epl(url, delay)
