import paho.mqtt.client as mqtt
import socket
import time

hostname = socket.gethostname()

# VARS
mqtt_broker = "mqtt.eclipse.org"
mqtt_broker_port = 1883
topic = "redi-cisco-2019/t"


def on_message(client, userdata, msg):
    utf_msg = msg.payload.decode("utf-8")
    print("Message received: {} at {}".format(
        utf_msg, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()
                               )))


client = mqtt.Client()
client.on_message = on_message
client.connect(mqtt_broker, mqtt_broker_port, 60)
client.subscribe(topic)

while True:
    client.loop_start()
    time.sleep(1)
