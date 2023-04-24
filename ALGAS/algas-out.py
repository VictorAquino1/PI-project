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


# GRAPHIC CONFIG

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

    cursor.execute("SELECT valor FROM sensor")
myresult = cursor.fetchall()
fig, ax = plt.subplots()
ax.plot(myresult)
ax.set_xlabel("Quantidade")
ax.set_ylabel("Distancia (mm)")
plt.show()