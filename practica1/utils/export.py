import requests
from warcio import WARCWriter
from warcio.statusandheaders import StatusAndHeaders
from io import BytesIO

def export_to_file(urls):
    """
    Export all files from a domain into a warcio file
    :param urls: urls to download
    :return:
    """
    archivo_warc = "./data/descargas.warc"
    with open(archivo_warc, 'wb') as output:
        writer = WARCWriter(output, gzip=True)

        for url in urls:
            try:
                resp = requests.get(url, timeout=10)
                http_headers = StatusAndHeaders('200 OK', resp.headers.items(), protocol='HTTP/1.0')

                payload = BytesIO(resp.content)
                
                record = writer.create_warc_record(url, 'response',
                                                   payload=payload,
                                                   http_headers=http_headers,
                                                   warc_content_type='application/http; msgtype=response')
                writer.write_record(record)
                print(f"generando: {url} -> {archivo_warc}")
            except requests.RequestException as e:
                print(f"Error al descargar {url}: {e}")
            except Exception as ex:
                print(f"{ex}")
