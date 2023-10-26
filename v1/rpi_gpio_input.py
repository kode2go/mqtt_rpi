import time
import paho.mqtt.client as paho
from paho import mqtt
import logging

import RPi.GPIO as GPIO  # Import the GPIO library for Raspberry Pi

logging.basicConfig(filename='mqtt_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# GPIO pin for control
GPIO_PIN = 14

# Initialize the GPIO settings
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.OUT)

gpio_state = GPIO.LOW

# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

    payload = msg.payload.decode().strip()

    global gpio_state

    if msg.payload == b'high' and gpio_state == GPIO.LOW:
        print("Turning GPIO 14 HIGH")
        logging.info(f"Received message on topic: {msg.topic}, QoS: {str(msg.qos)}, Payload: {payload}")
        logging.info("Turning GPIO 14 HIGH")
        GPIO.output(GPIO_PIN, GPIO.HIGH)
        gpio_state = GPIO.HIGH
        time.sleep(0.5)
        print("Turning GPIO 14 LOW")
        logging.info("Turning GPIO 14 HIGH")
        GPIO.output(GPIO_PIN, GPIO.LOW)
        gpio_state = GPIO.LOW
    else:
        print("Turning GPIO 14 LOW")
        logging.info(f"Received message on topic: {msg.topic}, QoS: {str(msg.qos)}, Payload: {payload}")
        logging.info("Turning GPIO 14 HIGH")
        GPIO.output(GPIO_PIN, GPIO.LOW)

# using MQTT version 5 here, for 3.1.1: MQTTv311, 3.1: MQTTv31
# userdata is user defined data of any type, updated by user_data_set()
# client_id is the given name of the client
client = paho.Client(client_id="x2", userdata=None, protocol=paho.MQTTv5)
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

# a single publish, this can also be done in loops, etc.
client.publish("encyclopedia/temperature", payload="cold", qos=1)

# loop_forever for simplicity, here you need to stop the loop manually
# you can also use loop_start and loop_stop
client.loop_forever()
