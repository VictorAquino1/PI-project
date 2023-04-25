import pyodbc
import matplotlib.pyplot as plt

cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:gp05-monitoramento.database.windows.net,1433;Database=gp05-monitoramento;Uid=gp-05;Pwd={#Gf51451488874};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
cursor = cnxn.cursor()
querry = "Select * from [dbo].[sensor];"
count = cursor.execute(querry)
valor = []

for x in count:
    l1.append(x.valor) 

plt.plot(l1)
plt.ylabel("Valores do sensor")