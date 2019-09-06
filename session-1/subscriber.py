import paho.mqtt.client as mqtt
import time
from modules import helpers as h

# VARS
mqtt_broker = "mqtt.eclipse.org"
mqtt_broker_port = 1883
topic = "redi-cisco-2019/light"


def on_message(client, userdata, msg):
    utf_msg = msg.payload.decode("utf-8")
    print("Message received: {} at: {} From Topic: {}".format(
        h.color_it(utf_msg, "yellow"),
        h.color_it(time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime()), "cyan"),
        h.color_it(topic, "purple")))


client = mqtt.Client()
client.on_message = on_message
client.connect(mqtt_broker, mqtt_broker_port, 60)
client.subscribe(topic)

print()
print("Connected to MQTT Broker: {}  on Port: {}".format(
    h.color_it(mqtt_broker, "yellow"),
    h.color_it(mqtt_broker_port, "green")))
print("Subscribed to Topic: ", h.color_it(topic, "cyan"))
print()

client.loop_forever()
