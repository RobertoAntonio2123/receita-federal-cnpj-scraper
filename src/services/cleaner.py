import pandas as pd

print('carregando os dados')

df = pd.read_csv(
"/home/roberto/Documentos/project/receita-federal-cnpj-scraper/tests/202501_CNPJ.csv",
encoding="latin1", # Teste 'latin1', 'ISO-8859-1' ou 'windows-1252'
sep=";", # Caso o separador seja diferente, ajuste para ',' ou '\t'
dtype=str, # Previne erros de tipos mistos
#sume_missing=True # Para evitar problemas com colunas vazias
)
df=df.drop(columns=['COMPLEMENTO', 'NOMEFANTASIA'])
df = df.dropna(subset=['LOGRADOURO', 'CEP'])
df.loc[:, 'NUMERO'] = df['NUMERO'].astype(str).str.extract('(\d+)') # Garante que está alterando df diretamente
df.loc[:, 'NUMERO'] = pd.to_numeric(df['NUMERO'], errors='coerce').astype('Int64') # Converte para número
df['NUMERO'] = df['NUMERO'].fillna(0)
df['BAIRRO'] = df['BAIRRO'].fillna('')
df = df.astype({
'CNPJ': 'Int64',
'RAZAOSOCIAL': 'string',
'COD_CNAE': 'Int64',
'COD_NATJURIDICA': 'Int64',
'TIPO_PESSOA': 'string',
'LOGRADOURO': 'string',
'NUMERO': 'Int64',
'CEP': 'Int64',
'BAIRRO': 'string',
'MUNICIPIO': 'string',
'UF': 'string'
})
print((df.isnull().sum() / len(df)) * 100)