from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuramos Selenium
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15)

# Navegamos al sitio
driver.get("https://www.eldia.com/")

# Hacemos clic en el botón de búsqueda
search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.buscar.b_buscar")))
driver.execute_script("arguments[0].click();", search_button)

# Hay que esperar a que aparezca el input de búsqueda
search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='search']")))

# Escribimos en el inpuy y le damos enter para buscar
search_input.send_keys("Inundación La Plata")
search_input.send_keys(Keys.RETURN)

# Esperar a que aparezcan los resultados
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.gsc-results")))

resultados = set()

def extraer_resultados():
    noticias = driver.find_elements(By.CSS_SELECTOR, "a.gs-title")
    for n in noticias:
        href = n.get_attribute("href")
        titulo = n.text.strip()
        if href and "La Plata" in titulo and "inundación" in titulo.lower():
            resultados.add((titulo, href))

# Recorremos las páginas dinámicamente
pagina_actual = 1
while True:
    try:
        print(f"Procesando página {pagina_actual}...")

        # Esperamos que haya resultados visibles
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.gsc-webResult")))

        extraer_resultados()

        # Reobtener el paginador en cada iteración
        paginador = driver.find_element(By.CSS_SELECTOR, "div.gsc-cursor-box")
        paginas = paginador.find_elements(By.CSS_SELECTOR, "div.gsc-cursor-page")

        # Buscar el botón de la siguiente página
        siguiente = None
        for p in paginas:
            if p.text.strip() == str(pagina_actual + 1):
                siguiente = p
                break

        if not siguiente:
            print("Última página alcanzada.")
            break

        driver.execute_script("arguments[0].click();", siguiente)
        pagina_actual += 1

        # Esperar hasta que el contenido cambie
        WebDriverWait(driver, 10).until(
            lambda d: str(pagina_actual) in [e.text.strip() for e in d.find_elements(By.CSS_SELECTOR, "div.gsc-cursor-current-page")]
        )
        time.sleep(10)

    except Exception as e:
        print(f"Error al avanzar de página: {e}")
        break

# Imprimir resultados
print(f"\n Noticias encontradas: {len(resultados)}\n")
for titulo, link in resultados:
    print(f"Título: {titulo}\nLink: {link}\n")

driver.quit()
