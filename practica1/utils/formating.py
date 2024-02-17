import urllib.parse

def normalize_url(url, path):
    if path[0] == "/" or path[0] == "#":
        return urllib.parse.urljoin(url, path)
    return path

def obtain_link(result, url):
    return list(map(lambda x: normalize_url(url, x.attrs['href']), filter(lambda x: 'href' in x.attrs, result)))