import zipfile
import os

def extract_zip_file(zip_path, extract_to):
    """Extrai um arquivo ZIP para um diretório específico."""
    if not os.path.exists(zip_path):
        print(f"Arquivo {zip_path} não encontrado.")
        return

    os.makedirs(extract_to, exist_ok=True)
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)
        print(f"Arquivo extraído para: {extract_to}")