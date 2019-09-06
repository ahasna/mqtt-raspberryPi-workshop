from modules import helpers as h
import paho.mqtt.client as mqtt
import socket
import time
hostname = socket.gethostname()
# VARS
mqtt_broker = "mqtt.eclipse.org"
mqtt_broker_port = 1883
topic = "redi-cisco-2019/light"


def on_publish(client, userdata, mid):
    publish_time = h.color_it(time.strftime(
        "%Y-%m-%d %H:%M:%S", time.localtime()), "cyan")
    print("Message successfully published to broker at {}".format(publish_time))


client = mqtt.Client()
client.on_publish = on_publish
client.connect(mqtt_broker, mqtt_broker_port, 60)
client.subscribe(topic)

print()
print("Connected to MQTT Broker: {}  on Port: {}".format(
    h.color_it(mqtt_broker, "yellow"),
    h.color_it(mqtt_broker_port, "green")))
print("Publishing to Topic: ", h.color_it(topic, "cyan"))
print()

while True:
    message = input("Type a message then hit Enter: ")
    user_message = "{}{}{}".format(
        message, h.color_it(" / pubisher Hostname: ", "white"), h.color_it(hostname, "red"))
    client.publish(topic, user_message, qos=0, retain=False)
