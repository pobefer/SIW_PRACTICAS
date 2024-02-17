import time
from collections import deque
import requests
from bs4 import BeautifulSoup
from utils.formating import obtain_link
from utils.robots import can_fetch
from utils.export import export_to_file


def crawl_h_iterative(urls, delay, max_downloads) -> None:
    """
    Realiza un crawling iterativo en profundidad de las URLs dadas.
    :param urls: Lista inicial de URLs a rastrear.
    :param delay: Retardo entre peticiones consecutivas.
    :param max_downloads: Número máximo de páginas a descargar.
    """
    resources_download = []
    stack = urls[:]
    current_downloads = 0

    while stack and current_downloads < max_downloads:
        url = stack.pop()
        try:
            if url in resources_download:
                continue
            if not can_fetch(url):
                print(f"No se puede descargar la url: {url}, lo impide robots.txt")
                continue
            response = requests.get(url)
            resources_download.append(url)
            current_downloads += 1
            print(f"Descargado: {url}")
        except requests.RequestException as e:
            print(f"Error al descargar {url}: {e}")
            continue

        soup = BeautifulSoup(response.content, 'html.parser')
        a_tags = soup.find_all('a')
        hrefs = obtain_link(a_tags, url)

        stack.extend(hrefs)

        if current_downloads >= max_downloads:
            export_to_file(resources_download)
            break

        time.sleep(delay)

    print(f"Descargas completadas: {current_downloads}")


def crawl_h_recursive(urls: [], delay: int, max_downloads: int, downloads_count=None, resources_download=None) -> None:
    """
    Realiza un crawling recursivo en profundidad de las URLs dadas.
    :param resources_download:
    :param downloads_count:
    :param urls: Lista inicial de URLs a rastrear.
    :param delay: Retardo entre peticiones consecutivas.
    :param max_downloads: Número máximo de páginas a descargar.
    """
    if downloads_count is None:
        downloads_count = {"current": 0}
    if resources_download is None:
        resources_download = {"current": []}
    if downloads_count["current"] >= max_downloads:
        export_to_file(resources_download)
        return

    for url in urls:
        if downloads_count["current"] >= max_downloads:
            export_to_file(resources_download)
            break

        try:
            if url in resources_download["current"]:
                continue
            if not can_fetch(url):
                print(f"No se puede descargar la url: {url}, lo impide robots.txt")
                continue
            print(f"Descargado: {url}")
            response = requests.get(url)
            resources_download["current"].append(url)
            downloads_count["current"] += 1
        except requests.RequestException as e:
            print(f"Error al descargar {url}: {e}")
            continue

        soup = BeautifulSoup(response.content, 'html.parser')
        a_field = soup.find_all('a')

        hrefs = obtain_link(result=a_field, url=url)

        time.sleep(delay)
        crawl_h_recursive(urls=hrefs,
                          delay=delay,
                          max_downloads=max_downloads,
                          downloads_count=downloads_count,
                          resources_download=resources_download)


def crawl_v(urls, delay, max_downloads) -> None:
    """
    Realiza un crawling en anchura (BFS) de las URLs dadas.
    :param urls: Lista inicial de URLs a rastrear.
    :param delay: Retardo entre peticiones consecutivas.
    :param max_downloads: Número máximo de páginas a descargar.
    """
    resources_download = []
    queue = deque(urls)
    current_downloads = 0

    while queue and current_downloads < max_downloads:
        url = queue.popleft()
        try:
            if url in resources_download:
                continue
            if not can_fetch(url):
                print(f"No se puede descargar la url: {url}, lo impide robots.txt")
                continue
            response = requests.get(url)
            resources_download.append(url)
            current_downloads += 1
            soup = BeautifulSoup(response.content, 'html.parser')
            a_field = soup.find_all('a')
            hrefs = obtain_link(a_field, url)

            for href in hrefs:
                if href not in queue:
                    queue.append(href)

            print(f"Descargado: {url}")
            time.sleep(delay)

        except requests.RequestException as e:
            print(f"Error al descargar {url}: {e}")
            continue
    export_to_file(resources_download)

    print(f"Descargas completadas: {current_downloads}")
