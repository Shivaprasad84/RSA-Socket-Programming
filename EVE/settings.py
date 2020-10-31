import rsa
import json

def write_keys_to_file(keys):
    with open('../PublicKeys/public_keys.json', 'r') as file:
        data = json.load(file)
        data["pub_key_eve"]["e"] = keys.public_key
        data["pub_key_eve"]["n"] = keys.modulus

    with open('../PublicKeys/public_keys.json', 'w') as file:
        json.dump(data, file)
    

def generate_keys(client_id):
    global keys
    p = 193
    q = 223
    print("key generation started...\n")
    keys = rsa.generate_key_pairs(p, q)
    write_keys_to_file(keys)
    print(f"\t{client_id}'s' keys" )
    print(keys)