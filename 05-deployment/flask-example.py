from flask import Flask

app = Flask('ping')

@app.route('/ping', methods = ['GET'])
def ping():
    return "PONG"

if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0', port = 9696)

# curl 0.0.0.0:9696/ping
# curl http://0.0.0.0:9696/ping
# curl http://localhost:9696/ping