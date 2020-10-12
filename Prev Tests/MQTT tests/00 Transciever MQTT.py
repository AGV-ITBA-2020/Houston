import paho.mqtt.client as mqtt

def print_msg(client, userdata, message):
    print(str(message.payload.decode("utf-8")))

client = mqtt.Client("Houston") #create new instance

client.on_message=print_msg

client.connect("localhost") #connect to broker
client.subscribe("outTopic")
client.loop_start()

while(1):
    str2Send = input()
    client.publish("AGV1",str2Send)