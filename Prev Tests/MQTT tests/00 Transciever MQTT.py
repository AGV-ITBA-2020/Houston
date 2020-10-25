import paho.mqtt.client as mqtt

def print_msg(client, userdata, message):
    print(str(message.payload.decode("utf-8")))

client = mqtt.Client("Houston") #create new instance

client.on_message=print_msg

client.connect("localhost") #connect to broker
client.subscribe("Houston")
client.loop_start()

i=0
while(1):
    data = input()
    if (data[0]=='K'):
        client.publish("AGV1", "Set K PID\n" + data[1:])
    else:
        client.publish("AGV1","Fixed speed\n"+data)

    i=i+1