from sys import getsizeof
import time
import random
import pyodbc

# conectando ao banco de dados
conn_string = "Driver={ODBC Driver 17 for SQL Server};Server=tcp:wordserver.database.windows.net,1433;Database=word-database;Uid=urubu100;Pwd=14052002Kb4_;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
conn = pyodbc.connect(conn_string)
cursor = conn.cursor()
# Range de inserção de dados
sizes = {
         range(0, 100),
        }
# Gerar numeros entre 0mm ate 100mm do sensor BIM-EM12E-Y1X
l1 = []
l2 = []

for x in sizes:
    print(x)
    for y in x:
        start = time.time()
        sensorValue = random.randint(0, 100)
        print(f"Valor do sensor = {sensorValue}")
        insert_query = f"INSERT INTO SensorData (SensorName,SensorValue,CaptureDate) VALUES ('proximidade', {sensorValue}, GETDATE())"
        cursor.execute(insert_query)
        cursor.commit()
        stop = time.time()
        delta = stop - start
        size = getsizeof(l1)
        l1.append(delta)
        l2.append(getsizeof(l1))
        print(f"getSizeof(l1) = {getsizeof(l1)}")
    del l1[0:]
    del l2[0:]

print(f"Valor dos sensores = {l1}")
print(f"tamanho final do array = {len(l1)}")

cursor.close()