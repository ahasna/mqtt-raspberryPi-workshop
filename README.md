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

## Setup

### On RaspberryPi

* ssh into yor RaspberryPi either from CLI by using:

```bash
ssh pi@<IP_ADDRESS>
```

or using [PUTTY](https://www.putty.org/)

* clone (or download) this repo to both your local machine by running the following command from your CLI

```bash
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

edit lines 15 and 16 adding `mqtt_broker` and `mqtt_broker_port`

```python
# VARS
mqtt_broker = "MQTT_BROKER_ADDRESS"
mqtt_broker_port = "MQTT_PORT"
# sensor/led
led_pin = 14
sensor_pin = 4
```

if necessary edit lines 18 and 19

### On your Laptop

* go to `mqtt-raspberryPi-workshop/dasboard/js`
* edit line 24 in `app.js` and add the MQTT Broker address.

```javascript
const mqtt_broker = "MQTT_BROKER_ADDRESS";
```

## connect Circuits

### Temp./Humidity sensor (DHT11)

follow the diagram below to connect the sensor to you RaspberryPi

![DHT11](img/sensor-connect.png)

### LED

follow the diagram below to connect the LED to you RaspberryPi

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

* clone (or download) this repo to both your local machine by running the following command from your CLI

```bash
git clone https://github.com/ahasna/mqtt-raspberryPi-workshop.git
```

* go to the repo you've just cloned

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