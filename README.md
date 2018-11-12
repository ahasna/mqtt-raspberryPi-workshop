# MQTT and RaspberryPi

## What is our workshop about

This workshop is about applying MQTT protocol to turn ON/OFF a light, and to get Temperature and Humidity data and view it on an online dashboard

## What is RaspberryPi

RaspberryPi is an open-source, low cost computer on a chip, in other words it is a cheap and small computer.
The affordable price, the small size and the powerful hardware make RaspberryPi a perfect core for lots of IoT Projects.
You can find more about RaspberryPi [here](https://www.raspberrypi.org/)

## What is MQTT

MQTT is a machine-to-machine (M2M)/"Internet of Things" connectivity protocol.
Further reading can be found [here](http://mqtt.org/)

## How we will do it

The idea is to use a Dashboard to control light and to monitor the data received form the Temperature/Humidity sensor.
What really happens behind the scenes when we move the button on the dashboard, is that a function will be triggered to send an MQTT message with a specific topic, on the other hand the python code that runs on the RaspberryPi is connected  to the same MQTT Broker and subscribed to the same topic, and we have already specified in out code that if we received an MQTT message with "ON" we turn on the light (we send a signal to the relay that is connected to the RaspberryPi) and vice versa.

In the same way, the python script on the RaspberryPi is sending Temperature/Humidity as MQTT messages and the dashboard s connected  to the same MQTT Broker and subscribed to the same topic, and after receiving the messages, a function is responsible about converting these messages to a user-friendly gauge.

## Further Reading and Resources

**MQTT** [mqtt.org](http://mqtt.org/)

**SSL for secure communication** [SSL](http://info.ssl.com/article.aspx?id=10241)

[**Eclipse Mosquitto**](https://mosquitto.org/)

**Eclipse Paho** [Paho library](https://www.eclipse.org/paho/)

**Cool IoT Blog** [IOT BYTES](https://iotbytes.wordpress.com/)

**Python for Beginners** [Learn Python](https://www.learnpython.org/)

## Setup

The setup has two parts:

* **On the RaspberryPi**

* **On your laptop**

### On RaspberryPi

* ssh into yor RaspberryPi either from CLI (on MacOS and Linux):

```bash
ssh pi@<IP_ADDRESS>
```

* or using [PUTTY](https://www.putty.org/) on Windows

* clone this repo to your `RaspberryPi` by running the following command

```bash
cd ~
git clone https://github.com/ahasna/mqtt-raspberryPi-workshop.git
```

* go to the repo you've just cloned

```bash
cd ~/mqtt-raspberryPi-workshop
```

* Run the following:

```bash
sudo apt-get update
pip install paho-mqtt
```

* edit code:

```bash
cd ~/mqtt-raspberryPi-workshop/htsensor
sudo nano run.py
```

* edit lines 15 - 19 adding values to the following variables:

`mqtt_broker`, `mqtt_broker_port`, `temp_topic`, `humidity_topic` and `light_topic`

**Note:** You'll have to change the topics to unique ones of your choice to avoid receiving messages from other publishers on the same broker

```python
# VARS
mqtt_broker = "iot.eclipse.org"
mqtt_broker_port = "1883"
temp_topic = "some_topic/sub_topic" # example: asem/home/temp
humidity_topic = "some_topic/another_sub_topic" # example: asem/home/humidity
light_topic = "some_topic/also_another_sub_topic" # example: asem/home/light
# sensor/led
led_pin = 14
sensor_pin = 4
```

* if necessary edit lines 21 and 22 (in case you chose to use different GPIO Pins to connect the Sensor and LED)

* Save changes: `Ctrl + X` then `Y` then finally `Enter`

### On your Laptop

* clone this repo to your `local machine (laptop)` by running the following command from your CLI

```bash
git clone https://github.com/ahasna/mqtt-raspberryPi-workshop.git
```

* or just download from Github as a ZIP file if you don't have `git` installed. From [here](https://github.com/ahasna/mqtt-raspberryPi-workshop)

* go to `mqtt-raspberryPi-workshop/dasboard/js` (the repo you've just downloaded or cloned)

* edit lines 24 - 27 in `app.js` to add the `MQTT_BROKER_ADDRESS` and make sure that the MQTT topics match those in `run.py` (in RaspberryPi)

```javascript
const mqtt_broker = "iot.eclipse.org";
const temp_topic = "some_topic/sub_topic"; // example: asem/home/temp
const humidity_topic = "some_topic/another_sub_topic"; // example: asem/home/humidity
const light_topic = "some_topic/also_another_sub_topic"; // example: asem/home/light
```

## connect Circuits

### Temp./Humidity sensor (DHT11)

follow the diagram below to connect the sensor to your RaspberryPi

![DHT11](img/sensor-connect.png)

### LED

follow the diagram below to connect the LED to your RaspberryPi

![LED](img/LED-raspi.png)

for more details see the GPIO layout for RaspberryPi3 below

![GPIO](img/GPIO.png)

## Running the Code

### RaspberryPi

* ssh into yor RaspberryPi either from CLI by using:

```bash
ssh pi@<IP_ADDRESS>
```

or using [PUTTY](https://www.putty.org/)

* go to the repo you've cloned

```bash
cd ~/mqtt-raspberryPi-workshop/htsensor
python run.py
```

* Run the following:

```bash
sudo apt-get update
pip install paho-mqtt
```

### Dashboard

* go to `mqtt-raspberryPi-workshop/dasboard/`
* open `index.html` in browser

### Expected results

if everything runs as expected you should see the following:

#### RaspberryPi CLI

![CLI](img/raspi-cli.gif)

#### Browser

![CLI](img/dasboard.gif)

## Is all of this too easy for you?

if what we have been doing so far is not challenging enough for you, try controlling the LED using the Temp./Humidity values and add an indication alert of that to the dashboard