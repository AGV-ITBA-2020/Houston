import paho.mqtt.client as mqtt
import time

def onMsg(client, userdata, message):
    print(str(message.payload.decode("utf-8")))

if __name__ == '__main__':
    client = mqtt.Client("AGV1")  # create new instance
    client.connect("localhost")  # connect to broker
    client.on_message = onMsg
    client.subscribe("AGV1")
    #Emula un AGV
    client.publish("Houston", "AGV1\nOnline")  # publish
    time.sleep(5)
    client.publish("Houston", "AGV1\nHB")  # publish
    time.sleep(5)
    client.publish("Houston", "AGV1\nQuest\nYes")  # publish
    time.sleep(5)
    client.publish("Houston", "AGV1\nStatus\nDistance: 50 BatVolt: 1230")  # publish
    time.sleep(1)
    client.publish("Houston", "AGV1\nQuest step reached")  # publish
    time.sleep(1)
    client.publish("Houston", "AGV1\nStatus\nDistance: 50 BatVolt: 1230")  # publish
    time.sleep(1)
    client.publish("Houston", "AGV1\nStatus\nDistance: 100 BatVolt: 1230")  # publish
    time.sleep(1)
    client.publish("Houston", "AGV1\nQuest step reached ")  # publish
    time.sleep(5)
    client.publish("Houston", "AGV1\nStatus\nDistance: 50 BatVolt: 1230")  # publish
    time.sleep(1)
    client.publish("Houston", "AGV1\nQuest step reached")  # publish
    time.sleep(5)
