from message_handler import MessageHandler
import settings
import time

class PubSubUtil:
    @staticmethod
    def set_callbacks(client):
        client.on_connect = PubSubUtil.on_connect
        client.on_subscribe = PubSubUtil.on_subscribe
        client.on_publish = PubSubUtil.on_publish
        client.on_message = PubSubUtil.on_message
        client.on_disconnect = PubSubUtil.on_disconnect


    @staticmethod
    def on_subscribe(client, userdata, mid, granted_qos):
        client.subscribed = True
        print(f"Subscribed: {mid} {granted_qos}")


    @staticmethod
    def on_publish(client,userdata,result):  
        client.published = True


    @staticmethod
    def handle_message(message):
        MessageHandler.handle_message(message)


    @staticmethod
    def on_disconnect(client, userdata, rc):
        print("Disconnected")


    @staticmethod
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected... Returned code = ", rc)
        else:
            print("Bad connection Returned code = ", rc)


    @staticmethod
    def on_message(client, userdata, msg):
        decoded_msg = str(msg.payload.decode("utf-8", "strict"))
        PubSubUtil.handle_message(decoded_msg)


    @staticmethod
    def connect_client(client, host, port):
        try:
            client.connect(host=host, port=port, keepalive=60)
        except:
            print("Unable to connect")
            exit(1)


    @staticmethod
    def wait_for_connection(client):
        while not client.is_connected():
            time.sleep(1)


    @staticmethod
    def wait_for_subscription(client):
        while not client.subscribed:
            time.sleep(1)