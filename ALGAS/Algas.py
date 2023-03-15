from sys import getsizeof
import matplotlib.pyplot as plt
import time
import random
import mysql.connector


# informações de conexão com o banco de dados
host = 'localhost'
user = 'root'
password = '1234'
database = 'algas'

# conectando ao banco de dados
cnx = mysql.connector.connect(host=host, user=user, password=password, database=database)
cursor = cnx.cursor()

sizes = {range(0, 100, 10),
         range(1000, 6000, 1000),
         range(1000, 6000, 100)
         }

"""
sizes = {range(1000, 6000, 1000)}
"""

#Gerar numeros entre 0mm ate 100mm 
l1 = []
for x in sizes:
    print(x)
    for y in x:
        start = time.time()
        sensorValue = random.randint(0, 100)
        print(f"Valor do sensor = {sensorValue}")
        insert_query = f"INSERT INTO sensor (valor) VALUES ({sensorValue})"
        cursor.execute(insert_query)
        cnx.commit()
        print(getsizeof(sensorValue))
        stop = time.time()
        l1.append(stop - start)
        plt.plot(l1, 'y')
        print(f"memory view var l1 = {getsizeof(l1)}")

print(f"Valor dos sensores = {l1}")
print(f"tamanho final do array = {len(l1)}")
#MUDAR AS CORES DE ACORDO COM A RANGE QUE MUDA
#EXPORTAR CSV DOS DADOS
plt.xlabel('Tamanho do array')
plt.ylabel('Time (S)')
plt.show()