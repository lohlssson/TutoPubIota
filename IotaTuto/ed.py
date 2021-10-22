import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('tcp://zmq.devnet.iota.org:5556')
socket.subscribe('sn')
print ("Socket connected")

while True:
    print ("Waiting for events from the node")
    message = socket.recv()
    data = message.split()
    print ("Transaction confirmed by milestone index: ", data[1])
    print ("Transaction hash: ", data[2])