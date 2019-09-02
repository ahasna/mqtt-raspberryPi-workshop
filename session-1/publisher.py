import paho.mqtt.client as mqtt
import socket
import time

hostname = socket.gethostname()

# VARS
mqtt_broker = "mqtt.eclipse.org"
mqtt_broker_port = 1883
topic = "redi-cisco-2019/t"


def on_publish(client, userdata, mid):
    print("Message successfully sent to broker at {}".format(
        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    )
    )


client = mqtt.Client()
client.on_publish = on_publish
client.connect(mqtt_broker, mqtt_broker_port, 60)
client.subscribe(topic)

while True:
    user_message = input("Type a message then hit Enter: ")
    client.publish(topic, user_message, qos=0, retain=False)
