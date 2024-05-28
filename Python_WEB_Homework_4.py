import os
import json
from flask import Flask, request, render_template, send_from_directory
from datetime import datetime
import socket
import threading

app = Flask(__name__)

if not os.path.exists('storage'):
    os.makedirs('storage')

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        username = request.form['username']
        message = request.form['message']
        send_to_socket_server(username, message)
        return render_template('message.html', success=True)
    return render_template('message.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

def send_to_socket_server(username, message):
    data = json.dumps({"username": username, "message": message})
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(data.encode(), ('localhost', 5000))
    sock.close()

def socket_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('localhost', 5000))

    while True:
        data, _ = sock.recvfrom(1024)
        message_data = json.loads(data.decode())
        timestamp = datetime.now().isoformat()
        with open('storage/data.json', 'a') as f:
            f.write(json.dumps({timestamp: message_data}, indent=4))
            f.write("\n")

if __name__ == '__main__':
    threading.Thread(target=socket_server, daemon=True).start()
    app.run(port=3000)
