import zipfile
import io
import os

def extrair_arquivo_zip(conteudo_zip, pasta_destino):
    """Extrai o arquivo ZIP na pasta especificada."""
    os.makedirs(pasta_destino, exist_ok=True)
    with zipfile.ZipFile(io.BytesIO(conteudo_zip), "r") as zip_ref:
        zip_ref.extractall(pasta_destino)
    print(f"Arquivos extraídos para a pasta: {pasta_destino}")
