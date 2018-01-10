import redis
import zmq

def fib(conn):
    pipe = conn.pipeline()
    while 1:
        try:
            pipe.watch("fib")
            X2 = pipe.lindex("fib", 1)
            X1 = pipe.lindex("fib", 0)
            Fib1 = int(X1)
            Fib2 = int(X2)
            curFib = Fib1 + Fib2
            pipe.multi()
            pipe.lset("fib", 0, curFib)
            pipe.lset("fib", 1, Fib1)
            pipe.execute()
            break
        except redis.WatchError:
            continue
        finally:
            pipe.reset()
    return
            
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
conn = redis.Redis('redis')
while True:
    mes = socket.recv()
    fib(conn)
    socket.send('done')
