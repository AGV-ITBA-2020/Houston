import paho.mqtt.client as mqtt

def print_msg(client, userdata, message):
    print(str(message.payload.decode("utf-8")))

# client = mqtt.Client("agvem") #create new instance
#
# client.on_message=print_msg
#
# client.connect("localhost") #connect to broker
# client.subscribe("AGV1")
# client.loop_start()
#
# i=0
# while(1):
#     data = input()
#     if (data=='QR'):
#         client.publish("Houston", "AGV1\nQuest step reached")
#
#     i=i+1

client = mqtt.Client("agvem") #create new instance

client.on_message=print_msg

client.connect("localhost") #connect to broker
client.subscribe("Houston")
client.loop_start()

i=0
while(1):
    data = input()
    if data == "Continue":
        client.publish("AGV1", data)
    elif data == "m1":
        client.publish("AGV1","Quest?\n"+"NoBs80Fl80Me80Fr80Me100StBeNo" )
    #client.publish("AGV1","Quest?\n"+"NoBs10Me20Fr10Me10Fl10Me20StBeNo" )
    i=i+1