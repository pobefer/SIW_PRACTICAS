import urllib.robotparser
from urllib import parse


def obtain_robots_file(url):
    partes_url = parse.urlparse(url)
    url_base = partes_url.scheme + "://" + partes_url.netloc
    url_robots = parse.urljoin(url_base, "robots.txt")
    return url_robots


def can_fetch(url):
    rp = urllib.robotparser.RobotFileParser()

    rp.set_url(obtain_robots_file(url))
    rp.read()

    user_agent = 'MyCrawler'

    if rp.can_fetch(user_agent, url):
        return True
    else:
        return False
