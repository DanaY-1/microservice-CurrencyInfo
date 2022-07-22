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
    "United States dollar": """The United States dollar (symbol: $; code: USD; also abbreviated US$ or U.S. Dollar, 
    to distinguish it from other dollar-denominated currencies; referred to as the dollar, U.S. dollar, American dollar, 
    or colloquially buck) is the official currency of the United States and several other countries.
    """,
    "European Euro": """The euro (symbol: €; code: EUR) is the official currency of 19 out of the 27 member states 
    of the European Union. This group of states is known as the eurozone or, officially, the euro area, and 
    includes about 349 million citizens as of 2019. The euro is divided into 100 cents. 
    """,
    "New Zealand dollar": """The New Zealand dollar (Māori: tāra o Aotearoa; sign: $, NZ$; code: NZD) is the official 
    currency and legal tender of New Zealand, the Cook Islands, Niue, the Ross Dependency, Tokelau, and a British territory, 
    the Pitcairn Islands. Within New Zealand, it is almost always abbreviated with the dollar sign ($), with "NZ$" sometimes 
    used to distinguish it from other dollar-denominated currencies.
    """,
    "Mexican peso": """The Mexican peso (symbol: $; code: MXN) is the currency of Mexico. Modern peso and dollar 
    currencies have a common origin in the 16th–19th century Spanish dollar, most continuing to use its sign, "$".
    """,
    "Canadian dollar": """The Canadian dollar (symbol: $; code: CAD; French: dollar canadien) is the currency of Canada. 
    It is abbreviated with the dollar sign $, or sometimes CA$, Can$ or C$ to distinguish it from other dollar-denominated 
    currencies. It is divided into 100 cents (¢). 
    """,
    "Peruvian sol": """The sol (Spanish pronunciation: [ˈsol]; plural: soles; currency sign: S/) is the currency of Peru; 
    it is subdivided into 100 céntimos ("cents"). The ISO 4217 currency code is PEN. 
    """
}

# Continuous Communication Pipeline
while True:
    message = s.recv(1024)                      # receive message from app (Currency Converter)
    message = message.decode()
    print(s_name + ":", message)                # display message from app (Currency Converter)
    if message == "EXIT":                       # exit if the entered message is EXIT
        print("Exiting...")
        break
    if message not in currency_info.keys():     # respond if no currency info is available
        message = "No information available"
        s.send(message.encode())
    for k in currency_info.keys():              # respond with appropriate currency
        if message == k:
            message = currency_info[k]
            s.send(message.encode())
            print(name + ":", message)           
    