import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
import sys
import io
from selenium import webdriver

url = 'https://www.google.com.br/'
path = 'C:\\Projetos\\Scripts de Teste\\scrape.jpg'

DRIVER = 'C:\\Projetos\\Scripts de Teste\\chromedriver_81.exe'
driver = webdriver.Chrome(DRIVER)
driver.get(url)
screenshot = driver.save_screenshot(path)
driver.quit()

extracttext = pytesseract.image_to_string(path)
print(extracttext)
