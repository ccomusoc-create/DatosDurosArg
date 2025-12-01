import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import os

os.makedirs("data", exist_ok=True)

# Agenda Cultura Nación
url = "https://www.cultura.gob.ar/agenda"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

eventos = soup.find_all("h2")
proximo_evento = eventos[0].text.strip() if eventos else "No disponible"

data = {
    "fecha": datetime.now().isoformat(),
    "proximo_evento": proximo_evento
}

with open("data/eventos.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Datos guardados correctamente en data/eventos.json")
