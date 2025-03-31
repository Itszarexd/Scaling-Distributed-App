import threading
import requests
from bs4 import BeautifulSoup
import time
import csv

# Lista de URLs a scrapear
urls = [
    'https://codeforces.com/',
    'https://cp-algorithms.com/',
    'https://www.educative.io/blog/scaling-in-python',
    'https://statusneo.com/concurrency-in-python-threading-processes-and-asyncio/'
]

# Almacenará los resultados
results = []

# Función para hacer scraping de una página
def scrape_page(url):
    try:
        print(f"Scraping {url}...")
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Aquí va el código para extraer los datos. Por ejemplo, extraer los títulos de artículos:
        titles = soup.find_all('h1')  # Cambia esto según el HTML de las páginas que estás scrappeando
        page_data = [title.get_text() for title in titles]

        # Guardar los resultados
        results.append({'url': url, 'titles': page_data})

        print(f"Finished scraping {url}")

    except Exception as e:
        print(f"Error scraping {url}: {e}")

# Crear hilos para cada página
def start_scraping():
    threads = []
    for url in urls:
        thread = threading.Thread(target=scrape_page, args=(url,))
        threads.append(thread)
        thread.start()

    # Esperar a que todos los hilos terminen
    for thread in threads:
        thread.join()

    print("Scraping completed.")

    # Guardar los resultados en un archivo CSV
    save_results()

# Guardar los resultados en un archivo CSV
def save_results():
    with open('scraping_results2.csv', 'w', newline='') as csvfile:
        fieldnames = ['url', 'titles']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for result in results:
            writer.writerow(result)

    print("Results saved to scraping_results.csv.")

# Ejecutar el scraper
if __name__ == "__main__":
    start_time = time.time()
    start_scraping()
    print(f"Scraping completed in {time.time() - start_time} seconds.")
