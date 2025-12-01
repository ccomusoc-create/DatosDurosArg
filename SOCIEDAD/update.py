import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import os

os.makedirs("data", exist_ok=True)

# SMN – alerta clima
url = "https://www.smn.gob.ar/avisos-meteorologicos"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

avisos = soup.find_all("p")
primer_aviso = avisos[0].text.strip() if avisos else "No disponible"

data = {
    "fecha": datetime.now().isoformat(),
    "alerta_clima": primer_aviso
}

with open("data/alerta_clima.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Datos guardados correctamente en data/alerta_clima.json")
