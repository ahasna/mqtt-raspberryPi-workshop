# This Python script was written by Stefan Braicu for the Cisco IoT Workshop.
# This code gets data from Temperature/Humidity Sensor then sends it to a Online-Dashboard, as well as controlling a relay using RaspberryPi.

# Importing:
# Python library to control GPIO pins onRaspberryPi.
import RPi.GPIO as GPIO
# Python Library to communicate with "add the sensor model"
import dht11
# Import time
import time
# Import Paho library (Python library to communicate with the MQTT Broker)
import paho.mqtt.client as mqtt

# VARS
mqtt_broker = "broker.mqttdashboard.com"
mqtt_broker_port = 1883
temp_topic = "redi-iot-2021/t"
humidity_topic = "redi-iot-2021/h"
light_topic = "redi-iot-2021/light"
# sensor/led
led_pin = 14
sensor_pin = 4
# initialize GPIO, First we stop the warnings which is a feature in this Python GPIO library.
GPIO.setwarnings(False)
# We also set the GPIO mode to BCM which is kind of standret RaspberryPi GPIO mapping scheme.
GPIO.setmode(GPIO.BCM)
# Finally we do a cleanup() this means that we set all GPIO pins to its default state.
GPIO.cleanup()

# Setting GPIO pin no. 14 as an output.
GPIO.setup(led_pin, GPIO.OUT)
# then we set it's state to one which equivalent to "OFF"
GPIO.output(led_pin, 0)

client = mqtt.Client()
# deifining on_message function that controls the GPIO pin to turn ON/OFF the light and prints received messages.

client.publish(light_topic, 'off', qos=0, retain=False)


def color_it(text, color):
    red = "\033[1;31;40m"
    green = "\033[1;32;40m"
    yellow = "\033[1;33;40m"
    cyan = "\033[1;36;40m"
    purple = "\033[1;35;40m"
    normal = "\033[0;37;40m"

    if color == "red":
        return "{}{}{}".format(red, text, normal)
    elif color == "green":
        return "{}{}{}".format(green, text, normal)
    elif color == "yellow":
        return "{}{}{}".format(yellow, text, normal)
    elif color == "cyan":
        return "{}{}{}".format(cyan, text, normal)
    elif color == "purple":
        return "{}{}{}".format(purple, text, normal)
    else:
        return text


def on_message(client, userdata, msg):
    tabs = "\t" * 4
    utf_msg = msg.payload.decode("utf-8")
    if (utf_msg == "on"):
        GPIO.output(led_pin, 1)
    if (utf_msg == "off"):
        GPIO.output(led_pin, 0)
    print("{} Light Switch: {}".format(
        tabs, color_it(utf_msg, "purple")), end='  \r')


# creating the MQTT client and establishing MQTT connection with the broker.
# paho Python Client - documentation: http://www.eclipse.org/paho/clients/python/docs/
client.on_message = on_message
client.connect(mqtt_broker, mqtt_broker_port, 60)
client.subscribe(light_topic)
client.loop_start()

# Reading data from the sensor.
instance = dht11.DHT11(pin=sensor_pin)
client.publish(humidity_topic, 0, qos=0, retain=False)
client.publish(temp_topic, 0, qos=0, retain=False)
# info
print()
print("Connected to MQTT Broker: {}  on Port: {}".format(
    color_it(mqtt_broker, "yellow"), color_it(mqtt_broker_port, "green")))
print()
print("Light Topic: ", color_it(light_topic, "cyan"))
print("Temp. Topic: ", color_it(temp_topic, "cyan"))
print("Humidity Topic: ", color_it(humidity_topic, "cyan"))
print()

while True:
    result = instance.read()
    if result.is_valid():
        if (result.temperature):
            client.publish(temp_topic, result.temperature,
                           qos=0, retain=False)
            temperature = result.temperature
        if (result.humidity):
            client.publish(humidity_topic, result.humidity,
                           qos=0, retain=False)
            humidity = result.humidity

        # colored CLI output
        info = "Temperature: {} Humidity: {}".format(color_it(str(
            result.temperature) + " C", "red"), color_it(str(result.humidity) + " %", "red"))

        print(info, end='\r')

    time.sleep(1)
