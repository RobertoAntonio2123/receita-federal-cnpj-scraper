import requests

# URL da página de download
url = "https://portaldatransparencia.gov.br/download-de-dados/favorecidos-pj"

# Fazendo a requisição para a página
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    print("Requisição bem-sucedida! Conteúdo da página:")
    print(response.text)  # Exibindo o conteúdo da página HTML
else:
    print(f"Falha na requisição. Código de status: {response.status_code}")