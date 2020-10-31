# RSA Socket Programming

## Prerequisites

1) Install paho-mqtt client ```pip install paho-mqtt```

2) Install mosquitto broker <https://mosquitto.org/download/> for windows and ```sudo apt-get install mosquitto``` in linux

3) Run: python3 alice.py <client_id> <topic_name> <secure(1)/not_secure(0)>

4) Run: python3 bob.py <client_id> <topic_name> <secure(1)/not_secure(0)>

5) Run: python3 eve.py <client_id> <topic_name> <secure(1)/not_secure(0)>

Keep all the client ids different and make each client subscrie to same topic. In a secure (1) channel eve would not be able to listen in on the coversation between Alice and Bob.
