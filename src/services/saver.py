import os
import shutil

def mover_arquivo(origem, destino):
    """Move um arquivo para o diretório de destino."""
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    shutil.move(origem, destino)
    print(f"Arquivo movido para {destino}")
