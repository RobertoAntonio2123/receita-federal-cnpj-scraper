import pandas as pd
import os

def limpar_dados(caminho_arquivo, caminho_saida):
    print('Carregando os dados...')

    # Leitura do CSV
    df = pd.read_csv(caminho_arquivo, encoding="latin1", sep=";", dtype=str)

    # Remover colunas desnecessárias
    colunas_para_remover = ['COMPLEMENTO', 'NOMEFANTASIA']
    df = df.drop(columns=[col for col in colunas_para_remover if col in df.columns], errors='ignore')

    # Remover registros sem LOGRADOURO e CEP
    df = df.dropna(subset=['LOGRADOURO', 'CEP'])

    # Tratar a coluna NUMERO
    df['NUMERO'] = df['NUMERO'].astype(str).str.extract('(\d+)').fillna('0')
    df['NUMERO'] = pd.to_numeric(df['NUMERO'], errors='coerce').astype('Int64')

    # Preencher valores nulos
    colunas_texto = ['RAZAOSOCIAL', 'TIPO_PESSOA', 'LOGRADOURO', 'MUNICIPIO', 'UF', 'BAIRRO']
    df[colunas_texto] = df[colunas_texto].fillna('')

    # Conversão dos tipos
    tipos = {
        'CNPJ': 'Int64', 'RAZAOSOCIAL': 'string', 'COD_CNAE': 'Int64',
        'COD_NATJURIDICA': 'Int64', 'TIPO_PESSOA': 'string', 'LOGRADOURO': 'string',
        'NUMERO': 'Int64', 'CEP': 'Int64', 'BAIRRO': 'string', 'MUNICIPIO': 'string', 'UF': 'string'
    }
    for coluna, tipo in tipos.items():
        if coluna in df.columns:
            df[coluna] = df[coluna].astype(tipo, errors='ignore')

    # Exibir percentual de valores nulos
    print("Percentual de valores nulos por coluna:")
    print((df.isnull().sum() / len(df)) * 100)

    # Salvar os dados limpos
    os.makedirs(os.path.dirname(caminho_saida), exist_ok=True)
    df.to_csv(caminho_saida, index=False, sep=";", encoding="utf-8")
    print(f"Arquivo limpo salvo como: {caminho_saida}")
