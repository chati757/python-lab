
#python3 -m pip install paho-mqtt
import paho.mqtt.client as mqtt
import os
import urllib.parse as urlparse

# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print("on_connect:rc: " + str(rc))

def on_message(client, obj, msg):
    print("on_message" + msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_publish(client, obj, mid):
    print("on_publish:massageid[mid]: " + str(mid))

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, obj, level, string):
    print(string)

mqttc = mqtt.Client()
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

# Uncomment to enable debug messages
#mqttc.on_log = on_log

# Parse CLOUDMQTT_URL (or fallback to localhost)
#mqtt://USER:PASSWORD@host:port
topic = "testtopic"

# Connect
mqttc.username_pw_set("wuolgjlj","7NEws8XoqYnL")
mqttc.connect("m13.cloudmqtt.com",14081,60)

# Start subscribe, with QoS level 0
mqttc.subscribe(topic, 0)

# Publish a message
mqttc.publish(topic, "my message")

# Continue the network loop, exit when an error occurs
rc = 0
while rc == 0:
    rc = mqttc.loop()
print("rc: " + str(rc))