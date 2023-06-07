import pyodbc
import csv
import requests

query = "SELECT * FROM SensorData WHERE SensorName = 'proximidade' "

csv_filename = 'resultado-victor.csv'

# Colocar sua connection string 
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:wordserver.database.windows.net,1433;Database=word-database;Uid=urubu100;Pwd=14052002Kb4_;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')

# Executa a consulta SQL
cursor = conn.cursor()
cursor.execute(query)

# Recupera os resultados da consulta
results = cursor.fetchall()

# Obtém os nomes das colunas
column_names = [column[0] for column in cursor.description]

# Exporta os resultados para um arquivo CSV
with open(csv_filename, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    
    # Escreve os nomes das colunas no arquivo CSV
    writer.writerow(column_names)
    
    # Escreve cada linha de resultado no arquivo CSV
    writer.writerows(results)

print(f"Os resultados foram exportados para o arquivo {csv_filename}.")

# Fecha a conexão com o banco de dados
conn.close()


import requests

url = 'https://evbt1pfmeh.execute-api.us-east-1.amazonaws.com/dev/grupo05-sparkb/resultado-victor.csv'  # URL do endpoint para onde o arquivo será enviado
arquivo = r'C:\Users\victo\Documents\Reps\PI-project\Data integration\resultado-victor.csv'  # Caminho do arquivo que será enviado

# Configurar os cabeçalhos da requisição (opcional)
headers = {'Content-Type': 'application/octet-stream'}

# Ler o conteúdo do arquivo
with open(arquivo, 'rb') as f:
    conteudo = f.read()

# Enviar a requisição PUT com o conteúdo do arquivo
response = requests.put(url, data=conteudo, headers=headers)

# Verificar a resposta do servidor
if response.status_code == 200:
    print('Arquivo enviado com sucesso!')
else:
    print('Erro ao enviar o arquivo:', response.status_code)