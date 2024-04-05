import pandas as pd

# Carregar o arquivo Excel
df = pd.read_excel('C:\\projetos python\\ETL excel para txt\\extracao.xlsx')

# Escolher as colunas que deseja extrair (substitua 'Nome da Coluna 1', 'Nome da Coluna 2', etc. pelos nomes das colunas desejadas)
colunas_desejadas = ['Coluna 1', 'Coluna 2']

# Escrever os dados das colunas escolhidas em um arquivo de texto
with open('C:\\projetos python\\ETL excel para txt\\dados.txt', 'w') as file:
    # Iterar sobre as linhas do DataFrame
    for index, row in df.iterrows():
        # Extrair os valores das colunas desejadas
        valores = [str(row[coluna]) for coluna in colunas_desejadas]
        # Escrever os valores no arquivo separados por vírgula (ou outro delimitador de sua escolha)
        linha = ' - '.join(valores)
        # Escrever a linha no arquivo
        file.write(f"{linha}\n")
