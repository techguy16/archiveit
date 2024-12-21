import requests,json,handlers.data

def request_availability(url):
    if "?v=" in url:
        url = url.split("?v=")[1]
    info = requests.get(f"https://archive.org/wayback/available?url=https://wayback-fakeurl.archive.org/yt/{url}", headers=handlers.data.requestparams).json()
    if info["archived_snapshots"] != {}:
        return info["archived_snapshots"]["closest"]["url"]
    return False

def download_video(url,save):
    data = requests.get(url)
    with open(save, "wb") as w:
        w.write(data.content)
        w.close()