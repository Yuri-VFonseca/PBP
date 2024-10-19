from datetime import datetime
data = datetime.now()
data_atual = '{}/{}/{}'.format(data.day, data.month, data.year)
print(f"Data: {data_atual}")
hora = '{}:{}'.format(data.hour, data.minute)
print(f"Hora: {hora}")