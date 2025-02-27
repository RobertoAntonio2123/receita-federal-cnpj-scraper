import requests
import os

def baixar_arquivo_zip(url, save_path):
    """Baixa um arquivo ZIP de uma URL e salva localmente."""
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        with open(save_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
        print(f"Download concluído: {save_path}")
    else:
        print(f"Erro ao baixar o arquivo. Código: {response.status_code}")
        return None
