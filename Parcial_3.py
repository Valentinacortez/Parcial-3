import concurrent.futures
import time
import random

def entrega(distribuidor, direccion):
    print(f"{distribuidor} está entregando un paquete a {direccion}...")
    tiempo_entrega = random.randint(2, 5)
    time.sleep(tiempo_entrega)
    print(f"{distribuidor} ha entregado el paquete en {direccion} tras {tiempo_entrega} segundos.")

distribuidores = ["Distribuidor 1", "Distribuidor 2", "Distribuidor 3", "Distribuidor 4"]
direcciones = ["Calle A", "Calle B", "Calle C", "Calle D"]

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(entrega, distribuidores, direcciones)