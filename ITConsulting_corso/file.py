import requests

# URL diretto al CSV ufficiale (NASA Open Data)
url = "https://data.nasa.gov/download/gh4g-9sfh/application%2Fzip"

# Scarica il file ZIP
response = requests.get(url)
with open("Meteorite_Landings.zip", "wb") as f:
    f.write(response.content)

print("ZIP scaricato!")

# Ora estrai il CSV dal file ZIP
import zipfile

with zipfile.ZipFile("Meteorite_Landings.zip", 'r') as zip_ref:
    zip_ref.extractall("meteorite_data")

print("CSV estratto nella cartella 'meteorite_data'")
