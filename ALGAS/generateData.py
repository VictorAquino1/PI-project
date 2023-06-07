import random
import pyodbc
from datetime import datetime

# Determina a quantidade de medições terão na viagem e a probabilidade de acontecer um evento
sizes = range(1,101,1)

# Criar conexão com o banco de dados

cnx_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:wordserver.database.windows.net,1433;Database=word-database;Uid=urubu100;Pwd=14052002Kb4_;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
cnx = pyodbc.connect(cnx_string)

# Criar cursor para executar as queries
cursor = cnx.cursor()

# Seleciona o id da última viagem feita e cria o id da próxima viagem
cursor.execute("SELECT MAX(id_viagem) AS maior_id_viagem FROM (SELECT DISTINCT id_viagem FROM sensoresIntegrados) AS S")
result = cursor.fetchall()
last_id_viagem = result[0][0]
if last_id_viagem is None:
	last_id_viagem = 0
id_viagem = last_id_viagem + 1

# Peso inicial da carga
weight = 30

# Coordenadas iniciais aleatórias
initial_latitude = random.uniform(-90, 90)
initial_longitude = random.uniform(-180, 180)

for n in sizes:
	#Simulação do sensor de temperatura
	temperature = random.randint(20, 30)

	#Simulação do sensor de umidade
	humidity = round(random.uniform(50, 80),2)

	#Simulação do sensor de vibração
	vibration = round(random.uniform(0, 200), 4)

	#Simulação do sensor de ruído
	noise = round(random.uniform(30, 90),4)

	#Simulação do sensor de proximidade
	proximity = random.randint(0, 100)

	#Simulação vibração alta
	if random.randint(0, 99) == 0:
		vibration = round(random.uniform(200, 220), 4)

	#Simulação de abertura de porta
	if proximity >= 90:
		noise = round(random.uniform(70, 90),4)

	#Simulação do evento de furto
	if random.randint(0, 99) == 0:
		weight = weight - 2
		proximity = random.randint(90, 100)
		noise = round(random.uniform(70, 90),4)

	#Simulação da localização em coordenadas
	latitude = initial_latitude + random.uniform(-0.01, 0.01)
	latitude = round(latitude, 4)
	longitude = initial_longitude + random.uniform(-0.01, 0.01)
	longitude = round(longitude, 4)

	capture_date = (datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

	# Executar query para inserir os valores medidos pelos sensores
	values = (id_viagem, temperature, humidity, vibration, noise, proximity, weight, latitude, longitude, capture_date)
	cursor.execute("INSERT INTO sensoresIntegrados (id_viagem, temperatura, umidade, vibracao, ruido, proximidade, peso, latitude, longitude, data_captura) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", values)

	print(f'Valor {n} - Id da Viagem {id_viagem} - Temperatura {temperature} - Umidade {humidity} - Vibração {vibration} - Ruído {noise} - Proximidade {proximity} - Peso {weight} - Latitude {latitude} - Longitude {longitude} - Data Captura {capture_date}')

# Salvar as mudanças no banco de dados
cnx.commit()

# Fechar cursor e conexão
cursor.close()
cnx.close()