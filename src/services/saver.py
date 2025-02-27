import shutil
import os

def save_clean_data(source_folder, destination_folder):
    """Move os arquivos limpos para a pasta final."""
    os.makedirs(destination_folder, exist_ok=True)

    for arquivo in os.listdir(source_folder):
        caminho_origem = os.path.join(source_folder, arquivo)
        caminho_destino = os.path.join(destination_folder, arquivo)
        shutil.move(caminho_origem, caminho_destino)
        print(f"Arquivo movido para {caminho_destino}")
