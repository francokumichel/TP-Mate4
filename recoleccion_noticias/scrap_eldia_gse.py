from googleapiclient.discovery import build
from dotenv import load_dotenv
import os
import time
import csv

load_dotenv()

API_KEY = os.getenv('API_KEY')
CX = os.getenv('CX')

def buscar(query, max_results=100):
    service = build("customsearch", "v1", developerKey=API_KEY)
    resultados = []

    for start in range(1, max_results, 10):
        res = service.cse().list(
            q=query,
            cx=CX,
            start=start
        ).execute()

        items = res.get('items', [])
        resultados.extend(items)

        time.sleep(1)

        if 'nextPage' not in res.get('queries', {}):
            break

    return resultados

def guardar_en_csv(resultados, nombre_archivo="resultados.csv"):
    with open(nombre_archivo, mode="w", newline='', encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["Fecha", "Título", "Link"])  # encabezados
        
        for item in resultados:
            titulo = item.get("title", "")
            link = item.get("link", "")
            fecha = item.get("pagemap", {}).get("metatags", [{}])[0].get("article:published_time", "")
            writer.writerow([fecha, titulo, link])

if __name__ == "__main__":
    query = 'Inundacion La Plata'
    resultados = buscar(query, max_results=100)
    guardar_en_csv(resultados)

    for item in resultados:
        print(f"- {item['title']}\n  {item['link']}\n")
