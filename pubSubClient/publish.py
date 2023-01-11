import paho.mqtt.client as mqtt

# Callback function for when the client successfully connects to the broker
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Once connected, the client can publish messages to a topic
    client.publish("exampleTopic", "Hello World!")




def main():

    client = mqtt.Client()
    client.on_connect = on_connect

    client.connect("localhost", 1883, 60)

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    client.loop_start()

    client.publish("exampleTopic", "Hello World! (again)")


    client.loop_forever()


if __name__ == "__main__":
    main()
