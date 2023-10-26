import time
import paho.mqtt.client as paho
from paho import mqtt

# setting callbacks for different events to see if it works, print the message, etc.
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

# with this callback, you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

# using MQTT version 5 here, for 3.1.1: MQTTv311, 3.1: MQTTv31
# userdata is user-defined data of any type, updated by user_data_set()
# client_id is the given name of the client
client = paho.Client(client_id="x1", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

# enable TLS for secure connection
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# set username and password
client.username_pw_set("user2", "Pajoloh100$")
# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect("73afeb948691459a98d7dab0fe284e89.s1.eu.hivemq.cloud", 8883)

# setting callbacks, use separate functions like above for better visibility
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish

# subscribe to all topics of encyclopedia by using the wildcard "#"
client.subscribe("encyclopedia/#", qos=1)

while True:
    # Get the Python input (0 or 1)
    python_input = input("Enter 0 for 'low' or 1 for 'high' (or 'q' to quit): ")

    if python_input.lower() == 'q':
        break  # Exit the loop if 'q' is entered.

    try:
        python_input = int(python_input)
        if python_input == 0:
            client.publish("encyclopedia/temperature", payload="low", qos=1)
        elif python_input == 1:
            client.publish("encyclopedia/temperature", payload="high", qos=1)
        else:
            print("Invalid input. Please enter 0 or 1.")
    except ValueError:
        print("Invalid input. Please enter 0 or 1.")
        

# Disconnect the MQTT client
client.disconnect()
