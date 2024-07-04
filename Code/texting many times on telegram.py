from telethon.sync import TelegramClient

api_id = '22552017'                                                                                   
api_hash = 'f98c95bbe3a69abca4f3dfc5c0c69876'                                                                                             

phone_number = '+49 160 7521767'

yr_target = str(input('your target? : ')) # here is the nickname of the person who will receive messages from you

message = str(input('your text for spam here: ')) # here's a message to him

with TelegramClient(phone_number, api_id, api_hash) as client: 
    client.start()

    
    entity = yr_target # here we pass the nickname to another variable that will be used in sending
    
    for x in range(100): # here is the number of messages how many the code will send
        client.send_message(entity, message) # repeating text will be written here to the selected person
    