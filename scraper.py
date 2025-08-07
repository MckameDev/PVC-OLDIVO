import requests
from bs4 import BeautifulSoup

def obtener_titulos_hn():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    titulos = []
    for a in soup.select(".titleline a"):
        titulo = a.get_text()
        enlace = a.get("href")
        titulos.append({"titulo": titulo, "url": enlace})
    return titulos

def nombres_frutas():
    url = "https://garcesfruit.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    frutas = []
    for div in soup.select('div[class$="mod"]'):
        clase = div.get("class", [""])[0]
        nombre = clase.replace(" mod", "")
        frutas.append(nombre)
    return frutas

def frutas_con_descripcion():
    url = "https://garcesfruit.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    frutas = []
    for div in soup.select('div[class$="mod"]'):
        clase = div.get("class", [""])[0]
        nombre = clase.replace(" mod", "")
        descripcion_tag = div.find("p")
        descripcion = descripcion_tag.get_text(strip=True) if descripcion_tag else ""
        frutas.append({"nombre": nombre, "descripcion": descripcion})
    return frutas