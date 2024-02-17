import sys
import os
import json
from crawler import crawl_v, crawl_h_recursive, crawl_h_iterative

if __name__ == "__main__":

    # if len(sys.argv) != 5:
    #     print("Uso: script.py <ruta_del_archivo> <max_descargas> <segundos_espera> <tipo de busqueda [0, 1, 2]>")
    #     sys.exit(1)

    file_path = 'data/urls.json'  #sys.argv[1]
    max_downloads_str = 10# sys.argv[2]
    wait_seconds_str = 1#sys.argv[3]
    kind = 0#sys.argv[4]

    # Verificar que el archivo exista
    if not os.path.isfile(file_path):
        print(f"Error: El archivo especificado no existe: {file_path}")
        sys.exit(1)
    else:
        with open(file_path, 'r') as archivo:
            datos = json.load(archivo)
            list_url = datos["urls"]

    # Verificar que el máximo de descargas sea un número entero
    try:
        max_downloads = int(max_downloads_str)
    except ValueError:
        print("Error: El número máximo de descargas debe ser un número entero.")
        sys.exit(1)

    # Verificar que los segundos de espera sean un número entero
    try:
        wait_seconds = int(wait_seconds_str)
    except ValueError:
        print("Error: El número de segundos de espera debe ser un número entero.")
        sys.exit(1)

    try:
        kind = int(kind)
    except ValueError:
        print("Error: Este parametro indica el tipo de busqueda: 0 {iterativa anchura}, 1 {recursiva profundidad}, 2 {iterativa profundidad}")
        sys.exit(1)
        
    if kind == 0:
        crawl_v(urls=list_url,
                delay=wait_seconds,
                max_downloads=max_downloads)
    if kind == 1:
        crawl_h_recursive(urls=list_url,
                delay=wait_seconds,
                max_downloads=max_downloads)
    if kind == 2:
        crawl_h_iterative(urls=list_url,
                delay=wait_seconds,
                max_downloads=max_downloads)