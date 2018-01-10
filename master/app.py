from flask import Flask
import redis 
import zmq
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    X = conn.lindex("fib", 0)
    fib1 = int(X)
    FElement = "Current F element  = " + str(X)
    return FElement

@app.route('/', methods = ['POST'])
def increment():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://worker:5555")
    socket.send('next')
    answer = socket.recv()
    return "incremented"

if __name__ == "__main__":
    conn = redis.Redis('redis')
    while 1:
        try:
            conn.ping()
            break
        except redis.ConnectionError:
            continue
    if(int(conn.llen("fib")) == 0):
        conn.rpush("fib", 2 ,1)
    app.run(host="0.0.0.0", debug=True)
