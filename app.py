from flask import Flask, request, jsonify
import time
from datetime import datetime

app = Flask(__name__)

usuarios_autorizados = {
    '771439528262': {'nome': 'Guilherme', 'painel': 'admin'},
    '632092037175': {'nome': 'joão', 'painel': 'usuario'},
}

@app.route('/autenticar', methods=['POST'])
def autenticar():
    data = request.get_json()
    rfid_tag = str(data.get('rfid_tag'))
    print(rfid_tag)

    if rfid_tag in usuarios_autorizados:
        usuario = usuarios_autorizados[rfid_tag]
        
        now = datetime.now()
        log_entry = f"{now.strftime('%Y-%m-%d %H:%M:%S')} - Acesso autorizado para {usuario['nome']} - {usuario['painel']}\n"
        
        with open('acessos.txt', 'a') as log_file:
            log_file.write(log_entry)

        return jsonify({
            'status': 'sucesso',
            'mensagem': f"Acesso autorizado para {usuario['nome']}",
            'painel': usuario['painel']
        }), 200
    else:
        return jsonify({
            'status': 'erro',
            'mensagem': 'Acesso negado. Tag não reconhecida.'
        }), 403

if __name__ == '__main__':
    app.run(host='10.1.24.123', port=8080)
