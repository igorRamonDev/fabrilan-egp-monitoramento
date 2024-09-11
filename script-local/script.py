import requests
import time

# URL do GitHub Pages (onde os dados são armazenados)
url = "https://igorramondev.github.io/fabrilan-egp-monitoramento/status.json"

def check_in():
    try:
        # Enviando uma requisição de presença
        response = requests.get(url)
        if response.status_code == 200:
            print("Status enviado com sucesso.")
        else:
            print("Erro ao enviar status.")
    except Exception as e:
        print(f"Erro na conexão: {e}")

# Verifica o status a cada 5 minutos
while True:
    check_in()
    time.sleep(300)  # Aguarda 5 minutos para verificar novamente
