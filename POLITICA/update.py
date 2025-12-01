import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import os

os.makedirs("data", exist_ok=True)

# Boletín Oficial (última publicación)
url = "https://www.boletinoficial.gob.ar/"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

# Tomamos el primer título publicado
titulos = soup.find_all("h3")
ultimo_titulo = titulos[0].text.strip() if titulos else "No disponible"

data = {
    "fecha": datetime.now().isoformat(),
    "ultimo_boletin": ultimo_titulo
}

with open("data/boletin.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Datos guardados correctamente en data/boletin.json")
