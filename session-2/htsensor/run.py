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
mqtt_broker = "mqtt.eclipse.org"
mqtt_broker_port = 1883
temp_topic = "redi-cisco-2019/t"
humidity_topic = "redi-cisco-2019/h"
light_topic = "redi-cisco-2019/light"
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


def on_message(client, userdata, msg):
    utf_msg = msg.payload.decode("utf-8")
    if (utf_msg == "on"):
        GPIO.output(led_pin, 1)
    if (utf_msg == "off"):
        GPIO.output(led_pin, 0)
    print("Light Switch: {} / from topic: {} at {}".format(utf_msg, light_topic,
                                                           time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())), end=' \r\n')


# creating the MQTT client and establishing MQTT connection with the broker.
# paho Python Client - documentation: http://www.eclipse.org/paho/clients/python/docs/
client.on_message = on_message
client.connect(mqtt_broker, mqtt_broker_port, 60)
client.subscribe(light_topic)
client.loop_start()

# Reading data from the sensor.
instance = dht11.DHT11(pin=sensor_pin)
temperature = 0
humidity = 0
while True:
    result = instance.read()
    if result.is_valid():
        if (result.temperature != temperature):
            client.publish(temp_topic, result.temperature, qos=0, retain=False)
            temperature = result.temperature
        if (result.humidity != humidity):
            client.publish(humidity_topic, result.humidity,
                           qos=0, retain=False)
            humidity = result.humidity
        print("Temperature: {} C sent to topic: {} \nHumidity: {} % sent to topic: {}\nat {}\n".format(
            result.temperature, temp_topic, result.humidity, humidity_topic, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())), end='\r\n')
    time.sleep(0.5)
