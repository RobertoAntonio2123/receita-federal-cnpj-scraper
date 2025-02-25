import requests

def baixar_arquivo_zip(url):
    """Baixa o arquivo ZIP da URL e retorna o conteúdo."""
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        print("Download bem-sucedido!")
        return response.content
    else:
        print(f"Falha no download. Código de status: {response.status_code}")
        return None
