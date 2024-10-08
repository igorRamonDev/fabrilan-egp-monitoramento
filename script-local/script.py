import json
import datetime
import os

# Caminho para o arquivo JSON
status_file = 'status.json'

# Nome do servidor atual (defina isso para cada servidor de forma única)
server_name = "Local"

def update_status():
    try:
        # Abre o arquivo status.json
        with open(status_file, 'r') as file:
            data = json.load(file)

        # Encontra o servidor correto e atualiza o tempo de check-in
        for server in data['servers']:
            if server['name'] == server_name:
                server['last_check_in'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
                server['status'] = "online"  # Defina como "online" se o check-in foi bem-sucedido
                break

        # Escreve as mudanças de volta no arquivo JSON
        with open(status_file, 'w') as file:
            json.dump(data, file, indent=4)

        print(f"Status do {server_name} atualizado com sucesso.")

    except Exception as e:
        print(f"Erro ao atualizar o status: {e}")

def git_commit_and_push():
    try:
        # Commit e push via Git
        os.system('git add status.json')
        os.system(f'git commit -m "Atualizando status do {server_name}"')
        os.system('git push origin main')
        print(f"Commit e push realizados para {server_name}.")
    except Exception as e:
        print(f"Erro ao realizar commit e push: {e}")

# Executa a função de atualização e commit
update_status()
git_commit_and_push()
