import paho.mqtt.client as mqtt

def print_msg(client, userdata, message):
    print(str(message.payload.decode("utf-8")))

client = mqtt.Client("asd") #create new instance

client.on_message=print_msg

client.connect("localhost") #connect to broker
client.subscribe("AGV1")
client.loop_start()
i=0;
while(1):
    i=i+1;