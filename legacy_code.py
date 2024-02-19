# import re
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pandas as pd
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
#
# # Configurar opciones de Chrome
# # chrome_options = Options()
# # chrome_options.add_argument("--user-data-dir=C:\\Users\\hecto\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
# # # Configurar el web driver con las opciones de Chrome
# # driver = webdriver.Chrome(options=chrome_options)
# page = 0
#
# driver = webdriver.Chrome()
# # driver.implicitly_wait(30)  # Aumenta el tiempo de espera implícito a 30 segundos
# driver.get(f"https://www.linkedin.com/search/results/people/?geoUrn=%5B%22105646813%22%5D&keywords=consultoria&origin=FACETED_SEARCH&page={str(page)}&profileLanguage=%5B%22es%22%5D&sid=qz*&titleFreeText=CEO")
# # Aceptar las cookies
# # cookies_accept_btn = WebDriverWait(driver, 15).until(
# #     EC.element_to_be_clickable((By.XPATH, "//*[@id='solvia-app']/solvia-cookies-policy/solvia-simple-modal[1]/div/div/div[2]/a[1]"))
# # )
# # cookies_accept_btn.click()
# # Recorrer todos los botones "Ver 12 más" y hacer clic en ellos
# counter = 0
# href_set = set()
# # Crea un DataFrame vacío fuera del bucle
# all_contacts_data = pd.DataFrame(columns=["link"])
#
# # Itera a través de todas las páginas
# for page in range(100):
#     time.sleep(15)
#     driver.get(f"https://www.linkedin.com/search/results/people/?geoUrn=%5B%22105646813%22%5D&keywords=consultoria&origin=FACETED_SEARCH&page={str(page)}&profileLanguage=%5B%22es%22%5D&sid=qz*&titleFreeText=CEO")
#
#
#     urls = driver.find_elements(By.XPATH,"//*[@id='/Ye9fNIiRK+mZHruuZPIow==']/div/ul//li//div//div//div//div//div//a[contains(@class, 'app-aware-link  scale-down')]")
#
#
#     for url in urls:
#         href = url.get_attribute("href")
#         print(href)  # Imprime el enlace
#         href_set.add(href)
#
#
#     # Crea una lista para almacenar los datos de las propiedades
#     contact_data = [{"link": href} for href in href_set]
#
#     # Añade las nuevas propiedades al DataFrame existente
#     all_contacts_data = all_contacts_data._append(contact_data, ignore_index=True)
#     print(all_contacts_data)  # Imprime el DataFrame
#
#
#     # Elimina las filas duplicadas
#     all_contacts_data = all_contacts_data.drop_duplicates(subset=["link"], keep="first")
#
#     # Vacía el conjunto href_set para la siguiente página
#     href_set.clear()
#
#     # Guarda el DataFrame en un archivo de Excel cada 20 propiedades
#     if (page + 1) % 20 == 0:
#         file_counter = (page + 1) // 20
#         all_contacts_data.to_excel(f"links{file_counter}.xlsx", index=False, engine="openpyxl")
#
# # Cierra el driver de Selenium
# driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# import selenium.webdriver.support.expected_conditions as ec  # noqa
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.common.keys import Keys
# import requests
# from urllib.parse import unquote
#
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument('--disable-extensions')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-infobars')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--disable-browser-side-navigation')
# options.add_argument('--disable-gpu')
#
# driver = webdriver.Chrome(options=options)
#
# driver.execute_script("window.open('https://www.linkedin.com/home', '_blank')")
# time.sleep(5)
# driver.switch_to.window(driver.window_handles[1])
#
# time.sleep(3)
# username_field = driver.find_element(By.XPATH, '//*[@id="session_key"]').send_keys("hectorcreatives08@gmail.com")
# time.sleep(3)
# password_field = driver.find_element(By.XPATH, '//*[@id="session_password"]').send_keys("20759364")
# time.sleep(3)
# btn = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')
# btn.click()
# time.sleep(5)
#
# driver.execute_script("window.open('https://www.linkedin.com/search/results/people/?geoUrn=%5B%22105646813%22%5D&keywords=consultoria&origin=FACETED_SEARCH&page=NaN&profileLanguage=%5B%22es%22%5D&sid=qz*&titleFreeText=CEO', '_blank')")
# time.sleep(5)
# driver.switch_to.window(driver.window_handles[2])
#
#
# //*[@id="AIwCO9XQROWEoesSW2giEg=="]/div/ul/li[1]/div/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a
# //*[@id="AIwCO9XQROWEoesSW2giEg=="]/div/ul/li[2]/div/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a
# //*[@id="AIwCO9XQROWEoesSW2giEg=="]/div/ul/li[3]/div/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a
#
# # Obtener todos los elementos que coinciden con el XPath
# urls = driver.find_elements(By.XPATH,"//*[@id='/Ye9fNIiRK+mZHruuZPIow==']/div/ul//li//div//div//div//div//div//a[contains(@class, 'app-aware-link scale-down')]")
#
# # Iterar sobre cada elemento y obtener el valor del atributo href
# for url in urls:
#   href = url.get_attribute("href")
#   print(href)
#
# # Cerrar el navegador
# driver.quit()



#
# import selenium.webdriver.support.expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.common.exceptions import NoSuchElementException
# import time
#
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument('--disable-extensions')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-infobars')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--disable-browser-side-navigation')
# options.add_argument('--disable-gpu')
#
# driver = webdriver.Chrome(options=options)
#
# # Define la URL base y el número total de páginas a scrappear
# base_url = "https://www.linkedin.com/search/results/people/?geoUrn=%5B%22105646813%22%5D&keywords=consultoria&origin=FACETED_SEARCH&profileLanguage=%5B%22es%22%5D&sid=mTd&titleFreeText=CEO"
# total_pages =  10  # Cambia esto al número total de páginas que deseas scrappear
#
# # Función para extraer las URLs de los perfiles
# def extract_profile_links():
#     profile_links = []
#     for index in range(1,  11):  # Asume que siempre hay  10 elementos por página
#         xpath = f"//*[@id='AIwCO9XQROWEoesSW2giEg==']/div/ul/li[{index}]/div/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a"
#         try:
#             element = driver.find_element(By.XPATH, xpath)
#             href = element.get_attribute("href")
#             profile_links.append(href)
#         except NoSuchElementException:
#             continue
#     return profile_links
#
# # Inicia sesión en LinkedIn
# driver.execute_script("window.open('https://www.linkedin.com/home', '_blank')")
# time.sleep(5)
# driver.switch_to.window(driver.window_handles[1])
#
# time.sleep(3)
# username_field = driver.find_element(By.XPATH, '//*[@id="session_key"]').send_keys("hectorcreatives08@gmail.com")
# time.sleep(3)
# password_field = driver.find_element(By.XPATH, '//*[@id="session_password"]').send_keys("20759364")
# time.sleep(3)
# btn = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')
# btn.click()
# time.sleep(5)
#
# # Navega a la primera página de resultados de búsqueda
# driver.execute_script(f"window.open('{base_url}&page=1', '_blank')")
# time.sleep(5)
# driver.switch_to.window(driver.window_handles[2])
#
# # Itera a través de todas las páginas y extrae las URLs
# for page in range(1, total_pages +  1):
#     # Extrae las URLs de la página actual
#     profile_links = extract_profile_links()
#     for link in profile_links:
#         print(link)
#
#     # Navega a la siguiente página
#     if page < total_pages:
#         next_page_xpath = "//*[@id='ember173']/button"
#
#         try:
#             next_button = WebDriverWait(driver,  10).until(EC.presence_of_element_located((By.XPATH, next_page_xpath)))
#             next_button.click()
#             time.sleep(5)  # Espera a que la página siguiente se cargue
#         except NoSuchElementException:
#             print("No se encontró el botón para la siguiente página.")
#             break
#
# # Cierra el navegador
# driver.quit()
#
#




# import selenium.webdriver.support.expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.common.exceptions import NoSuchElementException
# import time
# import pandas as pd
# from openpyxl import load_workbook
#
#
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument('--disable-extensions')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-infobars')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--disable-browser-side-navigation')
# options.add_argument('--disable-gpu')
#
# driver = webdriver.Chrome(options=options)
#
# # Define la URL base y el número total de páginas a scrappear
# base_url = "https://www.linkedin.com/search/results/people/?geoUrn=%5B%22105646813%22%5D&keywords=consultoria&origin=FACETED_SEARCH&profileLanguage=%5B%22es%22%5D&sid=mTd&titleFreeText=CEO"
# total_pages =  10  # Cambia esto al número total de páginas que deseas scrappear
#
# # Función para extraer las URLs de los perfiles
# def extract_profile_links():
#     profile_links = []
#     # Asume que siempre hay  10 elementos por página
#     xpath = "//span[@class='entity-result__title-line entity-result__title-line--2-lines ']/span/a"
#     try:
#         # Usa .find_elements para obtener una lista de todos los elementos que coinciden
#         elements = driver.find_elements(By.XPATH, xpath)
#         for element in elements:
#             # Para cada elemento, obtén el atributo href y agrégalo a la lista de enlaces
#             href = element.get_attribute("href")
#             profile_links.append(href)
#     except NoSuchElementException:
#         print("No se encontraron elementos.")
#         pass
#     return profile_links
#
#
#
# # Inicia sesión en LinkedIn
# driver.execute_script("window.open('https://www.linkedin.com/home', '_blank')")
# time.sleep(5)
# driver.switch_to.window(driver.window_handles[1])
#
# time.sleep(3)
# username_field = driver.find_element(By.XPATH, '//*[@id="session_key"]').send_keys("hectorcreatives08@gmail.com")
# time.sleep(3)
# password_field = driver.find_element(By.XPATH, '//*[@id="session_password"]').send_keys("20759364")
# time.sleep(3)
# btn = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')
# btn.click()
# time.sleep(5)
#
# # Navega a la primera página de resultados de búsqueda
# driver.get(base_url + "&page=1")
# time.sleep(5)  # Espera a que la página se cargue completamente
#
# # Nombre del archivo donde se guardarán las URLs
# output_file = "linkedin_links.xlsx"
#
# # Itera a través de todas las páginas y extrae las URLs
# for page in range(1, total_pages +   1):
#     # Extrae las URLs de la página actual
#     profile_links = extract_profile_links()
#
#
#     # Imprime las URLs en la consola
#     for link in profile_links:
#         print(link)
#
#     # Navega a la siguiente página cambiando el parámetro 'page' en la URL
#     if page < total_pages:
#         next_page = page +  1
#         driver.get(base_url + f"&page={next_page}")
#         time.sleep(20)  # Espera a que la página siguiente se cargue completamente
#
# # Cierra el navegador
# driver.quit()

