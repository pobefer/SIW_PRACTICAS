import time
import dask
import dask.bag as db
from simhash import Simhash, SimhashIndex

def calcular_simhash(elemento):
    elemento, value = elemento
    firma = Simhash(value, f=valor_f)
    return elemento, firma

def obtener_duplicados(elemento):
    elemento, value = elemento
    firma = Simhash(value, f=valor_f)
    duplicados = indice.get_near_dups(firma)
    return elemento, duplicados

def filtrar_y_modificar(elemento):
    elemento, value = elemento
    nuevo_value = [val for val in value if val != elemento]
    return elemento, nuevo_value

valor_f = 128

if __name__ == '__main__':
    inicio = time.time()

    # Leer el archivo de texto y crear una Dask Bag
    bag = db.read_text('data/articles_10000.train', blocksize='5MB').map(lambda x: x.strip().split(' ', 1))

    # Ajustar el número de workers
    dask.config.set(scheduler='processes', num_workers=6)

    # Generar firmas y crear el índice
    firmas = bag.map(calcular_simhash)
    firmas = firmas.persist()

    indice = SimhashIndex(firmas.compute(), k=10, f=valor_f)

    # Calcular duplicados y filtrarlos
    observaciones = bag.map(obtener_duplicados).filter(lambda x: len(x[1]) > 1)

    # Filtrar y modificar las observaciones
    resultados = observaciones.map(filtrar_y_modificar).compute()

    fin = time.time()

    print(f"tiempo de ejecucion -> {str(fin-inicio)}")
    print(resultados)
