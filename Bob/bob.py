import sys
import rsa
import json
import time
import settings
from pubsub_util import PubSubUtil
import paho.mqtt.client as mqtt

def get_public_key_to_encrypt():
    with open('../PublicKeys/public_keys.json', 'r') as file:
        data = json.load(file)
        e = int(data["pub_key_alice"]["e"])
        n = int(data["pub_key_alice"]["n"])
    
    return (e, n)


def encrypt_and_send_message(client, msg):
    e, n = get_public_key_to_encrypt()
    encrypted_msg = rsa.encrypt(msg, e, n)
    encoded_msg = rsa.encode_message(encrypted_msg)
    client.publish(client.topic, encoded_msg)


def send_message(client, msg):
    client.publish(client.topic, msg)


def wait_for_publish(client):
    while not client.published:
        time.sleep(0.5)


def main_application(client, secure):
    while True:
        client.published = False
        msg = input()
        if msg == "quit":
            break
        msg = client.client_id + ";" + msg
        if secure == "1":
            encrypt_and_send_message(client, msg)
            wait_for_publish(client)
        else:
            send_message(client, msg)
            wait_for_publish(client)


if __name__ == '__main__':
    client_id = sys.argv[1]

    topic = sys.argv[2]

    secure = sys.argv[3]
    
    client = mqtt.Client(client_id)

    if secure == "1":
        settings.generate_keys(client_id)

    PubSubUtil.set_callbacks(client)

    client.subscribed = False

    client.published = False

    client.client_id = client_id

    client.topic = topic

    PubSubUtil.connect_client(client, "localhost", 1883)

    client.loop_start()

    PubSubUtil.wait_for_connection(client)

    client.subscribe(topic)

    PubSubUtil.wait_for_subscription(client)

    main_application(client, secure)

    client.loop_stop()

    client.disconnect()
