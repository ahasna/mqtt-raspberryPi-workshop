# This Python script was written by Stefan Braicu for the Cisco IoT Workshop.
# it is used to create an HTTP Server that will translate HTTP requests into MQTT messages.
# This functions as a REST API, what menas we can use custom dashboard, Mobile App, Amazon Alexa ... etc to control the light and read the sensor data.

from flask import Flask
import paho.mqtt.client as mqtt

mqtt_broker = "Enter your MQTT Broker address as a string here"
mqtt_broker_port = "Enter the port as a number here"

app = Flask(__name__)

@app.route('/light/on')
def light_on():
    client.publish("cisco/light", "on", qos=0, retain=False)
    return "Turned ON"
@app.route('/light/off')
def light_off():
    client.publish("cisco/light", "off", qos=0, retain=False)
    return "Turned OFF"
if __name__ == '__main__':
    client = mqtt.Client()
    client.connect(mqtt_broker, mqtt_broker_port, 60)
    client.loop_start()
    app.run(host='0.0.0.0')
