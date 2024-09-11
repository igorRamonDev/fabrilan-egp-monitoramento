import json
from datetime import datetime, timedelta

# Caminho para o arquivo status.json
status_file = 'status.json'

# Carrega o arquivo JSON existente
with open(status_file, 'r') as file:
    data = json.load(file)

# Define o tempo atual
current_time = datetime.utcnow()

# Atualiza o status de cada servidor
for server in data['servers']:
    last_check_in = datetime.strptime(server['last_check_in'], "%Y-%m-%dT%H:%M:%SZ")
    
    # Se o último check-in foi há mais de 5 minutos, considera o servidor offline
    if current_time - last_check_in > timedelta(minutes=5):
        server['status'] = 'offline'
    else:
        server['status'] = 'online'

# Salva as atualizações no arquivo JSON
with open(status_file, 'w') as file:
    json.dump(data, file, indent=4)

print("Status dos servidores atualizado.")
