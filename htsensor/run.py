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
mqtt_broker = "MQTT_BROKER_ADDRESS"
mqtt_broker_port = "MQTT_PORT"
temp_topic = "cisco/t"
humidity_topic = "cisco/h"
light_topic = "cisco/light"
# sensor/led
led_pin = 14
sensor_pin = 4
# initialize GPIO, First we stop the warnings which is a feature in this Python GPIO library.
GPIO.setwarnings(False)
# We also set the GPIO mode to BCM which is kind of standret RaspberryPi GPIO mapping scheme.
GPIO.setmode(GPIO.BCM)
# Funally we do a cleanup() this means that we set all GPIO pins to its default state.
GPIO.cleanup()

# Setting GPIO pin no. 14 as an output.
GPIO.setup(led_pin, GPIO.OUT)
# then we set it's state to one which equivalent to "OFF"
GPIO.output(led_pin, 0)

client = mqtt.Client()
# deifining on_message function that controls the GPIO pin to turn ON/OFF the light and prints received messages.


def on_message(client, userdata, msg):
    if (msg.payload == "on"):
        GPIO.output(led_pin, 1)
    if (msg.payload == "off"):
        GPIO.output(led_pin, 0)
    print(msg.payload)


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
			client.publish(temp_topic, result.temperature, qos=0, retain=True)
			temperature = result.temperature
		if (result.humidity != humidity):
			client.publish(humidity_topic, result.humidity, qos=0, retain=True)
			humidity = result.humidity
		print("Temperature: {} C".format(result.temperature))
		print("Humidity: {} %".format( result.humidity))
	time.sleep(1)
