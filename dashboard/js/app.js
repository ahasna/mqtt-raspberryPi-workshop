var reconnectTimeout = 2000;
var app = angular.module('myApp', ['ngMaterial']);
app.controller("myController", function ($scope,$http) {

var g_t = new JustGage({
    id: "gauge_temperature",
    value: 0,
    min: 0,
    max: 50,
    title: "Temperature",
    label: "\xB0C"
  });

var g_h = new JustGage({
    id: "gauge_humidity",
    value: 0,
    min: 0,
    max: 100,
    title: "Humidity",
    label: "%RH"
  });

//MQTT
const mqtt_broker = "MQTT_BROKER_ADDRESS";
const temp_topic = "cisco/t" 
const humidity_topic = "cisco/h"
const light_topic = "cisco/light"

//### Snippet B1-1 here
// Create a client instance
client = new Paho.MQTT.Client(mqtt_broker, Number(80), "/ws", "bb_" + parseInt(Math.random() * 100, 10));
// set callback handlers
client.onConnectionLost = onConnectionLost;
client.onMessageArrived = onMessageArrived;
mqttConnect();
function mqttConnect() {
// connect the client
client.connect({onSuccess:onConnect,onFailure:onFailure});}

//### Snippet B1-2 here
// called when the client connects
function onConnect() {
  // Once a connection has been made, make a subscription and send a message.
  client.subscribe(temp_topic);
  client.subscribe(humidity_topic);
  client.subscribe(light_topic);
}


function onFailure() {
  setTimeout(mqttConnect, reconnectTimeout);
}


// called when the client loses its connection
function onConnectionLost(responseObject) {
  if (responseObject.errorCode !== 0) {
    console.log("onConnectionLost:"+responseObject.errorMessage);
  }
  setTimeout(mqttConnect, reconnectTimeout);
  connect();
}

// called when a message arrives
function onMessageArrived(message) {

    if (message.destinationName == temp_topic) {
	g_t.refresh(message.payloadString);
    } 
    if (message.destinationName == humidity_topic) {
	g_h.refresh(message.payloadString);
    } 

    if (message.destinationName == light_topic) {
	if (message.payloadString == "on") {
	    $scope.light = true;
	} else {
	    $scope.light = false;
	} 
	console.log(message.payloadString);
    }

  $scope.$apply();
}

//### Snippet B2 here
function onMessageArrived(message) {
    if (message.destinationName == temp_topic) {      g_t.refresh(message.payloadString);    }
    if (message.destinationName == humidity_topic) {     g_h.refresh(message.payloadString);   }
    if (message.destinationName == light_topic) {
        if (message.payloadString == "on") {             
	    $scope.light = true;
        } else {
            $scope.light = false;
        }   
	console.log(message.payloadString);     }   $scope.$apply();  
}

//### Snippet B3 here
$scope.switchLight = function() {
	if (!$scope.light) {
	    message = new Paho.MQTT.Message("on");
	} else {
	    message = new Paho.MQTT.Message("off");
	}
        message.destinationName = "cisco/light";

        client.send(message);
};

});
