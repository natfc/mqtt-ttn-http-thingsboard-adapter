from paho.mqtt import client as mqtt_client
import random
import json
import requests


client_id = f'python-mqtt-{random.randint(0, 1000)}'

# Callback for when a client connects
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Connected successfully for client {userdata['username']}")
        client.subscribe(userdata["topic"])
    else:
        print(f"Failed to connect for client {userdata['username']}, return code {rc}")

# Callback for when a message is received
def on_message(client, userdata, msg):
    print(f"Message received for {userdata['username']}")
    # print(f"Message received for {userdata['username']} on topic {msg.topic}: {msg.payload.decode()}")
    raw_payload = msg.payload.decode()
    payload = json.loads(raw_payload)

    decoded_payload = payload["uplink_message"]["decoded_payload"]
    print(f"decoded for {userdata['username']}")
    api_endpoint = get_api_endpoint(userdata["username"])
    response = requests.post(api_endpoint, json=decoded_payload)
    print(response)



def get_api_endpoint(username):
    for client in clients_config:
        if client["username"]==username:
            return client["api_endpoint"]
    raise NameError






with open("./src/config.json") as f:
    config = json.load(f)

common_config = config["common"]
clients_config = config["clients"]

clients = []
for client_cfg in clients_config:
    client = mqtt_client.Client(client_id)
    client.username_pw_set(client_cfg["username"], common_config["password"])
    client.user_data_set({"username": client_cfg["username"], "topic": client_cfg["topic"]})
    client.on_connect = on_connect
    client.on_message = on_message

    # Connect to the broker
    client.connect(common_config["broker"], common_config["port"], 500)
    clients.append(client)

# Once all clients are connected, we start all clients' loop
for client in clients:
    client.loop_start()

try:
    while True:
        pass
except KeyboardInterrupt:
    print("Stopping clients...")
    for client in clients:
        client.loop_stop()
        client.disconnect()

