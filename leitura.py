import RPi.GPIO as GPIO
import time
import requests
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    print("Aproxime o cartão RFID...")
    rfid_tag, _ = reader.read()
    rfid_tag_value = str(rfid_tag).strip()
    print(f"Tag lida: {rfid_tag_value}")

    try:
        response = requests.post('http://10.1.24.123:8080/autenticar', json={'rfid_tag': rfid_tag_value})
        response.raise_for_status()
        
        data = response.json()
        print(data['mensagem'])
        
        if data['painel'] == 'admin':
            print("Redirecionando para o painel de administrador...")
        else:
            print("Redirecionando para o painel de usuário...")
    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com a API: {e}")

    

