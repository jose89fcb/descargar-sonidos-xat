import os
import requests

# URL de la API
api_url = "https://api.xatblog.net/audies"

# Directorio de salida para guardar los archivos
output_directory = "sonidos_xat"

# Asegúrate de que el directorio de salida exista
os.makedirs(output_directory, exist_ok=True)

# Realiza una solicitud GET a la API
response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()

    # Verifica si la clave "audies" existe en los datos
    if "audies" in data:
        for index, item in enumerate(data["audies"]):
            # Construye la URL del sonido
            sound_url = f"https://xat.com/content/sounds/audies/{item}.webm"

            # Descarga el sonido
            response = requests.get(sound_url)
            if response.status_code == 200:
                # Guarda el sonido en el directorio de salida
                filename = f"{index}.webm"
                with open(os.path.join(output_directory, filename), "wb") as file:
                    file.write(response.content)
                print(f"Descargado: {filename}")
            else:
                print(f"No se pudo descargar: {sound_url}")
    else:
        print("La clave 'audies' no está en los datos de la API.")
else:
    print(f"No se pudo obtener datos de la API. Código de estado: {response.status_code}")
