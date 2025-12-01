import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import os

# Crear carpeta "data" si no existe
os.makedirs("data", exist_ok=True)

# -------------------------------
# SMN – alertas meteorológicas
# -------------------------------
try:
    url_smn = "https://www.smn.gob.ar/avisos-meteorologicos"
    html_smn = requests.get(url_smn, timeout=10).text
    soup_smn = BeautifulSoup(html_smn, "html.parser")
    avisos = soup_smn.find_all("p")
    alerta_ambiental = avisos[0].text.strip() if avisos else "No disponible"
except Exception as e:
    alerta_ambiental = f"Error al obtener datos SMN: {e}"

# -------------------------------
# WAQI – calidad del aire (CABA)
# -------------------------------
try:
    token = "5e2fe4f61f113332333486e45c479305e2ea140b"
    url_aqi = f"https://api.waqi.info/feed/A229789/?token={token}"  # CABA
    resp = requests.get(url_aqi, timeout=10)
    aqi_data = resp.json()  # convertir a diccionario
    
    aqi_valor = aqi_data.get("data", {}).get("aqi", "No disponible")
    pm25 = aqi_data.get("data", {}).get("iaqi", {}).get("pm25", {}).get("v", "No disponible")
    pm10 = aqi_data.get("data", {}).get("iaqi", {}).get("pm10", {}).get("v", "No disponible")
except Exception as e:
    aqi_valor = pm25 = pm10 = f"Error al obtener datos AQI: {e}"

# -------------------------------
# Guardar en JSON
# -------------------------------
data = {
    "fecha": datetime.now().isoformat(),
    "alerta_ambiental": alerta_ambiental,
    "aqi": aqi_valor,
    "pm25": pm25,
    "pm10": pm10
}

with open("data/ambiente.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Datos guardados correctamente en data/ambiente.json")
