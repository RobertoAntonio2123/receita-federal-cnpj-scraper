import pandas as pd
import os

def clean_data(extracted_folder, cleaned_folder):
    """Realiza a limpeza dos arquivos CSV na pasta extraída e salva na pasta de saída."""
    print(f"Limpando dados de {extracted_folder} para {cleaned_folder}...")
    os.makedirs(cleaned_folder, exist_ok=True)

    arquivos_para_remover = ["202501_CNAE.csv", "202501_NaturezaJuridica.csv"]
    for arquivo in arquivos_para_remover:
        caminho_arquivo = os.path.join(extracted_folder, arquivo)
        if os.path.exists(caminho_arquivo):
            os.remove(caminho_arquivo)
            print(f"Arquivo removido: {caminho_arquivo}")
    
    for arquivo in os.listdir(extracted_folder):
        if arquivo.endswith(".csv"):
            caminho_arquivo = os.path.join(extracted_folder, arquivo)
            caminho_saida = os.path.join(cleaned_folder, arquivo)
            print(f"Processando {caminho_arquivo}...")
            df = pd.read_csv(caminho_arquivo, encoding="latin1", sep=";", dtype=str)

            if "CNPJ" in df.columns:
                df = df[df["CNPJ"].str.len() == 14]

            df.to_csv(caminho_saida, index=False, sep=";", encoding="utf-8")
    
    print("Limpeza concluída!")