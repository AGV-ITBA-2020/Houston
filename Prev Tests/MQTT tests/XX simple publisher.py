import paho.mqtt.client as mqtt

client = mqtt.Client("AGV 1") #create new instance

client.connect("localhost") #connect to broker

client.publish("Houston","Step Reached")#publish