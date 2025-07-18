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

# Extraemos resultados de la primera página
extraer_resultados()

# Recorremos las demás páginas
while True:
    try:
        paginador = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.gsc-cursor-box")))
        pagina_actual = paginador.find_element(By.CSS_SELECTOR, "div.gsc-cursor-current-page").text

        paginas = paginador.find_elements(By.CSS_SELECTOR, "div.gsc-cursor-page")
        proxima = None
        for p in paginas:
            if int(p.text) > int(pagina_actual):
                proxima = p
                break

        if not proxima:
            break  # Esto por si es la última página

        # Guardar el primer título antes de hacer clic
        titulos_antes = [n.text.strip() for n in driver.find_elements(By.CSS_SELECTOR, "a.gs-title") if n.text.strip()]
        driver.execute_script("arguments[0].click();", proxima)

        # Esperar hasta que el contenido cambie (comparando los títulos)
        WebDriverWait(driver, 10).until(
            lambda d: any(n.text.strip() not in titulos_antes for n in d.find_elements(By.CSS_SELECTOR, "a.gs-title"))
        )

        extraer_resultados()

    except Exception as e:
        print(f"Error al avanzar de página: {e}")
        break

# Imprimir resultados
print(f"\n Noticias encontradas: {len(resultados)}\n")
for titulo, link in resultados:
    print(f"Título: {titulo}\nLink: {link}\n")

driver.quit()
