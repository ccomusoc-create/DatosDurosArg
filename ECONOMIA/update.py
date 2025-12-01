import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import os

os.makedirs("data", exist_ok=True)

# Dólar oficial BNA
url = "https://www.bna.com.ar/Cotizador/Monedas"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

tds = soup.find_all("td", {"class": "valor"})
dolar_oficial = None

for i, td in enumerate(tds):
    if td.text.strip() == "Dólar U.S.A.":
        dolar_oficial = tds[i + 1].text.strip()
        break

if dolar_oficial is None:
    dolar_oficial = "No disponible"

data = {
    "fecha": datetime.now().isoformat(),
    "dolar_oficial": dolar_oficial
}

with open("data/dolar.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Datos guardados correctamente en data/dolar.json")
