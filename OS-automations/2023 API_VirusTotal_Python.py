# Basado en https://www.youtube.com/watch?v=1FCSqV__Ot0
# usamos la API de virustotal para enviar un archivo, virustotal nos responde con un diccionario en el que interpretaremos los resultados

import hashlib
from virus_total_apis import PublicApi
import os

API KEY = #PONER AQUI NUESTRA KEY
api = PublicApi(API_KEY)

with open("virus.exe" ,"rb") as file:
    file_hash = hash1ib.md5(fi1e.read()).hexdigest()
response = api.get_file_report(file_hash)

if response["response_code"] == 200: # response 200 es que el escaneo se hizo OK
    if response["results"]["positives"] > 5: # Al menos 5 AV lo detecta como malicioso
        print("Archivo malicioso. Lo elimino")
        os.remove('virus.exe')
    else:
        print("Archivo seguro.") # Si ningun AV ve nada
else:
    print("No ha podido obtenerse el análisis del archivo.") 