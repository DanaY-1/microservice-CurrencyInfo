# Currency Information Generator

# This microservice communicates with the Currency Converter application. 
# The Currency Converter app sets up the socket connection and the microservice connects to the socket.
# The Currency Converter app will send an encoded request to the microservice.
# The microservice will respond, and the Currency Converter will receive the message.

import time, socket, sys

print("Initializing....\n")
time.sleep(1)

s = socket.socket()
shost = 'localhost'                             # specify publishing host (Currency Converter)
host = 'localhost'                              # specify subscribing host  (Currency Info Generator)
name = "Currency Info"
port = 1234                                     # specify port
print("Trying to connect to ", host, "(", port, ")\n")
time.sleep(1)
s.connect((host, port))
print("Connected...\n")

s.send(name.encode())                           # send microservice name
s_name = s.recv(1024)                           # receive app name (Currency Converter)
s_name = s_name.decode()                        # store name of app for ease of identification
print("Type EXIT to quit")
print("Enter message to send...")

# Currency Data
currency_info = {
    "United States dollar": "Some info"    
}

# Continuous Communication Pipeline
while True:
    message = s.recv(1024)                      # receive message from app (Currency Converter)
    message = message.decode()
    print(s_name + ":", message)                # display message from app (Currency Converter)
    if message == "EXIT":                       # exit if the entered message is EXIT
        print("Exiting...")
        break
    elif message == "United States dollar":
        message = currency_info["United States dollar"]
        s.send(message.encode())
    else:
        message = input(str(name+": "))         # user enter message to send
        s.send(message.encode())
    