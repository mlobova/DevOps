import time
import socket
from datetime import datetime
from flask import Flask
from flask import jsonify


app = Flask(__name__)

def data():
	now = datetime.now()
	date = str(now.date())
	time = str(now.time())
	ip = socket.gethostbyname(socket.gethostname())
	date_hash = hash(now.date())
	return date, time, ip, date_hash	

def motd():
	date, time, ip, date_hash = data()
	with open ("/etc/motd","w") as file:
		file.write(
f"""
Date: {date}\n
Time: {time}\n
IP: {ip}\n
HASH: {date_hash}
"""
		)


@app.route('/info')
def info():
	date, time, ip, date_hash = data()
	j = {
		"date": date,
		"time": time,
		"ip": ip,
		"hash": date_hash
	}
	return jsonify(j)

motd()
app.run(host='0.0.0.0', port=80)
