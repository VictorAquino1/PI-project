import datetime
from sys import getsizeof
import matplotlib.pyplot as plt
import time
import random
import mysql.connector
import csv

# informações de conexão com o banco de dados
host = 'localhost'
user = 'root'
password = '1234'
database = 'algas'

# conectando ao banco de dados
cnx = mysql.connector.connect(host=host, user=user, password=password, database=database)
cursor = cnx.cursor()
# Range de inserção de dados
sizes = {range(0, 100, 10),
         range(1000, 6000, 1000),
         range(1000, 6000, 100),
         range(1000, 6000, 10)
        }
#Gerar numeros entre 0mm ate 100mm 
l1 = []
l2 = []
for x in sizes:
    print(x)
    for y in x:
        start = time.time()
        sensorValue = random.randint(0, 100)
        print(f"Valor do sensor = {sensorValue}")
        insert_query = f"INSERT INTO sensor (valor, data) VALUES ({sensorValue}, now())"
        cursor.execute(insert_query)
        cnx.commit()
        stop = time.time()
        delta = stop - start
        size = getsizeof(l1)
        l1.append(delta)
        l2.append(getsizeof(l1))
        insert_query = f"INSERT INTO machineData (time, space) VALUES ({delta}, {size})"
        cursor.execute(insert_query)
        cnx.commit()
        print(f"getSizeof(l1) = {getsizeof(l1)}")

    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle(f'Monitoramento do sensor de proximidade caso = {x}')
    ax1.set_title('Dados de tempo')
    ax1.set_xlabel('Quantidade')
    ax1.set_ylabel('Tempo (s)')
    ax2.set_title('Comportamento do tamanho do array')
    ax2.set_xlabel('Quantidade')
    ax2.set_ylabel('Tamanho do array')
    ax1.plot(l1, "o--")
    ax2.plot(l2, "x-")
    plt.show()
    del l1[0:]
    del l2[0:]

print(f"Valor dos sensores = {l1}")
print(f"tamanho final do array = {len(l1)}")

print("==== EXPORTANDO BASE 'machineData' PARA CSV ====")
mpg_hdr = ['id', 'time', 'space']
mpg_query = ('SELECT id, time, space FROM machineData')
cursor.execute(mpg_query)
with open('machineData_Base.csv', 'w', newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(mpg_hdr)
    for (id, time, space) in cursor:
        writer.writerow([id, time, space])

print("==== EXPORTANDO BASE 'sensor' PARA CSV ====")
mpg_hdr = ['id', 'valor', 'data']
mpg_query = ('SELECT id, valor, data FROM sensor')
cursor.execute(mpg_query)
with open('sensor_Base.csv', 'w', newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(mpg_hdr)
    for (id, valor, data) in cursor:
        writer.writerow([id, valor, data])



cursor.execute("SELECT valor FROM sensor")
myresult = cursor.fetchall()
fig, ax = plt.subplots()
ax.plot(myresult)
ax.set_xlabel("Quantidade")
ax.set_ylabel("Distancia (mm)")
plt.show()

cursor.close()

