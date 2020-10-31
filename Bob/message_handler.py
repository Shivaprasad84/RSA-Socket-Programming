import rsa
import settings

class MessageHandler:
    @staticmethod
    def __print_message(message):
        try:
            client_id, msg = message.split(';')
            print(f"{client_id}: {msg}")
        except:
            print(message)
        

    @staticmethod
    def handle_message(message):
        try:
            decoded_message = rsa.decode_message(message)
            decrypted_message = rsa.decrypt(decoded_message, settings.keys.private_key, settings.keys.modulus)
            MessageHandler.__print_message(decrypted_message)
        except:
            MessageHandler.__print_message(message)


        
        
