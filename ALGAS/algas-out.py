import pyodbc
import matplotlib.pyplot as plt

cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:gp05-monitoramento.database.windows.net,1433;Database=gp05-monitoramento;Uid=gp-05;Pwd={#Gf51451488874};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
cursor = cnxn.cursor()
querry = "SELECT TOP (1000) * FROM [dbo].[machineData] where locationAz = 3;"
count = cursor.execute(querry)
# Machine data
time = []
space = []
for x in count:
    space.append(x.space) 
    print(x.space)

for x in count:
    time.append(x.time) 
    print(x.time)

# Machine data
querry = "SELECT TOP (1000) * FROM [dbo].[sensor] where locationAz = 3;"
count = cursor.execute(querry)

valor = []
id = []
for x in count:
    valor.append(x.valor) 

for x in count:
    id.append(x.id) 

fig, axs = plt.subplots(2)
fig.suptitle('sensor BIM-EM12E-Y1X - AWS(east-1e)')
axs[0].plot(space)
axs[0].set_title("Grafico do tempo x espaco")
axs[1].plot(valor)
axs[1].set_title("Simulação dos dados do sensor")
plt.show()

