import os
import requests
from alive_progress import alive_bar

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
        total_files = len(data["audies"])
        with alive_bar(total_files, title="Descargando archivos") as bar:
            for item in data["audies"]:
                # Construye la URL del sonido
                sound_url = f"https://xat.com/content/sounds/audies/{item}.webm"

                # Obtiene el nombre original del archivo
                file_name = os.path.basename(sound_url)

                # Comprueba si el archivo ya existe en el directorio de salida
                if not os.path.exists(os.path.join(output_directory, file_name)):
                    # Descarga el sonido
                    response = requests.get(sound_url)
                    if response.status_code == 200:
                        with open(os.path.join(output_directory, file_name), 'wb') as file:
                            file.write(response.content)
                    else:
                        print(f"No se pudo descargar: {sound_url}")
                else:
                    print(f"El archivo ya existe: {file_name}")
                bar()  # Actualiza el progressbar
    else:
        print("La clave 'audies' no está en los datos de la API.")
else:
    print(f"No se pudo obtener datos de la API. Código de estado: {response.status_code}")
