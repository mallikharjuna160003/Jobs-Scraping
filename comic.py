import requests, os, bs4, threading

os.makedirs("xkcd", exist_ok=True)

def downloadXkcd(startComic, endComic):
    url = 'https://xkcd.com'
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; XKCD-Downloader/1.0)'}
    for urlNumber in range(startComic, endComic):
        print('Downloading page %s/%s' % (url, urlNumber))
        complete_url = f"{url}/{urlNumber}/"
        response = requests.get(complete_url, timeout=10)
        response.raise_for_status()
        soup = bs4.BeautifulSoup(response.text)

        # Find the URL of the comic image.
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src')
            
            # Download the image.
            print('Downloading image %s: ' %(comicUrl))
            res = requests.get("https:"+comicUrl)
            res.raise_for_status()

            # Save the image to ./xkcd
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)

            imageFile.close()


#startComic = 140
#endComic = 280
#downloadXkcd(startComic, endComic)
downloadThreads = []
for i in range(0,1400,100):
    downloadThread = threading.Thread(target=downloadXkcd, args=(i,i+99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

for downloadThread in downloadThreads:
    downloadThread.join()

print('Done.')
